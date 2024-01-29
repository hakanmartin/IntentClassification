import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Excel dosyasını oku ve bir DataFrame'e yükle
veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Proje1.2VeriSetiEn _TR.xlsx')

# Türkçe metinlerin olduğu 'TR' sütununu seçin
metinler = veri_seti['TR'].values.astype('U')

# TF-IDF vektörleştiriciyi tanımlayın ve uygulayın
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)

# Elde edilen TF-IDF matrisini gözlemleme
#print(tfidf_vectors.shape)  # Vektörlerin boyutunu kontrol edin
#print(tfidf_vectors.toarray())  # TF-IDF matrisini dizi olarak görüntüleyin

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
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

# Sınıflandırma raporu
print(classification_report(y_test, y_pred, zero_division=1))
