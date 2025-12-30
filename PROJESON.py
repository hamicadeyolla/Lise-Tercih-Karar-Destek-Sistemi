import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime
import os
import webbrowser 
import csv  # Verileri Excel formatında dışarı aktarmak için gerekli

# --- 1. KÜTÜPHANE VE MODÜL KONTROLLERİ ---
# Programın çalışması için gerekli harici kütüphanelerin kontrolü.
try:
    from fpdf import FPDF
except ImportError:
    messagebox.showerror("Eksik Kütüphane", "PDF özelliği için 'fpdf' kütüphanesi gerekli.\nLütfen terminale 'pip install fpdf' yazarak kurun.")

# Grafik Kütüphanesi Kontrolü (Matplotlib)
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    MATPLOTLIB_VAR = True
except ImportError:
    MATPLOTLIB_VAR = False # Grafik özelliği devre dışı bırakılır.

# Veri Entegrasyonu (Modüler Yapı)
# Veriler 'data.py' dosyasından çekilir.
try:
    from data import OKUL_VERITABANI
except ImportError:
        messagebox.showerror("Kritik Hata", "data.py dosyası bulunamadı!\nLütfen aynı klasörde olduğundan emin olun.")
        OKUL_VERITABANI = []

# --- 2. MODEL KATMANI (OOP: Encapsulation - Kapsülleme) ---
class School:
    """
    Bu sınıf tek bir okulu temsil eden veri modelidir.
    OOP Prensibi: ENCAPSULATION (Kapsülleme) - Veriler gizlenir, metodlarla erişilir.
    """
    def __init__(self, veri):
        self.__ad = veri["ad"]
        self.__puan = veri["puan"]
        self.__yuzdelik = veri["yuzdelik"]
        self.__ilce = veri.get("ilce", "Belirtilmemiş") 
        
        self.__ozellikler = {
            "Spor Salonu": veri["spor"],
            "Yemekhane": veri["yemek"],
            "Konferans Salonu": veri["konferans"],
            "Bilgisayar Lab.": veri["bilg_lab"],
            "Fen Laboratuvarı": veri["fen_lab"],
            "Kantin": veri["kantin"]
        }
        self.eksik_ozellikler = [] 

    # --- GETTER METODLARI ---
    def get_ad(self): return self.__ad
    def get_puan(self): return self.__puan
    def get_yuzdelik(self): return self.__yuzdelik
    def get_ilce(self): return self.__ilce
    
    def ozellik_var_mi(self, ozellik):
        return self.__ozellikler.get(ozellik, False)
    
    def eksik_ekle(self, ozellik):
        self.eksik_ozellikler.append(ozellik)
        
    def eksikleri_temizle(self):
        self.eksik_ozellikler = []
        
    def get_eksikler(self):
        return self.eksik_ozellikler
    
    def tum_ozellikleri_getir(self):
        return self.__ozellikler

# --- 3. CONTROLLER KATMANI (Mantık ve Hesaplama Motoru) ---
class DecisionEngine:
    """
    Karar Motoru: Filtreleme, analiz ve sıralama işlemlerini yönetir.
    """
    def __init__(self):
        self.okullar = [School(veri) for veri in OKUL_VERITABANI]
        self.okul_isimleri = sorted([o.get_ad() for o in self.okullar])

    def detayli_analiz(self, kriterler, ogr_yuzdelik, secilen_ilce="Tümü"):
        """
        ANA ALGORİTMA: İlçe Filtresi -> Özellik Kontrolü -> Puan Karşılaştırma
        """
        kazanilanlar = []
        hedefler = []
        
        for okul in self.okullar:
            # 1. Aşama: İlçe Filtresi
            if secilen_ilce != "Tümü" and okul.get_ilce() != secilen_ilce:
                continue 

            # 2. Aşama: Özellik Kontrolü
            # BURASI ÖNEMLİ: Her analizde önce eski eksikler temizlenir.
            okul.eksikleri_temizle()
            for kriter in kriterler:
                if not okul.ozellik_var_mi(kriter):
                    okul.eksik_ekle(kriter)
            
            # 3. Aşama: Yüzdelik Dilim Karşılaştırma
            okul_yuzdelik = okul.get_yuzdelik()
            
            if ogr_yuzdelik <= okul_yuzdelik:
                kazanilanlar.append(okul)
            elif (ogr_yuzdelik - okul_yuzdelik) < 1.5:
                hedefler.append(okul)
                
        # Sıralama: En iyi yüzdelikten en kötüye
        kazanilanlar.sort(key=lambda x: x.get_yuzdelik())
        hedefler.sort(key=lambda x: x.get_yuzdelik())
        
        return kazanilanlar, hedefler
    
    def get_tum_ilceler(self):
        ilceler = set()
        for okul in self.okullar:
            ilceler.add(okul.get_ilce())
        liste = list(ilceler)
        liste.sort()
        return ["Tümü"] + liste
    
    def get_okul_by_name(self, ad):
        for o in self.okullar:
            if o.get_ad() == ad:
                return o
        return None

# --- 4. RAPORLAMA KATMANI (OOP: Inheritance - Kalıtım) ---
class PDFReport(FPDF):
    """
    FPDF sınıfından kalıtım alınarak oluşturulan özelleştirilmiş rapor sınıfı.
    """
    def header(self):
        try:
            self.add_font('ArialTR', '', r'C:\Windows\Fonts\arial.ttf', uni=True)
            self.add_font('ArialTR', 'B', r'C:\Windows\Fonts\arialbd.ttf', uni=True)
            self.set_font('ArialTR', 'B', 15)
        except:
            self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'LİSE TERCİH DANIŞMANLIĞI RAPORU', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        try:
            self.set_font('ArialTR', '', 8)
        except:
            self.set_font('Arial', '', 8)
        self.cell(0, 10, f'Sayfa {self.page_no()}', 0, 0, 'C')

# --- 5. VIEW KATMANI (GUI - Kullanıcı Arayüzü) ---
class DashboardApp(tk.Tk):
    """
    Uygulamanın Görsel Yüzü. Tkinter ile oluşturulmuştur.
    """
    def __init__(self):
        super().__init__()
        self.title("Lise Tercih Karar Destek Sistemi")
        self.geometry("1300x800")
        self.configure(bg="#ecf0f1")
        
        # Controller bağlantısı
        self.motor = DecisionEngine()
        
        # Analiz sonuçlarını saklama değişkenleri
        self.son_kazanilanlar = []
        self.son_hedefler = []
        
        # Status Bar değişkeni (Görünürde yok ama kod hatası vermesin diye arkada çalışır)
        self.status_var = tk.StringVar(value="Sistem Hazır.")
        
        # Arayüz Bileşenleri
        self.stil_ayarla()
        self.menuyu_olustur()
        self.ana_cerceveleri_olustur()
        self.sidebar_doldur()
        self.icerik_doldur()

    def stil_ayarla(self):
        """Görsel stil ayarları."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", foreground="black", rowheight=30, fieldbackground="white", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#34495e", foreground="white", font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[('selected', '#3498db')])

    def menuyu_olustur(self):
        """Üst menü barı."""
        menubar = tk.Menu(self)
        dosya = tk.Menu(menubar, tearoff=0)
        dosya.add_command(label="Yenile / Temizle", command=self.sifirla)
        dosya.add_separator()
        dosya.add_command(label="PDF Rapor Al", command=self.rapor_al_pdf)
        dosya.add_command(label="Excel (CSV) Aktar", command=self.excel_aktar)
        dosya.add_separator()
        dosya.add_command(label="Çıkış", command=self.quit)
        menubar.add_cascade(label="Dosya", menu=dosya)
        
        yardim = tk.Menu(menubar, tearoff=0)
        yardim.add_command(label="Hakkında", command=self.hakkinda_goster)
        menubar.add_cascade(label="Yardım", menu=yardim)
        self.config(menu=menubar)

    def ana_cerceveleri_olustur(self):
        """Sol ve Sağ ana paneller."""
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=300)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        self.main_area = tk.Frame(self, bg="#ecf0f1")
        self.main_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def sidebar_doldur(self):
        """Sol panel içeriği."""
        tk.Label(self.sidebar, text="🎓 OKUL\nASİSTANI", bg="#2c3e50", fg="#f1c40f", font=("Segoe UI", 24, "bold")).pack(pady=20)
        
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
        for k in ["Spor Salonu", "Yemekhane", "Konferans Salonu", "Bilgisayar Lab.", "Fen Laboratuvarı", "Kantin"]:
            var = tk.BooleanVar()
            tk.Checkbutton(frm2, text=k, variable=var, bg="#2c3e50", fg="white", selectcolor="#2c3e50", activebackground="#2c3e50", anchor="w").pack(fill="x", padx=5)
            self.vars[k] = var

        tk.Button(self.sidebar, text="🚀 ANALİZİ BAŞLAT", command=self.hesapla, bg="#e74c3c", fg="white", font=("Segoe UI", 12, "bold"), pady=10).pack(fill="x", padx=15, pady=10)
        
        tk.Button(self.sidebar, text="📊 Yüzdelik Grafiği", command=self.grafik_goster, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="💾 Excel'e Kaydet", command=self.excel_aktar, bg="#16a085", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        
        tk.Label(self.sidebar, text="Araçlar", bg="#2c3e50", fg="#95a5a6", font=("Segoe UI", 10, "underline")).pack(pady=(15,5))
        
        tk.Button(self.sidebar, text="🆚 Okulları Karşılaştır", command=self.karsilastirma_modulu_ac, bg="#9b59b6", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="📄 PDF Rapor Oluştur", command=self.rapor_al_pdf, bg="#e67e22", fg="white", font=("Segoe UI", 10, "bold"), pady=5).pack(fill="x", padx=15, pady=2)
        tk.Button(self.sidebar, text="📚 Tüm Okul Listesini Gör", command=self.tum_okullari_ac, bg="#34495e", fg="white", font=("Segoe UI", 10), pady=5).pack(side="bottom", fill="x", padx=15, pady=20)

    def icerik_doldur(self):
        """
        GRID sistemi ile iki tabloyu ekrana eşit (%50-%50) paylaştırma.
        """
        tk.Label(self.main_area, text="Analiz Sonuçları (Detay için okula çift tıklayın)", bg="#ecf0f1", fg="#2c3e50", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 10))
        
        table_frame = tk.Frame(self.main_area, bg="#ecf0f1")
        table_frame.pack(fill="both", expand=True)
        
        # Grid ayarları: İki sütuna da eşit ağırlık (weight=1) vererek tam ortadan bölüyoruz.
        table_frame.grid_columnconfigure(0, weight=1, uniform="group1")
        table_frame.grid_columnconfigure(1, weight=1, uniform="group1")
        table_frame.grid_rowconfigure(0, weight=1)

        # 1. Tablo (SOL)
        frm1 = tk.LabelFrame(table_frame, text="🎯 Hedef Tercihler", bg="white", fg="#e67e22", font=("Segoe UI", 11, "bold"))
        frm1.grid(row=0, column=0, sticky="nsew", padx=(0, 5)) 
        self.tree_hedef = self.tablo_yarat(frm1)

        # 2. Tablo (SAĞ)
        frm2 = tk.LabelFrame(table_frame, text="✅ Güvenli Tercihler", bg="white", fg="#27ae60", font=("Segoe UI", 11, "bold"))
        frm2.grid(row=0, column=1, sticky="nsew", padx=(5, 0)) 
        self.tree_kazan = self.tablo_yarat(frm2)
        
        self.tree_hedef.bind("<Double-1>", self.okul_detay_ac)
        self.tree_kazan.bind("<Double-1>", self.okul_detay_ac)

    def tablo_yarat(self, parent):
        """Treeview oluşturma fonksiyonu."""
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
        """Analiz fonksiyonu. Hata durumunda False döner."""
        try:
            val = self.ent_yuzdelik.get().replace(",", ".")
            yuzdelik = float(val)
        except ValueError:
            messagebox.showwarning("Hata", "Geçerli bir yüzdelik girin!")
            return False
        
        secimler = [k for k, v in self.vars.items() if v.get()]
        secilen_ilce = self.cmb_ilce.get()
        
        k, h = self.motor.detayli_analiz(secimler, yuzdelik, secilen_ilce)
        
        self.son_kazanilanlar = k
        self.son_hedefler = h
        
        self.doldur(self.tree_kazan, k)
        self.doldur(self.tree_hedef, h, is_hedef=True)
        self.status_var.set(f"Analiz Tamamlandı: {len(k)} güvenli, {len(h)} hedef okul bulundu.")
        return True

    def doldur(self, tree, liste, is_hedef=False):
        """Tabloyu doldurma fonksiyonu."""
        for i in tree.get_children(): tree.delete(i)
        for okul in liste:
            eksikler = okul.get_eksikler()
            # Eğer kullanıcı özellik seçmediyse 'eksikler' boştur, bu yüzden 'Tam Uygun' yazar.
            tag = 'riskli' if is_hedef and not eksikler else ('eksik_var' if eksikler else 'tam_uyumlu')
            notu = f"⚠️ Eksik: {', '.join(eksikler)}" if eksikler else "✔️ Tam Uygun"
            tree.insert("", "end", values=(okul.get_ad(), okul.get_ilce(), f"%{okul.get_yuzdelik()}", notu), tags=(tag,))

    def grafik_goster(self):
        """Grafik görselleştirme fonksiyonu."""
        if not MATPLOTLIB_VAR:
            messagebox.showerror("Kütüphane Eksik", "Grafik için 'matplotlib' gerekli.")
            return
        if not self.son_kazanilanlar and not self.son_hedefler:
            messagebox.showwarning("Veri Yok", "Önce bir analiz yapmalısınız!")
            return
        
        tum_liste = self.son_kazanilanlar + self.son_hedefler
        tum_liste.sort(key=lambda x: x.get_yuzdelik(), reverse=True) 
        ilk_15_okul = tum_liste[-15:] 
        
        isimler = [okul.get_ad() for okul in ilk_15_okul]
        yuzdelikler = [okul.get_yuzdelik() for okul in ilk_15_okul]
        eksikler_listesi = [okul.get_eksikler() for okul in ilk_15_okul]
        
        renkler = ['#e67e22' if e else '#27ae60' for e in eksikler_listesi]

        win = tk.Toplevel(self)
        win.title(f"Detaylı Yüzdelik ve Kriter Analizi")
        win.geometry("1100x700")
        
        fig, ax = plt.subplots(figsize=(12, 7), dpi=100)
        bars = ax.barh(isimler, yuzdelikler, color=renkler)
        
        ax.set_xlabel('Yüzdelik Dilim (Kısa Bar = Daha İyi Derece)')
        ax.set_title('Okul Yüzdelik Dilimleri ve Kriter Uygunluk Durumu')
        if yuzdelikler: ax.set_xlim(0, max(yuzdelikler) + 2.0)
        
        for bar, yuzde, eksik_listesi in zip(bars, yuzdelikler, eksikler_listesi):
            width = bar.get_width()
            if not eksik_listesi:
                etiket = f"%{yuzde:.2f} (Tam Uyumlu) ✅"
                yazi_rengi = '#145a32'
            else:
                eksik_str = ", ".join(eksik_listesi)
                etiket = f"%{yuzde:.2f} (Eksik: {eksik_str}) ⚠️"
                yazi_rengi = '#c0392b'
            
            ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, etiket, 
                    ha='left', va='center', fontsize=9, fontweight='bold', color=yazi_rengi)
        
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def excel_aktar(self):
        """Excel (CSV) çıktı alma fonksiyonu."""
        if not self.son_kazanilanlar and not self.son_hedefler:
            messagebox.showwarning("Uyarı", "Dışa aktarılacak veri yok!")
            return

        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                filetypes=[("Excel CSV Dosyası", "*.csv")],
                                                title="Verileri Kaydet")
        if not dosya_yolu: return

        try:
            with open(dosya_yolu, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';') 
                writer.writerow(["Okul Adı", "İlçe", "Puan", "Yüzdelik", "Durum", "Eksik Özellikler"])
                tum_liste = self.son_hedefler + self.son_kazanilanlar
                for okul in tum_liste:
                    durum = "Hedef" if okul in self.son_hedefler else "Güvenli"
                    eksikler = ", ".join(okul.get_eksikler()) if okul.get_eksikler() else "Tam Uygun"
                    writer.writerow([
                        okul.get_ad(), okul.get_ilce(), 
                        str(okul.get_puan()).replace('.', ','), 
                        str(okul.get_yuzdelik()).replace('.', ','),
                        durum, eksikler
                    ])
            messagebox.showinfo("Başarılı", "Veriler başarıyla kaydedildi!\nDosyayı Excel ile açabilirsiniz.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken hata oluştu:\n{e}")

    def karsilastirma_modulu_ac(self):
        """Karşılaştırma ekranı."""
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

    def rapor_al_pdf(self):
        """
        GÜNCELLEME: PDF Raporu artık eksik kriter listesi yerine,
        sadece okulları yüzdelik dilim durumuna göre iki ana kategoride listeler.
        """
        # 1. Önce analizi tazeleyelim.
        basarili = self.hesapla()
        if not basarili:
            return 

        # 2. Veri kontrolü
        if not self.tree_kazan.get_children() and not self.tree_hedef.get_children():
            messagebox.showwarning("Uyarı", "Kriterlere uygun okul bulunamadı.")
            return

        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Dosyası", "*.pdf")], title="PDF Raporu Kaydet")
        if not dosya_yolu: return
        try:
            pdf = PDFReport()
            pdf.add_page()
            try:
                pdf.add_font('ArialTR', '', r'C:\Windows\Fonts\arial.ttf', uni=True)
                pdf.set_font('ArialTR', '', 11)
            except:
                pdf.set_font('Arial', '', 11)
            
            # --- BAŞLIK BÖLÜMÜ ---
            pdf.set_font('', 'B', 12)
            pdf.cell(0, 10, f"Rapor Tarihi: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}", 0, 1)
            pdf.cell(0, 10, f"Ogrenci Yuzdelik Dilimi: %{self.ent_yuzdelik.get()}", 0, 1)
            pdf.cell(0, 10, f"Tercih Edilen Ilce: {self.cmb_ilce.get()}", 0, 1)
            
            # Seçilen kriterler bilgi olarak kalsın ama okul listesinde detay yazmayacağız.
            secilenler = [k for k, v in self.vars.items() if v.get()]
            kriter_str = ', '.join(secilenler) if secilenler else 'Belirtilmedi'
            pdf.multi_cell(0, 10, f"Filtrelenen Kriterler: {kriter_str}")
            pdf.ln(5)
            
            # --- BÖLÜM 1: HEDEF / RİSKLİ TERCİHLER ---
            pdf.set_fill_color(230, 126, 34) # Turuncu Başlık
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, " HEDEF TERCİHLER (PUANINIZIN YETMEDİĞİ / ZORLANABİLİR)", 0, 1, 'L', 1)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('', '', 10)
            
            if not self.tree_hedef.get_children():
                pdf.cell(0, 8, " - Bu kategoride okul bulunamadi.", 0, 1)
            else:
                for item in self.tree_hedef.get_children():
                    vals = self.tree_hedef.item(item)['values']
                    # Vals[0]=Okul Adı, Vals[1]=İlçe, Vals[2]=Yüzdelik, Vals[3]=Eksik Listesi (Bunu yazdırmıyoruz)
                    pdf.cell(10)
                    pdf.cell(0, 8, f"- {vals[0]} ({vals[1]}) - Yuzdelik: {vals[2]}", 0, 1)
            pdf.ln(5)
            
            # --- BÖLÜM 2: GÜVENLİ / KAZANILAN TERCİHLER ---
            pdf.set_font('', 'B', 12)
            pdf.set_fill_color(39, 174, 96) # Yeşil Başlık
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, " GUVENLİ TERCİHLER (PUANINIZIN YETTİĞİ)", 0, 1, 'L', 1)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('', '', 10)
            
            if not self.tree_kazan.get_children():
                pdf.cell(0, 8, " - Bu kategoride okul bulunamadi.", 0, 1)
            else:
                for item in self.tree_kazan.get_children():
                    vals = self.tree_kazan.item(item)['values']
                    pdf.cell(10)
                    pdf.cell(0, 8, f"- {vals[0]} ({vals[1]}) - Yuzdelik: {vals[2]}", 0, 1)
            
            pdf.output(dosya_yolu)
            messagebox.showinfo("Başarılı", "PDF Raporu başarıyla oluşturuldu!")
        except Exception as e:
            messagebox.showerror("Hata", f"PDF oluşturulurken hata: {e}")

    def tum_okullari_ac(self):
        """Tüm okulları ve tüm kriterleri listeleme penceresi."""
        top = tk.Toplevel(self)
        top.title("Tüm Veritabanı ve Detaylı İmkanlar")
        # Tüm sütunların sığması için genişliği artırdım
        top.geometry("1350x600") 
        top.attributes('-topmost', 'true')
        
        tk.Label(top, text="Tüm Ankara Liseleri ve İmkan Listesi", font=("Segoe UI", 12, "bold")).pack(pady=5)
        
        container = tk.Frame(top)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sütun Başlıkları (Kısa tutuldu sığması için)
        cols = ("Okul", "İlçe", "Puan", "Yüzde", "Spor", "Yemek", "Konf.", "PC Lab", "Fen Lab", "Kantin")
        
        tree = ttk.Treeview(container, columns=cols, show="headings")
        
        # Sütun Genişlik Ayarları
        tree.column("Okul", width=300, minwidth=200) # Okul adı uzun olabilir
        tree.column("İlçe", width=90, anchor="center")
        tree.column("Puan", width=60, anchor="center")
        tree.column("Yüzde", width=60, anchor="center")
        
        # Geri kalan özellik sütunlarının hepsi standart genişlikte
        for col in cols[4:]:
            tree.column(col, width=70, anchor="center")
            
        # Başlıkları Yazdır
        for c in cols: 
            tree.heading(c, text=c)
            
        yscroll = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        xscroll = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscroll=yscroll.set, xscroll=xscroll.set)
        
        tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        tree.bind("<Double-1>", self.okul_detay_ac) 
        
        # Verileri Doldurma Döngüsü
        for okul in self.motor.okullar:
            oz = okul.tum_ozellikleri_getir()
            
            # Veritabanındaki "Spor Salonu" anahtarı ile tablodaki yerini eşleştiriyoruz
            # True ise "Var", False ise "-" yazdırıyoruz daha temiz görünüm için.
            tree.insert("", "end", values=(
                okul.get_ad(),
                okul.get_ilce(),
                str(okul.get_puan()).replace(".", ","), # Puanı TR formatı yap
                f"%{okul.get_yuzdelik()}",
                "Var" if oz["Spor Salonu"] else "-",
                "Var" if oz["Yemekhane"] else "-",
                "Var" if oz["Konferans Salonu"] else "-",
                "Var" if oz["Bilgisayar Lab."] else "-",
                "Var" if oz["Fen Laboratuvarı"] else "-",
                "Var" if oz["Kantin"] else "-"
            ))

    def okul_detay_ac(self, event):
        """Okul detay kartı."""
        tree = event.widget
        sel = tree.selection()
        if not sel: return
        item = tree.item(sel)
        if not item['values']: return 
        okul_adi = item['values'][0]
        
        secili_okul = next((o for o in self.motor.okullar if str(o.get_ad()) == str(okul_adi)), None)
        
        if secili_okul:
            win = tk.Toplevel(self)
            win.title("Okul Kartı")
            win.geometry("600x550")
            win.configure(bg="white")
            win.attributes('-topmost', 'true')
            
            tk.Button(win, text="X", command=win.destroy, bg="#e74c3c", fg="white", font=("Arial",12,"bold"), bd=0).pack(anchor="ne", padx=10, pady=5)
            tk.Label(win, text=secili_okul.get_ad(), font=("Segoe UI", 16, "bold"), bg="white", fg="#2c3e50", wraplength=550).pack()
            tk.Label(win, text=f"📍 {secili_okul.get_ilce()}", font=("Segoe UI", 12), bg="white", fg="#7f8c8d").pack()
            
            def haritada_ac():
                adres = f"{secili_okul.get_ad()} {secili_okul.get_ilce()} Ankara"
                url = f"https://www.google.com/maps/search/?api=1&query={adres.replace(' ', '+')}"
                webbrowser.open(url)
            
            tk.Button(win, text="🗺️ Haritada Göster", command=haritada_ac, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=5)
            
            frm = tk.Frame(win, bg="#ecf0f1", pady=10)
            frm.pack(fill="x", padx=20, pady=10)
            tk.Label(frm, text=f"LGS: {secili_okul.get_puan()}", font=("Segoe UI",12,"bold"), bg="#2980b9").pack(side="left", padx=20)
            tk.Label(frm, text=f"Dilim: %{secili_okul.get_yuzdelik()}", font=("Segoe UI",12,"bold"), fg="#e67e22").pack(side="right", padx=20)
            
            tk.Label(win, text="İmkanlar", font=("Segoe UI",11,"underline"), bg="white", fg="#95a5a6").pack(pady=5)
            g_frm = tk.Frame(win, bg="white")
            g_frm.pack()
            
            r, c = 0, 0
            for ozellik, var_mi in secili_okul.tum_ozellikleri_getir().items():
                ikon, renk, bg = ("✅", "#27ae60", "#e8f8f5") if var_mi else ("❌", "#c0392b", "#fdedec")
                tk.Label(g_frm, text=f"{ikon} {ozellik}", font=("Segoe UI",10,"bold"), fg=renk, bg=bg, width=22, height=2, relief="groove").grid(row=r, column=c, padx=5, pady=5)
                c += 1
                if c > 1: c=0; r+=1

    # def status_bar_olustur(self):
        # ... (Bu fonksiyon iptal edildi)

    def sifirla(self):
        """Sıfırlama fonksiyonu."""
        self.ent_yuzdelik.delete(0, tk.END)
        self.cmb_ilce.current(0)
        for i in self.tree_kazan.get_children(): self.tree_kazan.delete(i)
        for i in self.tree_hedef.get_children(): self.tree_hedef.delete(i)
        self.status_var.set("Temizlendi.")

    def hakkinda_goster(self):
        """Hakkında."""
        messagebox.showinfo("Hakkında", "Lise Tercih Karar Destek Sistemi v13.0\nHamza Osman Erdoğan")

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()