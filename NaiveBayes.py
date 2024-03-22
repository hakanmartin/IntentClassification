import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Proje1.2VeriSetiEn _TR.xlsx')

metinler = veri_seti['TR'].values.astype('U')

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)

X = tfidf_vectors
y = veri_seti['INTENT']

nb_model = MultinomialNB()
nb_model.fit(X, y)

while True:
    user_input = input("Metin: ")

    if user_input.lower() == 'q':
        break

    transformed_input = tfidf_vectorizer.transform([user_input])

    predicted_intent = nb_model.predict(transformed_input)

    if predicted_intent[0] in veri_seti['INTENT'].unique():
        print(f"Niyet Tahmini (Naive Bayes): {predicted_intent[0]}")
    else:
        print("Niyet bulunamadı.")
