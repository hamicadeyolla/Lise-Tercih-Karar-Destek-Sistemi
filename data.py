# data.py

OKUL_VERITABANI = [
    # =============================================================================
    # 1. GRUP: %0 - %1 LİK DİLİM (Türkiye Derecesi)
    # =============================================================================

    # Ankara Fen Lisesi (Çiğdem Mah. / ODTÜ Ormanı Yanı)
    {'ad': 'Ankara Fen Lisesi', 'ilce': 'Çankaya', 'puan': 494.5096, 'yuzdelik': 0.08, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8772, 'lon': 32.8069},

    # Prof. Dr. Aziz Sancar Fen Lisesi (Ahlatlıbel / İncek Yolu)
    {'ad': 'Prof. Dr. Aziz Sancar Fen Lisesi', 'ilce': 'Çankaya', 'puan': 493.8037, 'yuzdelik': 0.21, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8510, 'lon': 32.7850},

    # Ankara Pursaklar Fen Lisesi (Pursaklar Merkez)
    {'ad': 'Ankara Pursaklar Fen Lisesi', 'ilce': 'Pursaklar', 'puan': 489.0189, 'yuzdelik': 0.31, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0385, 'lon': 32.8945},

    # Ankara Erman Ilıcak Fen Lisesi (Sincan / Fatih)
    {'ad': 'Ankara Erman Ilıcak Fen Lisesi', 'ilce': 'Sincan', 'puan': 481.8925, 'yuzdelik': 0.77, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9678, 'lon': 32.5856},

    # Atatürk Anadolu Lisesi (AAAL) (Beştepe / Cumhurbaşkanlığı Külliyesi Karşısı)
    {'ad': 'Atatürk Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 481.7319, 'yuzdelik': 0.79, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9220, 'lon': 32.8115},

    # Özdemir Bayraktar Havacılık ve Uzay Teknolojileri MTAL (Sincan)
    {'ad': 'Özdemir Bayraktar Havacılık ve Uzay Teknolojileri MTAL', 'ilce': 'Sincan', 'puan': 480.2425, 'yuzdelik': 0.96, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9715, 'lon': 32.5590},

    # =============================================================================
    # 2. GRUP: %1 - %3 LİK DİLİM
    # =============================================================================

    # Cumhuriyet Fen Lisesi (Bahçelievler / Emek)
    {'ad': 'Cumhuriyet Fen Lisesi', 'ilce': 'Çankaya', 'puan': 477.3322, 'yuzdelik': 1.09, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9165, 'lon': 32.8220},

    # Keçiören Vatansever Şehit Tümgeneral Aydoğan Aydın Fen Lisesi (Ovacık)
    {'ad': 'Keçiören Vatansever Şehit Tümgeneral Aydoğan Aydın Fen Lisesi', 'ilce': 'Keçiören', 'puan': 476.4021, 'yuzdelik': 1.31, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0155, 'lon': 32.8455},

    # Yenimahalle Fen Lisesi (İvedik / Demetevler)
    {'ad': 'Yenimahalle Fen Lisesi', 'ilce': 'Yenimahalle', 'puan': 474.6942, 'yuzdelik': 1.52, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9572, 'lon': 32.7910},

    # Özkent Akbilek Fen Lisesi (Eryaman)
    {'ad': 'Özkent Akbilek Fen Lisesi', 'ilce': 'Etimesgut', 'puan': 470.7507, 'yuzdelik': 1.9, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9755, 'lon': 32.6215},

    # ASELSAN Mesleki ve Teknik Anadolu Lisesi (Yenimahalle / Yeni Batı - Mesa Metro Yanı)
    # DÜZELTİLDİ: Artık Macunköy (Fabrika) değil, Mesa Metro (Okul) konumunda.
    {'ad': 'ASELSAN Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 470.5631, 'yuzdelik': 1.95, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9678, 'lon': 32.7027},

    # Ankara Atatürk Lisesi (Sıhhiye / Tarihi Taş Bina)
    {'ad': 'Ankara Atatürk Lisesi', 'ilce': 'Çankaya', 'puan': 467.2796, 'yuzdelik': 2.31, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9266, 'lon': 32.8513},

    # Gazi Anadolu Lisesi (Beştepe / AAAL Yanı)
    {'ad': 'Gazi Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 465.7329, 'yuzdelik': 2.57, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9225, 'lon': 32.8105},

    # =============================================================================
    # 3. GRUP: %3 - %5 LİK DİLİM
    # =============================================================================

    # Mehmet Emin Resulzade Anadolu Lisesi (Balgat)
    {'ad': 'Mehmet Emin Resulzade Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 462.6738, 'yuzdelik': 3.12, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9125, 'lon': 32.8210},

    # Dr.Binnaz Ege-Dr.Rıdvan Ege Anadolu Lisesi (Balgat)
    {'ad': 'Dr.Binnaz Ege-Dr.Rıdvan Ege Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 458.7408, 'yuzdelik': 3.86, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9055, 'lon': 32.8155},

    # Şehit Oğuzhan Yaşar Anadolu Lisesi (Etimesgut Merkez)
    {'ad': 'Şehit Oğuzhan Yaşar Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 456.9634, 'yuzdelik': 4.22, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9485, 'lon': 32.6655},

    # Hacı Ömer Tarman Anadolu Lisesi (Hoşdere/Ayrancı)
    {'ad': 'Hacı Ömer Tarman Anadolu Lisesi (İngilizce)', 'ilce': 'Çankaya', 'puan': 455.5786, 'yuzdelik': 4.5, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8925, 'lon': 32.8455},

    # Nermin Mehmet Çekiç Anadolu Lisesi (Batıkent)
    {'ad': 'Nermin Mehmet Çekiç Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 453.6937, 'yuzdelik': 4.9, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9725, 'lon': 32.7655},

    # =============================================================================
    # 4. GRUP: %5 - %10 LUK DİLİM
    # =============================================================================

    # Vecihi Hürkuş Anadolu Lisesi (Keçiören / Etlik)
    {'ad': 'Vecihi Hürkuş Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 450.932, 'yuzdelik': 5.51, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0150, 'lon': 32.8450},

    # Tevfik İleri Anadolu İmam Hatip Lisesi (Beştepe)
    {'ad': 'Tevfik İleri Anadolu İmam Hatip Lisesi', 'ilce': 'Yenimahalle', 'puan': 449.8055, 'yuzdelik': 5.77, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9320, 'lon': 32.8150},

    # Mamak Fen Lisesi (Mamak / General Zeki Doğan)
    {'ad': 'Mamak Fen Lisesi', 'ilce': 'Mamak', 'puan': 445.0946, 'yuzdelik': 5.81, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9250, 'lon': 32.9350},

    # Ayrancı Anadolu Lisesi (Ayrancı / Emniyet Yanı)
    {'ad': 'Ayrancı Anadolu Lisesi (İngilizce)', 'ilce': 'Çankaya', 'puan': 448.7779, 'yuzdelik': 6.01, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9045, 'lon': 32.8485},

    # Cezeri Yeşil Teknoloji MTAL (Eryaman / Tunahan Mah.)
    # DÜZELTİLDİ: Koordinat hassasiyeti artırıldı.
    {'ad': 'Cezeri Yeşil Teknoloji MTAL', 'ilce': 'Etimesgut', 'puan': 447.8821, 'yuzdelik': 6.22, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9913, 'lon': 32.6221},

    # Betül Can Anadolu Lisesi (Gaziosmanpaşa)
    {'ad': 'Betül Can Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 444.6465, 'yuzdelik': 7.03, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8970, 'lon': 32.8750},

    # Mustafa Azmi Doğan Anadolu Lisesi (Batıkent)
    {'ad': 'Mustafa Azmi Doğan Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 443.1534, 'yuzdelik': 7.42, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9810, 'lon': 32.7750},

    # Altındağ Yıldırım Beyazıt Fen Lisesi (Altınpark Yanı)
    {'ad': 'Altındağ Yıldırım Beyazıt Fen Lisesi', 'ilce': 'Altındağ', 'puan': 441.7915, 'yuzdelik': 7.77, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9550, 'lon': 32.8850},

    # Süleyman Demirel Anadolu Lisesi (Elvankent)
    {'ad': 'Süleyman Demirel Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 440.0664, 'yuzdelik': 8.24, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9650, 'lon': 32.6050},

    # Ayhan Sümer Anadolu Lisesi (Batıkent)
    {'ad': 'Ayhan Sümer Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 438.3585, 'yuzdelik': 8.71, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9680, 'lon': 32.7500},

    # Ümitköy Anadolu Lisesi (Ümitköy)
    {'ad': 'Ümitköy Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 438.1636, 'yuzdelik': 8.76, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8910, 'lon': 32.7040},

    # Aydınlıkevler Anadolu Lisesi (Aydınlıkevler)
    {'ad': 'Aydınlıkevler Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 436.421, 'yuzdelik': 9.25, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9560, 'lon': 32.8860},

    # Mustafa Hakan Güvençer Fen Lisesi (Kahramankazan)
    {'ad': 'Mustafa Hakan Güvençer Fen Lisesi', 'ilce': 'Kahramankazan', 'puan': 435.6174, 'yuzdelik': 9.48, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.1980, 'lon': 32.6850},

    # Ankara Lisesi (Ulus / Tarihi Bina)
    {'ad': 'Ankara Lisesi', 'ilce': 'Altındağ', 'puan': 433.8407, 'yuzdelik': 10.0, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': False, 'kantin': True, 'kutuphane': True, 'lat': 39.9365, 'lon': 32.8585},

    # =============================================================================
    # 5. GRUP: %10 ve ÜZERİ (Genel Anadolu ve Meslek Liseleri)
    # =============================================================================

    # Şehit Ömer Halisdemir Anadolu Lisesi (Eryaman)
    {'ad': 'Şehit Ömer Halisdemir Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 433.0315, 'yuzdelik': 10.24, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9820, 'lon': 32.6300},

    # Fatih Anadolu Lisesi (Keçiören / Sanatoryum)
    {'ad': 'Fatih Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 432.2273, 'yuzdelik': 10.48, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0055, 'lon': 32.8525},

    # Yavuz Sultan Selim Anadolu Lisesi (Keçiören)
    {'ad': 'Yavuz Sultan Selim Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 428.1724, 'yuzdelik': 11.71, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0090, 'lon': 32.8610},

    # Polatlı TOBB Fen Lisesi (Polatlı)
    {'ad': 'Polatlı TOBB Fen Lisesi', 'ilce': 'Polatlı', 'puan': 424.3292, 'yuzdelik': 12.92, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.5750, 'lon': 32.1450},

    # Meliha Hasanali Bostan Çubuk Fen Lisesi (Çubuk)
    {'ad': 'Meliha Hasanali Bostan Çubuk Fen Lisesi', 'ilce': 'Çubuk', 'puan': 423.8322, 'yuzdelik': 13.08, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.2350, 'lon': 33.0350},

    # Pursaklar Ayyıldız Anadolu Lisesi (Pursaklar)
    {'ad': 'Pursaklar Ayyıldız Anadolu Lisesi', 'ilce': 'Pursaklar', 'puan': 423.2374, 'yuzdelik': 13.27, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0320, 'lon': 32.9050},

    # Gazi Lisesi (Ulus / Hergele Meydanı)
    {'ad': 'Gazi Lisesi', 'ilce': 'Altındağ', 'puan': 422.3387, 'yuzdelik': 13.57, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9370, 'lon': 32.8600},

    # TUSAŞ Şehit Hakan Gülşen MTAL (Kahramankazan / TAI Yanı)
    {'ad': 'TUSAŞ Şehit Hakan Gülşen MTAL', 'ilce': 'Kahramankazan', 'puan': 421.3274, 'yuzdelik': 13.9, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.2120, 'lon': 32.6920},

    # Gölbaşı Anadolu Lisesi (Gölbaşı)
    {'ad': 'Gölbaşı Anadolu Lisesi', 'ilce': 'Gölbaşı', 'puan': 418.1924, 'yuzdelik': 14.95, 'spor': True, 'yemek': False, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.7920, 'lon': 32.8080},

    # Aktepe Şehit Köksal Kaşaltı Anadolu Lisesi (Keçiören / Aktepe)
    {'ad': 'Aktepe Şehit Köksal Kaşaltı Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 417.8427, 'yuzdelik': 15.08, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0190, 'lon': 32.8720},

    # 75. Yıl Anadolu Lisesi (Çankaya / Cebeci)
    {'ad': '75. Yıl Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 417.5816, 'yuzdelik': 15.17, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9300, 'lon': 32.8700},

    # Şehit Hakan Kabil Ortaokulu/Lisesi (Keçiören / İncirli)
    {'ad': 'Şehit Hakan Kabil Ortaokulu', 'ilce': 'Keçiören', 'puan': 417.0278, 'yuzdelik': 15.35, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9869, 'lon': 32.8647},

    # Hasan Şahan Kışlası (Çubuk) - (Eğitim Kurumu Konumu)
    {'ad': 'Hasan Şahan Kışlası', 'ilce': 'Çubuk', 'puan': 411.7584, 'yuzdelik': 17.16, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.2381, 'lon': 33.0328},

    # Nene Hatun Anadolu Lisesi (Çankaya / Kırkkonaklar)
    {'ad': 'Nene Hatun Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 410.9705, 'yuzdelik': 17.43, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8950, 'lon': 32.8800},

    # Ankara Türk Telekom Sosyal Bilimler Lisesi (Ümitköy / Mutlukent)
    {'ad': 'Ankara Türk Telekom Sosyal Bilimler Lisesi', 'ilce': 'Çankaya', 'puan': 409.0835, 'yuzdelik': 18.11, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8880, 'lon': 32.7000},

    # Hasan Ali Yücel Sosyal Bilimler Lisesi (Çiğdem / ODTÜ Yanı)
    {'ad': 'Hasan Ali Yücel Sosyal Bilimler Lisesi', 'ilce': 'Çankaya', 'puan': 406.8408, 'yuzdelik': 18.93, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8752, 'lon': 32.8060},

    # Şehit Ali İhsan Lezgi Anadolu Lisesi (Pursaklar)
    {'ad': 'Şehit Ali İhsan Lezgi Anadolu Lisesi', 'ilce': 'Pursaklar', 'puan': 403.4916, 'yuzdelik': 20.19, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0420, 'lon': 32.9080},

    # Şehit Abdullah Tayyip Olçok Anadolu Lisesi (Yenimahalle)
    {'ad': 'Şehit Abdullah Tayyip Olçok Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 400.9926, 'yuzdelik': 21.14, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9665, 'lon': 32.7555},

    # Sabahattin Zaim Sosyal Bilimler Lisesi (Altındağ / Karapürçek)
    {'ad': 'Sabahattin Zaim Sosyal Bilimler Lisesi', 'ilce': 'Altındağ', 'puan': 395.5901, 'yuzdelik': 23.28, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9750, 'lon': 32.9550},

    # Ali-Hasan Coşkun Mesleki ve Teknik Anadolu Lisesi (Dikmen)
    {'ad': 'Ali-Hasan Coşkun Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 392.4277, 'yuzdelik': 24.58, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8650, 'lon': 32.8250},

    # Kirami Refia Alemdaroğlu Anadolu Lisesi (Gölbaşı)
    {'ad': 'Kirami Refia Alemdaroğlu Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 392.2758, 'yuzdelik': 24.64, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8975, 'lon': 32.8335},

    # Elvankent Bilgi Anadolu Lisesi (Etimesgut / Elvankent)
    {'ad': 'Elvankent Bilgi Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 391.1345, 'yuzdelik': 25.12, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9495, 'lon': 32.6840},

    # Şentepe Şehit Volkan Canöz Anadolu Lisesi (Yenimahalle / Şentepe)
    {'ad': 'Şentepe Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 354.3406, 'yuzdelik': 42.45, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0020, 'lon': 32.7810},

    # Pursaklar Anadolu Lisesi (Pursaklar)
    {'ad': 'Pursaklar Anadolu Lisesi', 'ilce': 'Pursaklar', 'puan': 386.7262, 'yuzdelik': 27.0, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0385, 'lon': 32.9033},

    # Şehit Mehmet Karakaşoğlu MTAL (Pursaklar)
    {'ad': 'Şehit Mehmet Karakaşoğlu MTAL', 'ilce': 'Pursaklar', 'puan': 386.0718, 'yuzdelik': 27.29, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0385, 'lon': 32.9033},

    # Erdem Beyazıt Anadolu Lisesi (Gölbaşı)
    {'ad': 'Erdem Beyazıt Anadolu Lisesi', 'ilce': 'Gölbaşı', 'puan': 383.0543, 'yuzdelik': 28.61, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.7750, 'lon': 32.7950},

    # Ankara Mesleki ve Teknik Anadolu Lisesi (Ulus / Kazımkarabekir)
    {'ad': 'Ankara Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 382.7212, 'yuzdelik': 28.76, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9450, 'lon': 32.8600},

    # Polatlı Anadolu Lisesi (Polatlı)
    {'ad': 'Polatlı Anadolu Lisesi', 'ilce': 'Polatlı', 'puan': 382.4921, 'yuzdelik': 28.87, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.5800, 'lon': 32.1319},

    # Kalaba Anadolu Lisesi (Keçiören / Kalaba)
    {'ad': 'Kalaba Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 378.1064, 'yuzdelik': 30.82, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0010, 'lon': 32.8630},

    # Kocatepe Mimar Kemal Anadolu Lisesi (Kızılay)
    {'ad': 'Kocatepe Mimar Kemal Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 376.5342, 'yuzdelik': 31.54, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9170, 'lon': 32.8590},

    # Batıkent Mesleki ve Teknik Anadolu Lisesi (Batıkent)
    {'ad': 'Batıkent Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 375.3214, 'yuzdelik': 32.1, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9750, 'lon': 32.7450},

    # Halide Edip MTAL (Çankaya / Bahçelievler)
    {'ad': 'Halide Edip MTAL', 'ilce': 'Çankaya', 'puan': 373.1895, 'yuzdelik': 33.1, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9230, 'lon': 32.8250},

    # Şehit Sercan Öztürk Anadolu Lisesi (Yenimahalle)
    {'ad': 'Şehit Sercan Öztürk Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 371.7458, 'yuzdelik': 33.78, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9775, 'lon': 32.7160},

    # Zübeyde Hanım MTAL (Altındağ / İskitler)
    {'ad': 'Zübeyde Hanım MTAL', 'ilce': 'Altındağ', 'puan': 371.0503, 'yuzdelik': 34.12, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9500, 'lon': 32.8480},

    # Şehit Murat Demirci Anadolu Lisesi (Mamak)
    {'ad': 'Şehit Murat Demirci Anadolu Lisesi', 'ilce': 'Mamak', 'puan': 370.4705, 'yuzdelik': 34.39, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9240, 'lon': 32.9350},

    # Elmadağ Anadolu Lisesi (Elmadağ Merkez)
    {'ad': 'Elmadağ Anadolu Lisesi', 'ilce': 'Elmadağ', 'puan': 365.2635, 'yuzdelik': 36.94, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9173, 'lon': 33.2344},

    # Keçiören Mesleki ve Teknik Anadolu Lisesi (Keçiören / Dutluk)
    {'ad': 'Keçiören Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 363.8041, 'yuzdelik': 37.66, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0050, 'lon': 32.8650},

    # Abidinpaşa Anadolu Lisesi (Mamak / Abidinpaşa)
    {'ad': 'Abidinpaşa Anadolu Lisesi', 'ilce': 'Mamak', 'puan': 361.2683, 'yuzdelik': 38.93, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9240, 'lon': 32.9060},

    # Beypazarı Nurettin Karaoğuz Vakfı Anadolu Lisesi (Beypazarı)
    {'ad': 'Beypazarı Nurettin Karaoğuz Vakfı Anadolu Lisesi', 'ilce': 'Beypazarı', 'puan': 360.2798, 'yuzdelik': 39.42, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.1675, 'lon': 31.9211},

    # Güvercinlik Şehit Kaya Aldoğan Anadolu Lisesi (Etimesgut / Güvercinlik)
    {'ad': 'Güvercinlik Şehit Kaya Aldoğan Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 359.7214, 'yuzdelik': 39.71, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9400, 'lon': 32.7300},

    # Şentepe Anadolu Lisesi (Yenimahalle / Şentepe)
    {'ad': 'Şentepe Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 354.3406, 'yuzdelik': 42.45, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9950, 'lon': 32.7850},

    # Akyurt Şükrü Acar Anadolu Lisesi (Akyurt)
    {'ad': 'Akyurt Şükrü Acar Anadolu Lisesi', 'ilce': 'Akyurt', 'puan': 349.0306, 'yuzdelik': 45.21, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.1300, 'lon': 33.1000},

    # Sincan Anadolu Lisesi (Sincan)
    {'ad': 'Sincan Anadolu Lisesi', 'ilce': 'Sincan', 'puan': 348.604, 'yuzdelik': 45.43, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9575, 'lon': 32.5780},

    # Bağlum Anadolu Lisesi (Keçiören / Bağlum)
    {'ad': 'Bağlum Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 344.2494, 'yuzdelik': 47.74, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0500, 'lon': 32.8500},

    # Altındağ Anadolu Lisesi (Altındağ)
    {'ad': 'Altındağ Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 338.4556, 'yuzdelik': 50.84, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9416, 'lon': 32.8546},

    # Şehit Yasin Bahadır Yüce Anadolu Lisesi (Gölbaşı)
    {'ad': 'Şehit Yasin Bahadır Yüce Anadolu Lisesi', 'ilce': 'Gölbaşı', 'puan': 336.8833, 'yuzdelik': 51.68, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.7820, 'lon': 32.8050},

    # Akşemsettin Anadolu Lisesi (Sincan)
    {'ad': 'Akşemsettin Anadolu Lisesi', 'ilce': 'Sincan', 'puan': 333.1026, 'yuzdelik': 53.76, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9600, 'lon': 32.5800},

    # Layika Akbilek MTAL (Etimesgut)
    {'ad': 'Layika Akbilek MTAL', 'ilce': 'Etimesgut', 'puan': 330.1558, 'yuzdelik': 55.4, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9635, 'lon': 32.5830},
    # Gevher Nesibe MTAL (Çankaya / Etlik Zübeyde Hanım Doğumevi Yanı)
    {'ad': 'Gevher Nesibe MTAL', 'ilce': 'Keçiören', 'puan': 327.915, 'yuzdelik': 56.63, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9650, 'lon': 32.8350},

    # İbn-i Sina MTAL (Yenimahalle / Serhat Mah.)
    {'ad': 'İbn-i Sina MTAL', 'ilce': 'Yenimahalle', 'puan': 326.6876, 'yuzdelik': 57.34, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9750, 'lon': 32.7800},

    # Faruk Nafiz Çamlıbel Anadolu Lisesi (Eryaman)
    {'ad': 'Faruk Nafiz Çamlıbel Anadolu Lisesi', 'ilce': 'Etimesgut', 'puan': 324.9654, 'yuzdelik': 58.33, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9800, 'lon': 32.6200},

    # Fatih MTAL (Keçiören)
    {'ad': 'Fatih MTAL', 'ilce': 'Keçiören', 'puan': 323.003, 'yuzdelik': 59.46, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0050, 'lon': 32.8520},

    # Çankaya İMKB MTAL (Çankaya / Dikmen)
    {'ad': 'Çankaya İMKB MTAL', 'ilce': 'Çankaya', 'puan': 319.2312, 'yuzdelik': 61.64, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.8500, 'lon': 32.8300},

    # Uluğbey Anadolu Lisesi (Altındağ / Siteler)
    {'ad': 'Uluğbey Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 316.5878, 'yuzdelik': 63.22, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9550, 'lon': 32.9100},

    # Yenimahalle Zeynep-Salih Alp MTAL (Yenimahalle)
    {'ad': 'Yenimahalle Zeynep-Salih Alp MTAL', 'ilce': 'Yenimahalle', 'puan': 311.9682, 'yuzdelik': 65.99, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9665, 'lon': 32.7555},

    # Kanuni MTAL (Keçiören / Ufuktepe)
    {'ad': 'Kanuni MTAL', 'ilce': 'Keçiören', 'puan': 309.8452, 'yuzdelik': 67.29, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 40.0200, 'lon': 32.8600},

    # Şehit Özgür Gencer Anadolu Lisesi (Sincan / Temelli - Dikkat: Uzak)
    {'ad': 'Şehit Özgür Gencer Anadolu Lisesi', 'ilce': 'Sincan', 'puan': 308.5746, 'yuzdelik': 68.07, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.7200, 'lon': 32.4500},

    # Üreğil MTAL (Mamak / Üreğil)
    {'ad': 'Üreğil MTAL', 'ilce': 'Mamak', 'puan': 308.2043, 'yuzdelik': 68.3, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9300, 'lon': 32.9500},

    # Ortaköy 80. Yıl MTAL (Mamak / Ortaköy)
    {'ad': 'Ortaköy 80. Yıl MTAL', 'ilce': 'Mamak', 'puan': 304.5504, 'yuzdelik': 70.57, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9500, 'lon': 33.0500},

    # Etimesgut MTAL (Etimesgut / İstasyon)
    {'ad': 'Etimesgut MTAL', 'ilce': 'Etimesgut', 'puan': 300.7712, 'yuzdelik': 72.95, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9500, 'lon': 32.6800},

    # Şehit Arda Can MTAL (Polatlı)
    {'ad': 'Şehit Arda Can MTAL', 'ilce': 'Polatlı', 'puan': 295.4243, 'yuzdelik': 76.32, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.5850, 'lon': 32.1300},

    # Yenimahalle Ostim Mesleki ve Teknik Anadolu Lisesi (Ostim)
    {'ad': 'Yenimahalle Ostim Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Yenimahalle', 'puan': 288.73, 'yuzdelik': 80.64, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9650, 'lon': 32.7400},

    # İncirli Mesleki ve Teknik Anadolu Lisesi (Keçiören / Etlik)
    {'ad': 'İncirli Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Keçiören', 'puan': 286.4327, 'yuzdelik': 82.16, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9850, 'lon': 32.8450},

    # İskitler Mesleki ve Teknik Anadolu Lisesi (Altındağ / İskitler)
    {'ad': 'İskitler Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 286.4327, 'yuzdelik': 82.16, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9530, 'lon': 32.8450},

    # Çankaya Borsa İstanbul Turizm MTAL (Balgat)
    {'ad': 'Çankaya Borsa İstanbul Turizm Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 285.3, 'yuzdelik': 82.9, 'spor': False, 'yemek': False, 'konferans': True, 'bilg_lab': False, 'fen_lab': False, 'kantin': False, 'kutuphane': True, 'lat': 39.9020, 'lon': 32.8250},

    # Sincan Fatih MTAL (Sincan)
    # DÜZELTİLDİ: Sincan Fatih Kampüsüne (Yenikent tarafı değil) çekildi.
    {'ad': 'Sincan Fatih MTAL', 'ilce': 'Sincan', 'puan': 284.1485, 'yuzdelik': 83.67, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9840, 'lon': 32.5945},

    # Şehit Hakan Ünver MTAL (Sincan)
    {'ad': 'Şehit Hakan Ünver MTAL', 'ilce': 'Sincan', 'puan': 275.6033, 'yuzdelik': 89.37, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9600, 'lon': 32.5800},

    # Balgat Mesleki ve Teknik Anadolu Lisesi (Balgat / MHP Genel Mrk. Yanı)
    {'ad': 'Balgat Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Çankaya', 'puan': 258.098, 'yuzdelik': 100.0, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.9010, 'lon': 32.8120},

    # Polatlı MTAL (Polatlı)
    {'ad': 'Polatlı MTAL', 'ilce': 'Polatlı', 'puan': 255.4599, 'yuzdelik': 100.0, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.5800, 'lon': 32.1319},

    # Sincan Ahmet Andiçen Ticaret MTAL (Sincan / Lale Meydanı)
    {'ad': 'Sincan Ahmet Andiçen Ticaret Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Sincan', 'puan': 238.76, 'yuzdelik': 100.0, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': False, 'kantin': False, 'kutuphane': True, 'lat': 39.9620, 'lon': 32.5780},

    # Altındağ Atatürk Mesleki ve Teknik Anadolu Lisesi (Siteler)
    {'ad': 'Altındağ Atatürk Mesleki ve Teknik Anadolu Lisesi', 'ilce': 'Altındağ', 'puan': 235.0, 'yuzdelik': 100.0, 'spor': True, 'yemek': True, 'konferans': True, 'bilg_lab': False, 'fen_lab': True, 'kantin': False, 'kutuphane': True, 'lat': 39.9550, 'lon': 32.9050},

    # Haymana Anadolu İmam Hatip Lisesi (Haymana Merkez)
    {'ad': 'Haymana Anadolu İmam Hatip Lisesi', 'ilce': 'Haymana', 'puan': 150.5, 'yuzdelik': 100.0, 'spor': False, 'yemek': True, 'konferans': True, 'bilg_lab': True, 'fen_lab': True, 'kantin': True, 'kutuphane': True, 'lat': 39.4250, 'lon': 32.4950},
]
