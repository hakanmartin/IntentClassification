import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Veri setlerini yükleme
egitim_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Egitim-NER-S.xlsx')
test_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test-NER-S.xlsx')

# Boş değerleri uygun bir şekilde doldurma
egitim_veri_seti['NER'] = egitim_veri_seti['NER'].fillna('')
test_veri_seti['NER'] = test_veri_seti['NER'].fillna('')

# TF-IDF vektörlerini oluşturma, NER etiketlerini de dikkate alarak
egitim_metinler_ner = [text + ' ' + str(ner) if not isinstance(ner, float) else text for text, ner in zip(egitim_veri_seti['TR'], egitim_veri_seti['NER'])]
test_metinler_ner = [text + ' ' + str(ner) if not isinstance(ner, float) else text for text, ner in zip(test_veri_seti['TR'], test_veri_seti['NER'])]

tfidf_vectorizer_ner = TfidfVectorizer()
egitim_tfidf_vectors_ner = tfidf_vectorizer_ner.fit_transform(egitim_metinler_ner)
test_tfidf_vectors_ner = tfidf_vectorizer_ner.transform(test_metinler_ner)

# Eğitim ve test veri setlerini ilgili etiketlerle birlikte ayarlama
X_train_ner = egitim_tfidf_vectors_ner
y_train_ner = egitim_veri_seti['INTENT']

X_test_ner = test_tfidf_vectors_ner
y_test_ner = test_veri_seti['INTENT']

# Support Vector Machine modeli oluşturma ve eğitme
svm_model_ner = SVC(kernel='linear')
svm_model_ner.fit(X_train_ner, y_train_ner)

# Test veri seti üzerinde tahmin yapma
y_pred_ner = svm_model_ner.predict(X_test_ner)

# Model performansını değerlendirme
accuracy_ner = accuracy_score(y_test_ner, y_pred_ner)
print(f"Model Doğruluğu (NER ile): {accuracy_ner}")

print(classification_report(y_test_ner, y_pred_ner, zero_division=1))

# Confusion matrix oluşturma ve görselleştirme
cm_ner = confusion_matrix(y_test_ner, y_pred_ner)
confusion_df_ner = pd.DataFrame(cm_ner, index=svm_model_ner.classes_, columns=svm_model_ner.classes_)
sns.heatmap(confusion_df_ner, annot=True, cmap='YlGnBu')
plt.xlabel('Tahmini Niyet (NER ile)')
plt.ylabel('Gerçek Niyet')
plt.show()


# SVM ile modeli egitme, ve dogruluk oralari