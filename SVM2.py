import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Proje1.2VeriSetiEn _TR.xlsx')

metinler = veri_seti['TR'].values.astype('U')

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)

X = tfidf_vectors
y = veri_seti['INTENT']

svm_model = SVC(kernel='linear')
svm_model.fit(X, y)

while True:
    user_input = input("Metin: ")

    if user_input.lower() == 'q':
        break

    # Gelen metni TF-IDF vektörlerine dönüştür
    transformed_input = tfidf_vectorizer.transform([user_input])

    # SVM modeli ile niyet tahmini yap
    predicted_intent = svm_model.predict(transformed_input)
    print(f"Niyet Tahmini (SVM): {predicted_intent[0]}")