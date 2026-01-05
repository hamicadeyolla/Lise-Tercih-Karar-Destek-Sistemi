import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime
import os
import webbrowser   # Harita ve link işlemleri için
import csv          # Excel (CSV) raporlama için
import requests     # İnternetten veri çekmek için (Google Maps API)
import threading    # Arayüz donmasını engellemek için
import time         # İşlem yönetimi için
import math         # Matematiksel hesaplamalar ve Haversine formülü için
from abc import ABC, abstractmethod # Soyut Sınıf (Abstraction) için gerekli
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükler
# =============================================================================
# BÖLÜM 1: KÜTÜPHANE VE MODÜL KONTROLLERİ
# =============================================================================

try:
    from fpdf import FPDF
except ImportError:
    messagebox.showerror("Eksik Kütüphane", "PDF özelliği için 'fpdf' kütüphanesi gerekli.\nLütfen terminalden 'pip install fpdf' yazarak kurun.")

# Veri Dosyası Kontrolü (data.py)
try:
    from data import OKUL_VERITABANI
except ImportError:
    messagebox.showerror("Kritik Hata", "data.py dosyası bulunamadı!\nLütfen aynı klasörde olduğundan emin olun.")
    OKUL_VERITABANI = []

# =============================================================================
# BÖLÜM 2: KONUM ANALİZ MOTORU
# =============================================================================
class LocationAnalyzer:
    """
    [OOP - Encapsulation & Algoritma]
    Bu sınıf, Google Places API ve Matematiksel Algoritmalar kullanarak okul çevresini analiz eder.
    
    Özellikler (v10.11 - Detaylı Rapor):
    1. İsim Detayı: Hastane, Polis vb. yerlerin isimleri raporda yazar.
    2. Haversine: Kuş uçuşu mesafe.
    3. Akıllı Filtre: Kantinleri ve lokantaları kafe saymaz.
    4. Kafe Yarıçapı: 250m (Sadece çok yakın olanlar).
    """
    def __init__(self):
        
        self.api_key = os.getenv("GOOGLE_API_KEY")
        
        self.base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        self.cache = {} # Performans için önbellek

    def _haversine(self, lat1, lon1, lat2, lon2):
        """
        [ALGORİTMA] Haversine Formülü
        İki GPS koordinatı arasındaki mesafeyi matematiksel olarak hesaplar.
        """
        R = 6371000  # Dünya'nın yarıçapı
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return int(distance)

    def analiz_et(self, lat, lon):
       
        if not self.api_key:
            return None, "API Key Eksik! .env dosyasını kontrol edin."

        koordinat_anahtari = (lat, lon)
        if koordinat_anahtari in self.cache:
            return self.cache[koordinat_anahtari]

        # Sonuçları tutacak sözlük yapısı
        analiz_sonuclari = {
            "ulasim": {"sayi": 0, "isimler": []},     
            "hastane": {"sayi": 0, "isimler": []},
            "polis": {"sayi": 0, "isimler": []},
            "kutuphane": {"sayi": 0, "isimler": []},
            "bar": {"sayi": 0, "isimler": []},       
            "cafe": {"sayi": 0, "isimler": []},       
            "kumar": {"sayi": 0, "isimler": []},      
            "oyun": {"sayi": 0, "isimler": []}        
        }

        # 1. ADIM: POZİTİF UNSURLAR
        ulasim_tipleri = ["subway_station", "light_rail_station", "train_station"]
        for tip in ulasim_tipleri:
            self._google_ara(lat, lon, tip, 1000, "ulasim", analiz_sonuclari)

        self._google_ara(lat, lon, "hospital", 1500, "hastane", analiz_sonuclari)
        self._google_ara(lat, lon, "library", 1000, "kutuphane", analiz_sonuclari)
        self._google_ara(lat, lon, "police", 1000, "polis", analiz_sonuclari)

        # 2. ADIM: NEGATİF UNSURLAR
        self._google_ara(lat, lon, "bar", 800, "bar", analiz_sonuclari)
        self._google_ara(lat, lon, "casino", 600, "kumar", analiz_sonuclari)

        # [ÖNEMLİ] Kafe Araması (250m Yarıçap + Filtreli Mod)
        self._google_ara(lat, lon, "cafe", 250, "cafe", analiz_sonuclari, filtreli=True)

        # 3. ADIM: KEYWORD ARAMALAR
        ozel_aramalar = [
            ("iddaa", "kumar"), ("sayısal loto", "kumar"), ("ganyan", "kumar"),
            ("internet cafe", "oyun"), ("playstation cafe", "oyun")
        ]
        for kelime, kategori in ozel_aramalar:
            self._keyword_ara(lat, lon, kelime, 600, kategori, analiz_sonuclari)

        # 4. ADIM: PUANLAMA
        final_score, yorum = self.puanla_ve_raporla(analiz_sonuclari)
        self.cache[koordinat_anahtari] = (final_score, yorum)
        return final_score, yorum

    def _google_ara(self, okul_lat, okul_lon, tip, radius, kategori_key, sonuc_sozlugu, filtreli=False):
        """Yardımcı Fonksiyon: API sorgusu yapar, sonuçları filtreler."""
        try:
            params = {'location': f"{okul_lat},{okul_lon}", 'radius': radius, 'type': tip, 'key': self.api_key, 'language': 'tr'}
            resp = requests.get(self.base_url, params=params, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                
                # --- AKILLI FİLTRE LİSTESİ ---
                yasakli_kelimeler = ["lokanta", "restoran", "kebap", "pide", "köfte", "yemek", 
                                     "pastane", "fırın", "börek", "kantin", "büfe", "döner", 
                                     "market", "bakkal", "okul", "lise", "kolej", "avm"]

                for yer in data.get('results', []):
                    yer_adi = yer['name']
                    
                    if filtreli:
                        yer_adi_kucuk = yer_adi.lower()
                        if any(yasak in yer_adi_kucuk for yasak in yasakli_kelimeler):
                            continue 

                    yer_lat = yer['geometry']['location']['lat']
                    yer_lng = yer['geometry']['location']['lng']
                    mesafe = self._haversine(okul_lat, okul_lon, yer_lat, yer_lng)
                    
                    zaten_var = any(yer_adi in kayit for kayit in sonuc_sozlugu[kategori_key]["isimler"])
                    if not zaten_var:
                        sonuc_sozlugu[kategori_key]["isimler"].append(f"{yer_adi} ({mesafe}m)")
                        sonuc_sozlugu[kategori_key]["sayi"] += 1
        except Exception:
            pass 

    def _keyword_ara(self, okul_lat, okul_lon, keyword, radius, kategori_key, sonuc_sozlugu):
        try:
            params = {'location': f"{okul_lat},{okul_lon}", 'radius': radius, 'keyword': keyword, 'key': self.api_key}
            resp = requests.get(self.base_url, params=params, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                for yer in data.get('results', []):
                    yer_adi = yer['name']
                    yer_lat = yer['geometry']['location']['lat']
                    yer_lng = yer['geometry']['location']['lng']
                    mesafe = self._haversine(okul_lat, okul_lon, yer_lat, yer_lng)
                    
                    zaten_var = any(yer_adi in kayit for kayit in sonuc_sozlugu[kategori_key]["isimler"])
                    if not zaten_var:
                        sonuc_sozlugu[kategori_key]["isimler"].append(f"{yer_adi} ({mesafe}m)")
                        sonuc_sozlugu[kategori_key]["sayi"] += 1
        except Exception:
            pass

    def puanla_ve_raporla(self, ozet):
        """Analiz sonuçlarını puana ve DETAYLI metne çevirir."""
        base_score = 50 
        
        # --- POZİTİF PUANLAR ---
        base_score += 20 if ozet["ulasim"]["sayi"] > 0 else 0
        base_score += 10 if ozet["hastane"]["sayi"] > 0 else 0
        base_score += 10 if ozet["polis"]["sayi"] > 0 else 0
        base_score += 10 if ozet["kutuphane"]["sayi"] > 0 else 0
        
        # --- NEGATİF PUANLAR ---
        ceza_kumar = min(ozet["kumar"]["sayi"], 3) * 5 
        ceza_oyun = min(ozet["oyun"]["sayi"], 2) * 5
        ceza_bar = min(ozet["bar"]["sayi"], 3) * 5
        ceza_cafe = min(ozet["cafe"]["sayi"], 2) * 5 
        
        base_score -= (ceza_kumar + ceza_oyun + ceza_bar + ceza_cafe)
        final_score = max(0, min(100, base_score))
        
        # --- DETAYLI RAPOR METNİ ---
        yorum = f"CEVRESEL GUVENLIK ANALIZI\nSkor: {final_score}/100\n" + "="*55 + "\n"
        
        # Ulaşım
        if ozet["ulasim"]["sayi"] > 0:
            istasyonlar = ", ".join(ozet["ulasim"]["isimler"][:3]) 
            if len(ozet["ulasim"]["isimler"]) > 3: istasyonlar += "..."
            yorum += f"Ulasim (+20): VAR - {istasyonlar} \n"
        else:
            yorum += "Ulasim: Yakinda Metro/Banliyo bulunamadi.\n"

        # Hastane (İsimleri ekledik)
        if ozet["hastane"]["sayi"] > 0:
            hastane_isimleri = ", ".join(ozet["hastane"]["isimler"][:2]) # İlk 2 hastaneyi yaz
            yorum += f"Saglik (+10): VAR - {hastane_isimleri}\n"
        else:
            yorum += f"Saglik (+10): Yok\n"

        # Polis (İsimleri ekledik)
        if ozet["polis"]["sayi"] > 0:
            polis_isimleri = ", ".join(ozet["polis"]["isimler"][:1]) # En yakın merkezi yaz
            yorum += f"Guvenlik (+10): VAR - {polis_isimleri}\n"
        else:
            yorum += f"Guvenlik (+10): Yok\n"

        # Kütüphane (İsimleri ekledik)
        if ozet["kutuphane"]["sayi"] > 0:
            lib_isimleri = ", ".join(ozet["kutuphane"]["isimler"][:2])
            yorum += f"Kutuphane (+10): VAR - {lib_isimleri}\n"
        else:
            yorum += f"Kutuphane (+10): Yok\n"

        yorum += "-"*55 + "\nRISK ANALIZI (Filtrelenmis):\n"
        yorum += f"Sans Oyunlari: {ozet['kumar']['sayi']} (Ceza: -{ceza_kumar})\n"
        yorum += f"Oyun Salonu: {ozet['oyun']['sayi']} (Ceza: -{ceza_oyun})\n"
        yorum += f"Alkollu Mekan: {ozet['bar']['sayi']} (Ceza: -{ceza_bar})\n"
        yorum += f"Sosyal Yogunluk (Cafe): {ozet['cafe']['sayi']} (Ceza: -{ceza_cafe})\n"
        
        return final_score, yorum

# =============================================================================
# BÖLÜM 3: VERİ MODELİ (OOP - ENCAPSULATION)
# =============================================================================
class School:
    def __init__(self, veri):
        self.__ad = veri["ad"]
        self.__puan = veri["puan"]
        self.__yuzdelik = veri["yuzdelik"]
        self.__ilce = veri.get("ilce", "Belirtilmemiş")
        self.__lat = veri.get("lat", 39.9208)
        self.__lon = veri.get("lon", 32.8541)
        
        self.__ozellikler = {
            "Spor Salonu": veri.get("spor", False),
            "Yemekhane": veri.get("yemek", False),
            "Kütüphane": veri.get("kutuphane", True),
            "Konferans Salonu": veri.get("konferans", False),
            "Bilgisayar Lab.": veri.get("bilg_lab", False),
            "Fen Laboratuvarı": veri.get("fen_lab", False),
            "Kantin": veri.get("kantin", False)
        }
        self.eksik_ozellikler = [] 

    # Getter metodları
    def get_ad(self): return self.__ad
    def get_puan(self): return self.__puan
    def get_yuzdelik(self): return self.__yuzdelik
    def get_ilce(self): return self.__ilce
    def get_coords(self): return self.__lat, self.__lon
    
    def ozellik_var_mi(self, ozellik): return self.__ozellikler.get(ozellik, False)
    def eksik_ekle(self, ozellik): self.eksik_ozellikler.append(ozellik)
    def eksikleri_temizle(self): self.eksik_ozellikler = []
    def get_eksikler(self): return self.eksik_ozellikler
    def tum_ozellikleri_getir(self): return self.__ozellikler

# =============================================================================
# BÖLÜM 4: RAPORLAMA MODÜLÜ (OOP - ABSTRACTION & POLYMORPHISM)
# =============================================================================
class ReportGenerator(ABC):
    @abstractmethod
    def olustur(self, dosya_yolu, veri_paketi, ekstra_bilgi=""):
        pass

class PDFReport(ReportGenerator, FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        baslik = self.tr_to_en('LISE TERCIH KARAR DESTEK SISTEMI')
        self.cell(0, 10, baslik, 0, 1, 'C')
        self.ln(5)

    def tr_to_en(self, text):
        if not text: return ""
        ceviri = {'ğ': 'g', 'Ğ': 'G', 'ş': 's', 'Ş': 'S', 'ı': 'i', 'İ': 'I', 'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C'}
        for tr, eng in ceviri.items(): text = text.replace(tr, eng)
        return text.encode('latin-1', 'replace').decode('latin-1')

    def olustur(self, dosya_yolu, veri_paketi, ekstra_bilgi=""):
        self.add_page()
        self.set_font('Arial', '', 11)
        self.cell(0, 10, self.tr_to_en(f"Rapor Tarihi: {datetime.datetime.now().strftime('%d.%m.%Y')}"), 0, 1)
        self.cell(0, 10, self.tr_to_en(f"Ogrenci Yuzdelik: {ekstra_bilgi}"), 0, 1)
        self.ln(5)
        
        self.set_fill_color(230, 126, 34); self.set_text_color(255, 255, 255)
        self.cell(0, 10, self.tr_to_en(" HEDEF TERCIHLER (Yuksek Puanli)"), 0, 1, 'L', 1)
        self.set_text_color(0, 0, 0)
        
        if not veri_paketi["hedef"]:
            self.cell(0, 10, self.tr_to_en("- Hedef tercih bulunamadi."), 0, 1)
        else:
            for okul in veri_paketi["hedef"]: self.satir_yaz(okul)
        
        self.ln(5)
        self.set_fill_color(39, 174, 96); self.set_text_color(255, 255, 255)
        self.cell(0, 10, self.tr_to_en(" GUVENLI TERCIHLER (Yerlesme Ihtimali Yuksek)"), 0, 1, 'L', 1)
        self.set_text_color(0, 0, 0)
        
        if not veri_paketi["guvenli"]:
            self.cell(0, 10, self.tr_to_en("- Uygun okul bulunamadi."), 0, 1)
        else:
            for okul in veri_paketi["guvenli"]: self.satir_yaz(okul)
        self.output(dosya_yolu)

    def satir_yaz(self, okul):
        ham_durum = "Tam Uygun" if not okul.get_eksikler() else f"Eksik: {', '.join(okul.get_eksikler())}"
        self.set_font('Arial', 'B', 10)
        self.cell(0, 8, self.tr_to_en(f"- {okul.get_ad()} ({okul.get_ilce()}) - %{okul.get_yuzdelik()}"), 0, 1)
        self.set_font('Arial', 'I', 9) 
        self.cell(0, 5, self.tr_to_en(f"   Durum: {ham_durum}"), 0, 1)

class CSVReport(ReportGenerator):
    def olustur(self, dosya_yolu, veri_paketi, ekstra_bilgi=""):
        try:
            with open(dosya_yolu, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';') 
                writer.writerow(["Kategori", "Okul Adı", "İlçe", "Puan", "Yüzdelik", "Eksik Özellikler", "Öğrenci Notu"])
                for okul in veri_paketi["hedef"]: self.satir_ekle(writer, okul, "HEDEF", ekstra_bilgi)
                for okul in veri_paketi["guvenli"]: self.satir_ekle(writer, okul, "GUVENLI", ekstra_bilgi)
        except PermissionError:
            raise Exception("Dosya şu anda açık! Lütfen Excel dosyasını kapatıp tekrar deneyin.")
        except Exception as e:
            raise e

    def satir_ekle(self, writer, okul, kategori, not_bilgisi):
        eksikler = ", ".join(okul.get_eksikler()) if okul.get_eksikler() else "Tam Uygun"
        writer.writerow([kategori, okul.get_ad(), okul.get_ilce(), str(okul.get_puan()).replace('.', ','), str(okul.get_yuzdelik()).replace('.', ','), eksikler, not_bilgisi])

# =============================================================================
# BÖLÜM 5: KARAR MOTORU
# =============================================================================
class DecisionEngine:
    def __init__(self):
        self.okullar = [School(veri) for veri in OKUL_VERITABANI]
        self.okul_isimleri = sorted([o.get_ad() for o in self.okullar])

    def detayli_analiz(self, kriterler, ogr_yuzdelik, secilen_ilce="Tümü"):
        kazanilanlar = []
        hedefler = []
        for okul in self.okullar:
            if secilen_ilce != "Tümü" and okul.get_ilce() != secilen_ilce: continue 
            okul.eksikleri_temizle()
            for kriter in kriterler:
                if not okul.ozellik_var_mi(kriter): okul.eksik_ekle(kriter)
            
            if ogr_yuzdelik <= okul.get_yuzdelik(): kazanilanlar.append(okul)
            elif (ogr_yuzdelik - okul.get_yuzdelik()) < 1.5: hedefler.append(okul)
                
        kazanilanlar.sort(key=lambda x: x.get_yuzdelik())
        hedefler.sort(key=lambda x: x.get_yuzdelik())
        return kazanilanlar, hedefler
    
    def get_tum_ilceler(self):
        ilceler = set()
        for okul in self.okullar: ilceler.add(okul.get_ilce())
        return ["Tümü"] + sorted(list(ilceler))
    
    def get_okul_by_name(self, ad):
        for o in self.okullar:
            if o.get_ad() == ad: return o
        return None

# =============================================================================
# BÖLÜM 6: ARAYÜZ KATMANI (GUI)
# =============================================================================
class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lise Tercih Karar Destek Sistemi") 
        self.geometry("1300x800")
        self.configure(bg="#ecf0f1")
        
        self.motor = DecisionEngine()
        self.konum_analizcisi = LocationAnalyzer() 
        self.son_kazanilanlar = []
        self.son_hedefler = []
        self.status_var = tk.StringVar(value="Sistem Hazır.")
        
        self.stil_ayarla()
        self.menuyu_olustur()
        self.ana_cerceveleri_olustur()
        self.sidebar_doldur()
        self.icerik_doldur()

    def stil_ayarla(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", foreground="black", rowheight=30, fieldbackground="white", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#34495e", foreground="white", font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[('selected', '#3498db')])

    def menuyu_olustur(self):
        menubar = tk.Menu(self)
        dosya = tk.Menu(menubar, tearoff=0)
        dosya.add_command(label="Yenile / Temizle", command=self.sifirla)
        dosya.add_separator()
        dosya.add_command(label="PDF Rapor Al", command=self.rapor_al_pdf)
        dosya.add_command(label="Excel (CSV) Aktar", command=self.rapor_al_excel)
        dosya.add_separator()
        dosya.add_command(label="Çıkış", command=self.quit)
        menubar.add_cascade(label="Dosya", menu=dosya)
        
        yardim = tk.Menu(menubar, tearoff=0)
        yardim.add_command(label="Hakkında", command=self.hakkinda_goster)
        menubar.add_cascade(label="Yardım", menu=yardim)
        self.config(menu=menubar)

    def ana_cerceveleri_olustur(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=300)
        self.sidebar.pack(side="left", fill="y")
        self.main_area = tk.Frame(self, bg="#ecf0f1")
        self.main_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def sidebar_doldur(self):
        tk.Label(self.sidebar, text="🎓 LİSE TERCİH\nSİSTEMİ", bg="#2c3e50", fg="#f1c40f", font=("Segoe UI", 24, "bold")).pack(pady=20)
        
        frm = tk.LabelFrame(self.sidebar, text="Öğrenci Bilgileri", bg="#2c3e50", fg="white", font=("Segoe UI", 10, "bold"))
        frm.pack(fill="x", padx=15, pady=10)
        tk.Label(frm, text="Yüzdelik Dilim:", bg="#2c3e50", fg="#bdc3c7").pack(anchor="w", padx=5)
        self.ent_yuzdelik = tk.Entry(frm, font=("Segoe UI", 12))
        self.ent_yuzdelik.pack(fill="x", padx=5, pady=5)

        tk.Label(frm, text="İlçe Tercihi:", bg="#2c3e50", fg="#bdc3c7").pack(anchor="w", padx=5, pady=(10,0))
        self.cmb_ilce = ttk.Combobox(frm, values=self.motor.get_tum_ilceler(), state="readonly", font=("Segoe UI", 10))
        self.cmb_ilce.current(0)
        self.cmb_ilce.pack(fill="x", padx=5, pady=5)
        
        frm2 = tk.LabelFrame(self.sidebar, text="Beklentiler", bg="#2c3e50", fg="white", font=("Segoe UI", 10, "bold"))
        frm2.pack(fill="x", padx=15, pady=10)
        self.vars = {}
        for k in ["Kütüphane", "Spor Salonu", "Yemekhane", "Konferans Salonu", "Bilgisayar Lab.", "Fen Laboratuvarı", "Kantin"]:
            var = tk.BooleanVar()
            tk.Checkbutton(frm2, text=k, variable=var, bg="#2c3e50", fg="white", selectcolor="#2c3e50", activebackground="#2c3e50", anchor="w").pack(fill="x", padx=5)
            self.vars[k] = var

        tk.Button(self.sidebar, text="🚀 ANALİZİ BAŞLAT", command=self.hesapla, bg="#e74c3c", fg="white", font=("Segoe UI", 12, "bold"), pady=10).pack(fill="x", padx=15, pady=10)
        
        tk.Button(self.sidebar, text="🧠 Akıllı Karar Destek Sistemi", command=self.akilli_oneri_sistemi, bg="#9b59b6", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="💾 Excel'e Kaydet", command=self.rapor_al_excel, bg="#16a085", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        
        tk.Label(self.sidebar, text="Araçlar", bg="#2c3e50", fg="#95a5a6", font=("Segoe UI", 10, "underline")).pack(pady=(15,5))
        tk.Button(self.sidebar, text="🆚 Okulları Karşılaştır", command=self.karsilastirma_modulu_ac, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="📄 PDF Rapor Oluştur", command=self.rapor_al_pdf, bg="#e67e22", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="📚 Tüm Okul Listesini Gör", command=self.tum_okullari_ac, bg="#34495e", fg="white", font=("Segoe UI", 10), pady=5).pack(side="bottom", fill="x", padx=15, pady=20)

    def icerik_doldur(self):
        tk.Label(self.main_area, text="Analiz Sonuçları (Detay ve Harita için okula çift tıklayın)", bg="#ecf0f1", fg="#2c3e50", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 10))
        table_frame = tk.Frame(self.main_area, bg="#ecf0f1")
        table_frame.pack(fill="both", expand=True)
        table_frame.grid_columnconfigure(0, weight=1, uniform="group1")
        table_frame.grid_columnconfigure(1, weight=1, uniform="group1")
        table_frame.grid_rowconfigure(0, weight=1)

        frm1 = tk.LabelFrame(table_frame, text="🎯 Hedef Tercihler", bg="white", fg="#e67e22", font=("Segoe UI", 11, "bold"))
        frm1.grid(row=0, column=0, sticky="nsew", padx=(0, 5)) 
        self.tree_hedef = self.tablo_yarat(frm1)

        frm2 = tk.LabelFrame(table_frame, text="✅ Güvenli Tercihler", bg="white", fg="#27ae60", font=("Segoe UI", 11, "bold"))
        frm2.grid(row=0, column=1, sticky="nsew", padx=(5, 0)) 
        self.tree_kazan = self.tablo_yarat(frm2)
        
        self.tree_hedef.bind("<Double-1>", self.okul_detay_ac)
        self.tree_kazan.bind("<Double-1>", self.okul_detay_ac)

    def tablo_yarat(self, parent):
        container = tk.Frame(parent)
        container.pack(fill="both", expand=True)
        cols = ("Okul", "İlçe", "Yüzdelik", "Durum")
        tree = ttk.Treeview(container, columns=cols, show="headings")
        tree.column("Okul", width=250, minwidth=150) 
        tree.column("İlçe", width=90, anchor="center")
        tree.column("Yüzdelik", width=70, anchor="center")
        tree.column("Durum", width=200)
        for c in cols: tree.heading(c, text=c)
        
        yscroll = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        xscroll = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscroll=yscroll.set, xscroll=xscroll.set)
        tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        tree.tag_configure('tam_uyumlu', background='#d4edda')
        tree.tag_configure('eksik_var', background='#fff3cd')
        tree.tag_configure('riskli', background='#f8d7da')
        return tree

    def hesapla(self):
        try:
            val = self.ent_yuzdelik.get().replace(",", ".")
            yuzdelik = float(val)
        except ValueError:
            messagebox.showwarning("Hata", "Geçerli bir yüzdelik girin!")
            return False
        
        secimler = [k for k, v in self.vars.items() if v.get()]
        k, h = self.motor.detayli_analiz(secimler, yuzdelik, self.cmb_ilce.get())
        self.son_kazanilanlar = k
        self.son_hedefler = h
        self.doldur(self.tree_kazan, k)
        self.doldur(self.tree_hedef, h, is_hedef=True)
        self.status_var.set(f"Analiz Tamamlandı: {len(k)} güvenli, {len(h)} hedef okul bulundu.")
        return True

    def doldur(self, tree, liste, is_hedef=False):
        for i in tree.get_children(): tree.delete(i)
        for okul in liste:
            eksikler = okul.get_eksikler()
            tag = 'riskli' if is_hedef and not eksikler else ('eksik_var' if eksikler else 'tam_uyumlu')
            notu = f"⚠️ Eksik: {', '.join(eksikler)}" if eksikler else "✔️ Tam Uygun"
            tree.insert("", "end", values=(okul.get_ad(), okul.get_ilce(), f"%{okul.get_yuzdelik()}", notu), tags=(tag,))

    # [OOP - POLYMORPHISM KULLANIMI]
    def raporu_baslat(self, generator: ReportGenerator, dosya_uzantisi, dosya_tipi):
        if not self.son_kazanilanlar and not self.son_hedefler:
            if not self.hesapla(): return

        dosya_yolu = filedialog.asksaveasfilename(defaultextension=dosya_uzantisi, filetypes=[(dosya_tipi, dosya_uzantisi)], title="Raporu Kaydet")
        if not dosya_yolu: return
        
        try:
            # ARTIK TEK BİR LİSTE DEĞİL, KATEGORİLEŞTİRİLMİŞ VERİ PAKETİ GÖNDERİYORUZ
            veri_paketi = {
                "hedef": self.son_hedefler,
                "guvenli": self.son_kazanilanlar
            }
            generator.olustur(dosya_yolu, veri_paketi, ekstra_bilgi=f"%{self.ent_yuzdelik.get()}")
            messagebox.showinfo("Başarılı", f"Rapor başarıyla oluşturuldu:\n{dosya_yolu}")
        except Exception as e:
            messagebox.showerror("Hata", f"Rapor hatası: {str(e)}")

    def rapor_al_pdf(self):
        self.raporu_baslat(PDFReport(), ".pdf", "PDF Dosyası")

    def rapor_al_excel(self):
        self.raporu_baslat(CSVReport(), ".csv", "Excel CSV")

    def okul_detay_ac(self, event):
        tree = event.widget
        sel = tree.selection()
        if not sel: return
        item = tree.item(sel)
        okul_adi = item['values'][0]
        
        secili_okul = next((o for o in self.motor.okullar if str(o.get_ad()) == str(okul_adi)), None)
        if not secili_okul: return

        win = tk.Toplevel(self)
        win.title(f"{secili_okul.get_ad()} - Detay Kartı")
        win.geometry("750x750")
        win.configure(bg="white")
        win.attributes('-topmost', 'true')
        
        top_btn_frame = tk.Frame(win, bg="white")
        top_btn_frame.pack(anchor="ne", padx=10, pady=5)
        
        tk.Button(top_btn_frame, text="KAPAT", command=win.destroy, bg="#e74c3c", fg="white", font=("Arial",10,"bold")).pack(side="right", padx=2)
        
        def haritada_ac():
            ad = secili_okul.get_ad().replace(" ", "+")
            ilce = secili_okul.get_ilce().replace(" ", "+")
            webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={ad}+{ilce}+Ankara")
            
        tk.Button(top_btn_frame, text="📍 Haritada Göster", command=haritada_ac, bg="#3498db", fg="white", font=("Arial",10,"bold")).pack(side="right", padx=2)
        
        tk.Label(win, text=secili_okul.get_ad(), font=("Segoe UI", 16, "bold"), bg="white", fg="#2c3e50", wraplength=600).pack()
        tk.Label(win, text=f"📍 {secili_okul.get_ilce()} - Ankara", font=("Segoe UI", 12), bg="white", fg="#7f8c8d").pack()
        
        analiz_frame = tk.LabelFrame(win, text="🌍 Profesyonel Çevre Analizi (GOOGLE MAPS)", bg="#f0f3f4", font=("Segoe UI", 10, "bold"), fg="#2980b9")
        analiz_frame.pack(fill="both", expand=True, padx=20, pady=10)
        analiz_frame.columnconfigure(0, weight=1) 
        analiz_frame.columnconfigure(1, weight=0)

        lbl_sonuc = tk.Label(analiz_frame, text="Okul çevresindeki Metro, Polis, Bahis Bayileri vb.\nanaliz etmek için butona basın.", bg="#f0f3f4", justify="left", anchor="nw")
        lbl_sonuc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        btn_analiz = tk.Button(analiz_frame, text="ANALİZ ET 🛰️", bg="#8e44ad", fg="white", font=("Segoe UI", 10, "bold"))
        btn_analiz.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        lbl_skor = tk.Label(analiz_frame, text="", font=("Segoe UI", 14, "bold"), bg="#f0f3f4")
        lbl_skor.grid(row=1, column=0, columnspan=2, sticky="se", padx=10, pady=10)
        
        def yeniden_boyutlandir(event):
            yeni_genislik = event.width - 150 
            lbl_sonuc.config(wraplength=yeni_genislik)
        analiz_frame.bind("<Configure>", yeniden_boyutlandir)

        def analizi_baslat():
            btn_analiz.config(text="Hesaplanıyor...", state="disabled", bg="#95a5a6")
            lbl_sonuc.config(text="Google ile veriler çekiliyor...")
            def islem():
                lat, lon = secili_okul.get_coords()
                puan, yorum = self.konum_analizcisi.analiz_et(lat, lon)
                
                def arayuzu_guncelle():
                    if puan is None:
                        lbl_sonuc.config(text=f"⚠️ {yorum}", fg="red")
                        btn_analiz.config(text="Tekrar Dene", state="normal", bg="#e74c3c")
                    else:
                        renk = "#27ae60" if puan >= 75 else ("#e67e22" if puan >= 50 else "#c0392b")
                        lbl_sonuc.config(text=yorum, fg="#2c3e50", font=("Consolas", 9))
                        lbl_skor.config(text=f"SKOR: {puan} / 100", fg=renk)
                        btn_analiz.config(text="Analiz Tamamlandı", state="disabled", bg="#27ae60")
                win.after(0, arayuzu_guncelle)
            threading.Thread(target=islem, daemon=True).start()
        btn_analiz.config(command=analizi_baslat)
        
        frm = tk.Frame(win, bg="#ecf0f1", pady=10)
        frm.pack(fill="x", padx=20, pady=10)
        tk.Label(frm, text=f"LGS: {secili_okul.get_puan()}", font=("Segoe UI",12,"bold"), bg="#2980b9", fg="white").pack(side="left", padx=20)
        tk.Label(frm, text=f"Dilim: %{secili_okul.get_yuzdelik()}", font=("Segoe UI",12,"bold"), fg="#e67e22").pack(side="right", padx=20)
        
        tk.Label(win, text="İmkanlar", font=("Segoe UI",11,"underline"), bg="white", fg="#95a5a6").pack(pady=5)
        g_frm = tk.Frame(win, bg="white")
        g_frm.pack(pady=10)
        r, c = 0, 0
        for k, v in secili_okul.tum_ozellikleri_getir().items():
            ikon, color = ("✅", "#27ae60") if v else ("❌", "#c0392b")
            tk.Label(g_frm, text=f"{ikon} {k}", fg=color, bg="white", width=20, relief="groove").grid(row=r, column=c, padx=2, pady=2)
            c += 1
            if c > 2: c=0; r+=1

    def akilli_oneri_sistemi(self):
        tum_liste = self.son_kazanilanlar + self.son_hedefler
        if not tum_liste:
            messagebox.showwarning("Veri Yok", "Lütfen önce analiz yapın.")
            return
        
        adaylar = self.son_kazanilanlar[:8] if self.son_kazanilanlar else self.son_hedefler[:8]
        
        wait_win = tk.Toplevel(self)
        wait_win.title("Karar Destek Sistemi")
        wait_win.geometry("350x150")
        tk.Label(wait_win, text="🧠 Okullar Analiz Ediliyor...\n\nGoogle Maps verileri ile karşılaştırma yapılıyor...", font=("Arial", 10)).pack(expand=True)
        self.update()
        
        def hesapla_ve_goster():
            # --- AKADEMİK BARİYERLİ SEÇİM (Fark > 1.5 ise alınmaz) ---
            uygun_adaylar = [] # Sadece farkı <= 1.5 olanlar
            uzak_adaylar = []  # Farkı > 1.5 olanlar (Yedek)
            hata_olustu = False
            hatali_okul_adi = ""
            
            try:
                ogrenci_yuzdelik = float(self.ent_yuzdelik.get().replace(",", "."))
            except:
                ogrenci_yuzdelik = 0.0

            for okul in adaylar:
                lat, lon = okul.get_coords()
                guvenlik_puan, _ = self.konum_analizcisi.analiz_et(lat, lon)
                
                if guvenlik_puan is None:
                    hata_olustu = True
                    hatali_okul_adi = okul.get_ad()
                    break 
                
                # Puanlama
                total_skor = (okul.get_puan() / 5) + (guvenlik_puan * 0.8)
                fark = abs(okul.get_yuzdelik() - ogrenci_yuzdelik)
                
                paket = (okul, total_skor, guvenlik_puan)
                
                # AKADEMİK BARİYER: %1.5
                if fark <= 1.5:
                    uygun_adaylar.append(paket)
                else:
                    uzak_adaylar.append(paket)
            
            # Bariyer içindekilere öncelik ver
            final_liste = uygun_adaylar if uygun_adaylar else uzak_adaylar
            
            self.after(0, lambda: sonuc_ekranini_ac(final_liste, wait_win, hata_olustu, hatali_okul_adi))

        def sonuc_ekranini_ac(analiz_sonuclari, wait_penceresi, hata_var, hatali_okul_adi):
            wait_penceresi.destroy()
            
            if hata_var:
                messagebox.showerror("API Hatası", f"'{hatali_okul_adi}' verisi çekilirken hata oluştu.\nAPI Key'inizi kontrol ediniz.")
                return

            if analiz_sonuclari:
                analiz_sonuclari.sort(key=lambda x: (x[1], x[0].get_puan()), reverse=True)
                en_iyi_data = analiz_sonuclari[0]
                
                okul, skor, g_puan = en_iyi_data
                res_win = tk.Toplevel(self)
                res_win.title("Akıllı Karar Destek Sistemi")
                res_win.geometry("600x500")
                res_win.configure(bg="#fdfefe")
                
                tk.Label(res_win, text="🏆 SİZİN İÇİN EN İDEAL SEÇİM", font=("Segoe UI", 16, "bold"), bg="#fdfefe", fg="#27ae60").pack(pady=20)
                
                card = tk.LabelFrame(res_win, text="Önerilen Okul", font=("Arial", 12, "bold"), bg="white", fg="#2c3e50")
                card.pack(fill="both", expand=True, padx=20, pady=10)
                
                tk.Label(card, text=okul.get_ad(), font=("Arial", 14, "bold"), bg="white", fg="#2980b9", wraplength=500).pack(pady=10)
                tk.Label(card, text=f"📍 {okul.get_ilce()} | Puan: {okul.get_puan()} | Yüzdelik: %{okul.get_yuzdelik()}", bg="white", font=("Arial", 11)).pack()
                
                score_frm = tk.Frame(card, bg="#ecf0f1", pady=10)
                score_frm.pack(fill="x", padx=10, pady=10)
                
                tk.Label(score_frm, text=f"🛡️ Güvenlik İndeksi: {g_puan}/100", font=("Arial", 12, "bold"), bg="#ecf0f1", fg="#e67e22").pack(side="left", padx=20)
                tk.Label(score_frm, text="✅ Akademik Uygunluk: Yüksek", font=("Arial", 12, "bold"), bg="#ecf0f1", fg="#27ae60").pack(side="right", padx=20)
                
                tk.Label(card, text="NEDEN BU OKUL?", font=("Arial", 10, "bold"), bg="white", fg="gray").pack(anchor="w", padx=10)
                reason = f"Google Maps üzerinden yapılan canlı analiz sonucunda; {okul.get_ad()}, hem akademik başarısı hem de çevresel güvenlik/ulaşım imkanlarıyla diğer okullar arasında size en uygun olanı oldu. ({int(skor)}) aldı."
                tk.Label(card, text=reason, bg="white", justify="left", wraplength=500).pack(anchor="w", padx=10, pady=5)
                
                tk.Button(res_win, text="Tamam", command=res_win.destroy, bg="#34495e", fg="white", width=20).pack(pady=10)

        threading.Thread(target=hesapla_ve_goster, daemon=True).start()

    def tum_okullari_ac(self):
        top = tk.Toplevel(self)
        top.title("Tüm Veritabanı ve Detaylı İmkanlar")
        top.geometry("1350x600") 
        top.attributes('-topmost', 'true')
        container = tk.Frame(top)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        cols = ("Okul", "İlçe", "Puan", "Yüzde", "Kütüp.", "Spor", "Yemek", "Konf.", "PC Lab", "Fen Lab", "Kantin")
        tree = ttk.Treeview(container, columns=cols, show="headings")
        tree.column("Okul", width=300, minwidth=200); tree.column("İlçe", width=80, anchor="center")
        for c in cols: tree.heading(c, text=c)
        
        yscroll = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        xscroll = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscroll=yscroll.set, xscroll=xscroll.set)
        tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        container.grid_rowconfigure(0, weight=1); container.grid_columnconfigure(0, weight=1)
        tree.bind("<Double-1>", self.okul_detay_ac) 
        
        for okul in self.motor.okullar:
            oz = okul.tum_ozellikleri_getir()
            tree.insert("", "end", values=(
                okul.get_ad(), okul.get_ilce(), str(okul.get_puan()).replace(".", ","), f"%{okul.get_yuzdelik()}",
                "Var" if oz["Kütüphane"] else "-", "Var" if oz["Spor Salonu"] else "-", "Var" if oz["Yemekhane"] else "-",
                "Var" if oz["Konferans Salonu"] else "-", "Var" if oz["Bilgisayar Lab."] else "-",
                "Var" if oz["Fen Laboratuvarı"] else "-", "Var" if oz["Kantin"] else "-"
            ))

    def karsilastirma_modulu_ac(self):
        win = tk.Toplevel(self)
        win.title("Okul Karşılaştırma Aracı")
        win.geometry("900x600")
        win.configure(bg="#ecf0f1")
        win.attributes('-topmost', 'true')
        
        tk.Label(win, text="İki Okulu Karşılaştır", font=("Segoe UI", 16, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)
        
        select_frm = tk.Frame(win, bg="#ecf0f1")
        select_frm.pack(fill="x", padx=20, pady=10)
        
        tk.Label(select_frm, text="1. Okul:", bg="#ecf0f1", font=("Segoe UI", 10)).pack(side="left", padx=5)
        cmb1 = ttk.Combobox(select_frm, values=self.motor.okul_isimleri, width=40, state="readonly")
        cmb1.pack(side="left", padx=5)
        
        tk.Label(select_frm, text="2. Okul:", bg="#ecf0f1", font=("Segoe UI", 10)).pack(side="left", padx=5)
        cmb2 = ttk.Combobox(select_frm, values=self.motor.okul_isimleri, width=40, state="readonly")
        cmb2.pack(side="left", padx=5)
        
        result_frm = tk.Frame(win, bg="white", relief="sunken", bd=1)
        result_frm.pack(fill="both", expand=True, padx=20, pady=10)
        
        def kiyasla():
            for widget in result_frm.winfo_children(): widget.destroy()
            ad1, ad2 = cmb1.get(), cmb2.get()
            if not ad1 or not ad2:
                messagebox.showwarning("Eksik", "Lütfen iki okul seçiniz!", parent=win)
                return
            
            o1 = self.motor.get_okul_by_name(ad1)
            o2 = self.motor.get_okul_by_name(ad2)
            
            tk.Label(result_frm, text="", bg="white", width=20).grid(row=0, column=0)
            tk.Label(result_frm, text=o1.get_ad(), font=("Segoe UI", 11, "bold"), bg="#3498db", fg="white", width=40, wraplength=300, height=3).grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
            tk.Label(result_frm, text=o2.get_ad(), font=("Segoe UI", 11, "bold"), bg="#e74c3c", fg="white", width=40, wraplength=300, height=3).grid(row=0, column=2, padx=2, pady=2, sticky="nsew")
            
            parametreler = [
                ("İlçe", o1.get_ilce(), o2.get_ilce()),
                ("LGS Puanı", o1.get_puan(), o2.get_puan()),
                ("Yüzdelik Dilim", f"%{o1.get_yuzdelik()}", f"%{o2.get_yuzdelik()}")
            ]
            
            row = 1
            for baslik, d1, d2 in parametreler:
                tk.Label(result_frm, text=baslik, font=("Segoe UI", 10, "bold"), bg="#ecf0f1", anchor="e", padx=10).grid(row=row, column=0, sticky="ew", pady=1)
                tk.Label(result_frm, text=d1, font=("Segoe UI", 10), bg="white").grid(row=row, column=1, sticky="nsew", pady=1)
                tk.Label(result_frm, text=d2, font=("Segoe UI", 10), bg="white").grid(row=row, column=2, sticky="nsew", pady=1)
                row += 1
            
            tk.Label(result_frm, text="İMKANLAR", font=("Segoe UI", 10, "bold"), bg="#2c3e50", fg="white").grid(row=row, column=0, columnspan=3, sticky="ew", pady=10)
            row += 1
            
            oz1 = o1.tum_ozellikleri_getir()
            oz2 = o2.tum_ozellikleri_getir()
            
            for k in oz1.keys():
                tk.Label(result_frm, text=k, font=("Segoe UI", 10), bg="#ecf0f1", anchor="e", padx=10).grid(row=row, column=0, sticky="ew", pady=1)
                ikon1, renk1 = ("✅ VAR", "#27ae60") if oz1[k] else ("❌ YOK", "#c0392b")
                tk.Label(result_frm, text=ikon1, font=("Segoe UI", 10, "bold"), fg=renk1, bg="white").grid(row=row, column=1, sticky="nsew", pady=1)
                ikon2, renk2 = ("✅ VAR", "#27ae60") if oz2[k] else ("❌ YOK", "#c0392b")
                tk.Label(result_frm, text=ikon2, font=("Segoe UI", 10, "bold"), fg=renk2, bg="white").grid(row=row, column=2, sticky="nsew", pady=1)
                row += 1
            result_frm.grid_columnconfigure(1, weight=1)
            result_frm.grid_columnconfigure(2, weight=1)

        tk.Button(select_frm, text="🔎 KIYASLA", command=kiyasla, bg="#27ae60", fg="white", font=("Segoe UI", 10, "bold")).pack(side="left", padx=20)

    def sifirla(self):
        self.ent_yuzdelik.delete(0, tk.END)
        self.cmb_ilce.current(0)
        for i in self.tree_kazan.get_children(): self.tree_kazan.delete(i)
        for i in self.tree_hedef.get_children(): self.tree_hedef.delete(i)
        self.status_var.set("Temizlendi.")

    def hakkinda_goster(self):
        messagebox.showinfo("Hakkında", "Lise Tercih Karar Destek Sistemi")

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()