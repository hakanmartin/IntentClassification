import spacy
from spacy.matcher import Matcher

nlp = spacy.load("tr_core_news_md")
matcher = Matcher(nlp.vocab)

# Add match IDs and patterns directly to the Matcher
patterns = {
    "atis_flight": [[{"LOWER": {"IN": ["uçmak", "uçuş", "uçuşlar", "uçak bileti", "havayolu", "uçuş rezervasyonu", "havayolu firması", "varış noktası", "dönüş uçuşu"]}}]],
    "atis_flight_time": [[{"LOWER": {"IN": ["saat", "kalkış saati", "varış saati", "uçuş saatleri", "gece uçuşları", "uçuş süresi", "ne zaman varır", "gecenin ortası uçuşları", "erken sabah uçuşları", "gündüz uçuşları"]}}]],
    "atis_airfare": [[{"LOWER": {"IN": ["fiyat", "ücret", "maliyet", "bilet fiyatı", "uçuş ücreti", "ucuz bilet", "promosyonlu uçuşlar", "indirimli bilet", "bütçe uçuşları", "ekonomik sınıf fiyatları"]}}]],
    "atis_ground_service": [[{"LOWER": {"IN": ["havaalanı transferi", "araç kiralama", "otopark", "havaalanı servisleri", "havalimanı taşıma", "ulaşım seçenekleri", "şehir merkezi ulaşımı", "havaalanı taksi", "otobüs servisi", "havaalanı terminali","kara taşımacılığı","kara"]}}]],
    "atis_airport": [[{"LOWER": {"IN": ["havaalanı", "terminal", "havaalanı kodu", "hava limanı", "varış noktası", "havaalanı haritası", "terminal bilgisi", "havaalanı terminal numaraları", "havaalanı giriş çıkışları", "bagaj teslim alanı"]}}]],
    "atis_distance": [[{"LOWER": {"IN": ["uzaklık", "mesafe", "ne kadar uzaklıkta", "uçuş mesafesi", "varış noktası uzaklığı", "havaalanı mesafesi", "şehirlerarası mesafe", "rota uzunluğu", "toplam uçuş mesafesi", "havaalanı şehir merkezi uzaklığı"]}}]],
    "atis_airline": [[{"LOWER": {"IN": ["havayolu", "hava yolu şirketi", "hangi havayolu", "hava şirketi", "uçuş firması", "havayolu itibarı", "havayolu güvenilirliği", "yıldızlı havayolu", "havayolu derecelendirmesi", "havayolu hizmet kalitesi"]}}]],
    "atis_abbreviation": [[{"LOWER": {"IN": ["kısaltma", "kod", "ne anlama geliyor", "havaalanı kodu", "havayolu kısaltması", "rezervasyon kodu", "uçuş numarası", "check-in kodu", "uçuş kodu", "ucus referans kodu"]}}]],
    "atis_quantity": [[{"LOWER": {"IN": ["kaç", "miktar", "sayı", "uçuş sayısı", "kaç uçuş var", "koltuk sayısı", "yatay bagaj kapasitesi", "bilet adedi", "varış noktası sayısı", "gece uçuşu sayısı"]}}]],
    "atis_capacity": [[{"LOWER": {"IN": ["kapasite", "koltuk sayısı", "taşıma kapasitesi", "uçak kapasitesi", "koltuk sayısı nedir", "bagaj taşıma kapasitesi", "biniş kapasitesi", "yolcu kapasitesi", "uçak içi kapasite", "maksimum yolcu kapasitesi"]}}]],

}

# Add patterns for each intent directly to the Matcher
for intent, intent_patterns in patterns.items():
    for pattern in intent_patterns:
        matcher.add(intent, [pattern])

# Kullanıcıdan giriş iste
user_input = input("Metin: ")

# Giriş metnini analiz et
doc = nlp(user_input)

# Matcher'ı kullanarak niyetleri tespit et
matches = matcher(doc)

if matches:
    detected_intents = set()
    for match_id, start, end in matches:
        detected_intents.add(nlp.vocab.strings[match_id])
    print("Niyet:", '#'.join(detected_intents))
else:
    print("Niyet: Niyet bulunamadı :(")
