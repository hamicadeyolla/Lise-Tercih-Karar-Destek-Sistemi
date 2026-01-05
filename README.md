# 🎓 Lise Tercih Karar Destek Sistemi (High School Decision Support System)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Completed-success)

**[TR]** Bu proje, Ankara Üniversitesi **BOZ213 Nesne Tabanlı Programlama** dersi final ödevi kapsamında geliştirilmiştir. Lise tercihi yapacak öğrenciler için akademik başarı (Yüzdelik Dilim) ve çevresel güvenlik/imkan analizini birleştiren akıllı bir karar destek sistemidir.

**[EN]** This project was developed as a final assignment for the **BOZ213 Object-Oriented Programming** course at Ankara University. It is an intelligent decision support system for high school students, combining academic success metrics with environmental safety and facility analysis.

---

## 🚀 Özellikler / Features

### 🇹🇷 Türkçe
* **Google Maps API Entegrasyonu:** Okulların çevresindeki "Kafe, Bar, Oyun Salonu" yoğunluğunu ve "Metro, Polis, Hastane" yakınlığını analiz eder.
* **Akıllı Filtreleme:** Öğrencinin yüzdelik dilimine ve ilçe tercihine göre "Hedef" ve "Güvenli" okulları listeler.
* **OOP Mimarisi:** Kapsülleme (Encapsulation), Soyutlama (Abstraction) ve Kalıtım (Inheritance) prensipleriyle modüler yapı.
* **Raporlama:** Analiz sonuçlarını **PDF** ve **Excel (CSV)** formatında dışa aktarır.
* **Görsel Arayüz (GUI):** Kullanıcı dostu Tkinter arayüzü.

### 🇬🇧 English
* **Google Maps API Integration:** Analyzes environmental factors (Cafes, Bars, Transport, Safety) around schools using real-time geolocation data.
* **Smart Filtering:** Lists "Target" and "Safe" schools based on the student's percentile and district preference.
* **OOP Architecture:** Modular design using Encapsulation, Abstraction, and Inheritance principles.
* **Reporting:** Exports analysis results to **PDF** and **Excel (CSV)** formats.
* **GUI:** User-friendly interface built with Tkinter.

---

## 🛠️ Kurulum / Installation

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:
Follow these steps to run the project locally:

1.  **Depoyu Klonlayın / Clone the Repository:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/REPO_ISMI.git](https://github.com/KULLANICI_ADIN/REPO_ISMI.git)
    cd REPO_ISMI
    ```

2.  **Gerekli Kütüphaneleri Yükleyin / Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Anahtarı Ayarı / API Key Setup:**
    * Proje ana dizininde `.env` adında bir dosya oluşturun. / Create a `.env` file in the root directory.
    * İçine Google Maps API anahtarınızı ekleyin: / Add your Google Maps API key:
    ```env
    GOOGLE_API_KEY=AIzaSy... (Senin Keyin)
    ```

4.  **Çalıştırma / Run:**
    ```bash
    python PROJESON.py
    ```

---

## 📂 Proje Yapısı / Project Structure

* `PROJESON.py`: Ana uygulama ve GUI (Main application).
* `data.py`: Okul veritabanı ve koordinat bilgileri (School database).
* `requirements.txt`: Kütüphane gereksinimleri (Dependencies).
* `.env`: (Gizli) API anahtarını saklar / Stores API key securely.

---

## 👥 Ekip / Team
* **Ad Soyad:** Hamza Osman Erdoğan
* **Bölüm:** Bilgisayar ve Öğretim Teknolojileri Eğitimi (BÖTE)
* **Ders:** Nesne Tabanlı Programlama (BOZ213)
