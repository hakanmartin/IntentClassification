import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import hstack

# Veri setlerini okuma
egitim_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Egitim-3972-4.xlsx')
test_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test3-1000.xlsx')

# Metin verilerini ve NER sütunlarını al
egitim_metinler = egitim_veri_seti['TR'].values.astype('U')
test_metinler = test_veri_seti['TR'].values.astype('U')
egitim_nerler = egitim_veri_seti['NER'].values.reshape(-1, 1)
test_nerler = test_veri_seti['NER'].values.reshape(-1, 1)
egitim_da = egitim_veri_seti['DA'].values.reshape(-1, 1)
test_da = test_veri_seti['DA'].values.reshape(-1, 1)

# TF-IDF vektörlerini oluşturma
tfidf_vectorizer = TfidfVectorizer()
egitim_tfidf_vectors = tfidf_vectorizer.fit_transform(egitim_metinler)
test_tfidf_vectors = tfidf_vectorizer.transform(test_metinler)

# TF-IDF vektörleri ile NER ve DA sütunlarını birleştirme
X_train = hstack((egitim_tfidf_vectors, egitim_nerler, egitim_da))
X_test = hstack((test_tfidf_vectors, test_nerler, test_da))

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

# Confusion Matrix oluşturma
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 7))  # Figür boyutunu artırarak daha geniş bir alan yaratma
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=svm_model.classes_, yticklabels=svm_model.classes_, annot_kws={"size": 10})
plt.xlabel('Tahmin Edilen', fontsize=12)
plt.ylabel('Gerçek', fontsize=12)
plt.title('Confusion Matrix', fontsize=15)
plt.xticks(rotation=90, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()  # Layout'u sıkılaştırarak eksen etiketlerinin kesilmesini önler
plt.show()