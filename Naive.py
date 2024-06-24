import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

egitim_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Egitim-3972.xlsx')
test_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test-1000.xlsx')

# Eğitim ve test veri setlerindeki metinleri alma
egitim_metinler = egitim_veri_seti['TR'].values.astype('U')
test_metinler = test_veri_seti['TR'].values.astype('U')

# TF-IDF vektörlerini oluşturma
tfidf_vectorizer = TfidfVectorizer()
egitim_tfidf_vectors = tfidf_vectorizer.fit_transform(egitim_metinler)
test_tfidf_vectors = tfidf_vectorizer.transform(test_metinler)

# Eğitim ve test veri setlerini ilgili etiketlerle birlikte ayarlama
X_train, y_train = egitim_tfidf_vectors, egitim_veri_seti['INTENT']
X_test, y_test = test_tfidf_vectors, test_veri_seti['INTENT']

# Naive Bayes modeli oluşturma ve eğitme
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = nb_model.predict(X_test)

# Model performansını değerlendirme
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

print(classification_report(y_test, y_pred, zero_division=1))

# Confusion matrix oluşturma ve görselleştirme
cm = confusion_matrix(y_test, y_pred)
confusion_df = pd.DataFrame(cm, index=nb_model.classes_, columns=nb_model.classes_)
sns.heatmap(confusion_df, annot=True, cmap='YlGnBu')
plt.xlabel('Tahmini Niyet')
plt.ylabel('Gerçek Niyet')
plt.show()
