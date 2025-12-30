# Lise Tercih Karar Destek Sistemi (LGS Assistant)

Bu proje, **Nesne Yönelimli Programlama (OOP)** dersi final ödevi kapsamında geliştirilmiş bir karar destek yazılımıdır. LGS sınavına giren öğrencilerin yüzdelik dilimlerine ve sosyal imkan beklentilerine (spor salonu, yemekhane vb.) en uygun liseleri analiz eder, listeler ve raporlar.

## 🚀 Proje Özellikleri

* **Detaylı Filtreleme:** İlçe ve okul imkanlarına (Yemekhane, Konferans Salonu, Lab vb.) göre akıllı filtreleme.
* **Karar Destek Motoru:** Öğrencinin yüzdelik dilimine göre "Güvenli Tercih" ve "Hedef Tercih" sınıflandırması.
* **Görselleştirme:** Matplotlib kütüphanesi ile başarı durumu ve kriter uygunluk grafikleri.
* **Raporlama:** Kişiye özel PDF formatında tercih danışmanlığı raporu çıktısı.
* **Veri Karşılaştırma:** İki farklı okulun teknik ve sosyal imkanlarının yan yana kıyaslanması.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

* **Dil:** Python 3.x
* **Arayüz (GUI):** Tkinter
* **Veri Görselleştirme:** Matplotlib
* **Raporlama:** FPDF
* **Veri Yönetimi:** CSV, Custom Data Module

## 🏗 Mimari Yapı (OOP & MVC)

Proje, **Model-View-Controller (MVC)** yapısına benzer modüler bir mimari ile geliştirilmiştir:

1.  **Model (`School` Class):** Veri kapsülleme (Encapsulation) prensibi ile okul verileri güvenli bir şekilde yönetilir. Veriler `data.py` dosyasından çekilir.
2.  **View (`DashboardApp` Class):** Tkinter ile oluşturulan kullanıcı arayüzü. Kalıtım (Inheritance) yoluyla `tk.Tk` sınıfından türetilmiştir.
3.  **Controller (`DecisionEngine` Class):** Analiz, sıralama ve filtreleme algoritmalarının çalıştığı mantık katmanıdır.

## 📦 Kurulum ve Çalıştırma

1.  Projeyi bilgisayarınıza indirin veya klonlayın:
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/Lise-Tercih-Karar-Destek-Sistemi.git](https://github.com/KULLANICI_ADINIZ/Lise-Tercih-Karar-Destek-Sistemi.git)
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install fpdf matplotlib
    ```
3.  Uygulamayı başlatın:
    ```bash
    python PROJESON.py
    ```

## 📝 Hazırlayan
**Hamza Osman Erdoğan**
Ankara Üniversitesi - Bilgisayar ve Öğretim Teknolojileri Öğretmenliği
