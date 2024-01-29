import re

# Kural örneklerini ve niyetleri içeren sözlük
patterns = {
    "atis_flight": ["uçmak", "uçuş", "uçuşlar", "uçak bileti", "havayolu", "ucus rezervasyonu", "havayolu firması", "varış noktası", "dönüş uçuşu"],
    "atis_flight_time": ["saat", "kalkış saati", "varış saati", "uçuş saatleri", "gece uçuşları", "uçuş süresi", "ne zaman varır", "gecenin ortası uçuşları", "erken sabah uçuşları", "gündüz uçuşları"],
    "atis_airfare": ["fiyat", "ücret", "maliyet", "bilet fiyatı", "uçuş ücreti", "ucuz bilet", "promosyonlu uçuşlar", "indirimli bilet", "bütçe uçuşları", "ekonomik sınıf fiyatları","ekonomik"],
    "atis_ground_service": ["havaalanı transferi", "araç kiralama", "otopark", "havaalanı servisleri", "havalimanı taşıma", "ulaşım seçenekleri", "şehir merkezi ulaşımı", "havaalanı taksi", "otobüs servisi", "havaalanı terminali","kara taşımacılığı","kara"],
    "atis_airport": ["havaalanı", "terminal", "havaalanı kodu", "hava limanı", "varış noktası", "havaalanı haritası", "terminal bilgisi", "havaalanı terminal numaraları", "havaalanı giriş çıkışları", "bagaj teslim alanı"],
    "atis_distance": ["uzaklık", "mesafe", "ne kadar uzaklıkta", "uçuş mesafesi", "varış noktası uzaklığı", "havaalanı mesafesi", "şehirlerarası mesafe", "rota uzunluğu", "toplam uçuş mesafesi", "havaalanı şehir merkezi uzaklığı"],
    "atis_airline": ["havayolu", "hava yolu şirketi", "hangi havayolu", "hava şirketi", "ucus firması", "havayolu itibarı", "havayolu güvenilirliği", "yıldızlı havayolu", "havayolu derecelendirmesi", "havayolu hizmet kalitesi"],
    "atis_abbreviation": ["kısaltma", "kod", "ne anlama geliyor", "havaalanı kodu", "havayolu kısaltması", "rezervasyon kodu", "uçuş numarası", "check-in kodu", "uçuş kodu", "ucus referans kodu"],
    "atis_quantity": ["kaç", "miktar", "sayı", "uçuş sayısı", "kaç uçuş var", "koltuk sayısı", "yatay bagaj kapasitesi", "bilet adedi", "varış noktası sayısı", "gece uçuşu sayısı"],
    "atis_capacity": ["kapasite", "koltuk sayısı", "taşıma kapasitesi", "uçak kapasitesi", "koltuk sayısı nedir", "bagaj taşıma kapasitesi", "biniş kapasitesi", "yolcu kapasitesi", "uçak içi kapasite", "maksimum yolcu kapasitesi"],
    # Diğer niyetler buraya eklenebilir
}

def detect_intent(user_input):
    detected_intents = []

    # Her bir kural örneğini kontrol et
    for intent, patterns_list in patterns.items():
        for pattern in patterns_list:
            if re.search(rf"\b{pattern}\b", user_input, re.IGNORECASE):
                detected_intents.append(intent)

    return detected_intents

# Kullanıcıdan giriş iste
user_input = input("Metin: ")

# Niyeti tespit et
intents = detect_intent(user_input)

if intents:
    print("Niyet:", '#'.join(set(intents)))
else:
    print("Niyet: Niyet bulunamadı.")
