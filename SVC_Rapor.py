import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

egitim_veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Egitim-3972-2.xlsx')
test_veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000.xlsx')

egitim_metinler = egitim_veri_seti['TR'].values.astype('U')
test_metinler = test_veri_seti['TR'].values.astype('U')

tfidf_vectorizer = TfidfVectorizer()
egitim_tfidf_vectors = tfidf_vectorizer.fit_transform(egitim_metinler)
test_tfidf_vectors = tfidf_vectorizer.transform(test_metinler)

# TF-IDF vektörlerini X, niyet etiketlerini y olarak tanımlama
X_train = egitim_tfidf_vectors
y_train = egitim_veri_seti['INTENT']

X_test = test_tfidf_vectors
y_test = test_veri_seti['INTENT']

# Support Vector Machine modeli oluşturma ve eğitme
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Test veri seti üzerinde tahmin yapma
y_pred = svm_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

print(classification_report(y_test, y_pred, zero_division=1))
