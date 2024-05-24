import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Excel dosyasını oku ve bir DataFrame'e yükle
veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/ProjeVeriSetiEn_TR.xlsx')

metinler = veri_seti['TR'].values.astype('U')

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

svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

print(classification_report(y_test, y_pred, zero_division=1))
