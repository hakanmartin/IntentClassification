import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Excel dosyasını oku ve bir DataFrame'e yükle
veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/ProjeVeriSetiEn_TR.xlsx')

# Türkçe metinlerin olduğu 'TR' sütununu seçin
metinler = veri_seti['TR'].values.astype('U')

# TF-IDF vektörleştiriciyi tanımlayın ve uygulayın
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)

# TF-IDF vektörlerini X, niyet etiketlerini y olarak tanımlama
X = tfidf_vectors
y = veri_seti['INTENT']

# Eğitim ve test veri setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Support Vector Machine modeli oluşturma ve eğitme
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Test veri seti üzerinde tahmin yapma
y_pred = svm_model.predict(X_test)

# Model performansını değerlendirme
sonuc = classification_report(y_test, y_pred, zero_division=1, output_dict=True)

def genel_dogruluk(sonuc, agirliklar):
    accuracy = sonuc['accuracy']
    precision = sonuc['macro avg']['precision']
    recall = sonuc['macro avg']['recall']
    f1_score = sonuc['macro avg']['f1-score']

    toplam_agirlik = sum(agirliklar)
    genel_dogruluk = (agirliklar[0] * accuracy + agirliklar[1] * precision +
                      agirliklar[2] * recall + agirliklar[3] * f1_score) / toplam_agirlik

    return genel_dogruluk

# Ağırlıkları tanımlama
agirliklar = [0.6, 0.2, 0.2, 0.0]

# Genel doğruluğu hesaplama
genel_dogruluk_degeri = genel_dogruluk(sonuc, agirliklar)

# Genel doğruluğu yazdırma
print(f"Genel Doğruluk: {genel_dogruluk_degeri}")
