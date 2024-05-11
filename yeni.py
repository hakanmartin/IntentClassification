import tkinter as tk
from PIL import Image, ImageTk


def girdi_al():
    kullanici_girdisi = girdi.get()
    print("Kullanıcı Girdisi:", kullanici_girdisi)
    tik_buton.pack()
    carpi_buton.pack()
    detect_intent(kullanici_girdisi)


def secenek_tik():
    print("Niyet doğru bulundu")


#    ana_pencere.quit()

def secenek_carpi():
    print("Niyet yanlış bulundu")


#    ana_pencere.quit()

def detect_intent(user_input):
    intents = {
        "atis_flight": ["uçmak", "uçuş", "uçuşlar", "uçak bileti", "havayolu", "uçuş rezervasyonu", "havayolu firması",
                        "varış noktası", "dönüş uçuşu"],
        "atis_flight_time": ["saat", "kalkış saati", "varış saati", "uçuş saatleri", "gece uçuşları", "uçuş süresi",
                             "ne zaman varır", "gecenin ortası uçuşları", "erken sabah uçuşları", "gündüz uçuşları"],
        "atis_airfare": ["fiyat", "ücret", "maliyet", "bilet fiyatı", "uçuş ücreti", "ucuz bilet",
                         "promosyonlu uçuşlar", "indirimli bilet", "bütçe uçuşları", "ekonomik sınıf fiyatları"],
        "atis_ground_service": ["havaalanı transferi", "araç kiralama", "otopark", "havaalanı servisleri",
                                "havalimanı taşıma", "ulaşım seçenekleri", "şehir merkezi ulaşımı", "havaalanı taksi",
                                "otobüs servisi", "havaalanı terminali", "kara taşımacılığı", "kara"],
        "atis_airport": ["havaalanı", "terminal", "havaalanı kodu", "hava limanı", "varış noktası",
                         "havaalanı haritası", "terminal bilgisi", "havaalanı terminal numaraları",
                         "havaalanı giriş çıkışları", "bagaj teslim alanı"],
        "atis_distance": ["uzaklık", "mesafe", "ne kadar uzaklıkta", "uçuş mesafesi", "varış noktası uzaklığı",
                          "havaalanı mesafesi", "şehirlerarası mesafe", "rota uzunluğu", "toplam uçuş mesafesi",
                          "havaalanı şehir merkezi uzaklığı"],
        "atis_airline": ["havayolu", "hava yolu şirketi", "hangi havayolu", "hava şirketi", "uçuş firması",
                         "havayolu itibarı", "havayolu güvenilirliği", "yıldızlı havayolu", "havayolu derecelendirmesi",
                         "havayolu hizmet kalitesi"],
        "atis_abbreviation": ["kısaltma", "kod", "ne anlama geliyor", "havaalanı kodu", "havayolu kısaltması",
                              "rezervasyon kodu", "uçuş numarası", "check-in kodu", "uçuş kodu", "ucus referans kodu"],
        "atis_quantity": ["kaç", "miktar", "sayı", "uçuş sayısı", "kaç uçuş var", "koltuk sayısı",
                          "yatay bagaj kapasitesi", "bilet adedi", "varış noktası sayısı", "gece uçuşu sayısı"],
        "atis_capacity": ["kapasite", "koltuk sayısı", "taşıma kapasitesi", "uçak kapasitesi", "koltuk sayısı nedir",
                          "bagaj taşıma kapasitesi", "biniş kapasitesi", "yolcu kapasitesi", "uçak içi kapasite",
                          "maksimum yolcu kapasitesi"],

    }

    detected_intent = None
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                detected_intent = intent
                break
        if detected_intent:
            break

    if detected_intent:
        print("Tespit Edilen Niyet:", detected_intent)
        niyet_etiketi.config(text="Tespit Edilen Niyet: " + detected_intent)
        niyet_etiketi.pack()
        handle_intent(detected_intent)
    else:
        print("Niyet Tespit Edilemedi.")
        niyet_etiketi.config(text="Niyet Tespit Edilemedi.")
        niyet_etiketi.pack()


def handle_intent(intent):
    if intent == "atis_flight":
        print("Uçuş niyeti tespit edildi.")
    elif intent == "atis_flight_time":
        print("Uçuş saatleri niyeti tespit edildi.")
    elif intent == "atis_airfare":
        print("Uçak bileti fiyatı niyeti tespit edildi.")


ana_pencere = tk.Tk()
ana_pencere.title("NİYET TESPİT")
ana_pencere.geometry("300x300")
ana_pencere.configure(bg="lightblue")

girdi_etiketi = tk.Label(ana_pencere, text="Metin girin", bg="lightblue")
girdi_etiketi.pack(pady=5)

girdi = tk.Entry(ana_pencere, bg="white", fg="black")
girdi.pack(pady=5)

girdi_butonu = tk.Button(ana_pencere, text="Girdiyi Al", command=girdi_al, bg="#008CBA", fg="white")
girdi_butonu.pack(pady=5)

tik_buton = tk.Button(ana_pencere, text="  ✔️", command=secenek_tik, font=("Arial", 10), bg="#4CAF50", fg="white",
                      width=3)
tik_buton.pack(side=tk.LEFT, padx=5)
tik_buton.pack_forget()

carpi_buton = tk.Button(ana_pencere, text="❌", command=secenek_carpi, font=("Arial", 10), bg="#f44336", fg="white",
                        width=3)
carpi_buton.pack(side=tk.LEFT, padx=5)
carpi_buton.pack_forget()

niyet_etiketi = tk.Label(ana_pencere, text="", bg="white")
niyet_etiketi.pack()

ana_pencere.mainloop()