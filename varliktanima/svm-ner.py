import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from scipy.sparse import hstack # type: ignore

# Veri setlerini okuma
egitim_veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Egitim-3972-2.xlsx')
test_veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000-4.xlsx')

# Metin verilerini ve NER sütunlarını al
egitim_metinler = egitim_veri_seti['TR'].values.astype('U')
test_metinler = test_veri_seti['TR'].values.astype('U')
egitim_nerler = egitim_veri_seti['NER'].values.reshape(-1, 1)
test_nerler = test_veri_seti['NER'].values.reshape(-1, 1)

# TF-IDF vektörlerini oluşturma
tfidf_vectorizer = TfidfVectorizer()
egitim_tfidf_vectors = tfidf_vectorizer.fit_transform(egitim_metinler)
test_tfidf_vectors = tfidf_vectorizer.transform(test_metinler)

# NER sütununu kategorik olarak kodlama
column_transformer = ColumnTransformer(
    [('onehot', OneHotEncoder(), [0])],  # NER sütunu için OneHotEncoder kullan
    remainder='passthrough'
)

# Eğitim ve test veri setlerine NER sütununu ekleme
egitim_tfidf_ner = column_transformer.fit_transform(egitim_nerler)
test_tfidf_ner = column_transformer.transform(test_nerler)

# TF-IDF vektörleri ile NER sütunlarını birleştirme
X_train = hstack((egitim_tfidf_vectors, egitim_tfidf_ner))
X_test = hstack((test_tfidf_vectors, test_tfidf_ner))

# Etiketleri tanımlama
y_train = egitim_veri_seti['INTENT']
y_test = test_veri_seti['INTENT']

# Modeli oluşturma ve eğitme
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Tahmin yapma
y_pred = svm_model.predict(X_test)

# Doğruluk hesaplama
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

# Sınıflandırma raporu
print(classification_report(y_test, y_pred, zero_division=1))

# Tahmin edilen sonuçları veri setine ekleme ve kaydetme
test_veri_seti['PREDICTED_INTENT'] = y_pred
test_veri_seti.to_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000-4.xlsx', index=False)
print("Tahminler sonuçlar dosyasına kaydedildi.")
