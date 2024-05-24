import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Veriyi okuyun ve modeli eğitin
veri_seti = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/ProjeVeriSetiEn_TR.xlsx')
metinler = veri_seti['TR'].values.astype('U')
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)
X = tfidf_vectors
y = veri_seti['INTENT']
svm_model = SVC(kernel='linear')
svm_model.fit(X, y)


def process_user_input_svm(user_input):
    transformed_input = tfidf_vectorizer.transform([user_input])
    predicted_intent = svm_model.predict(transformed_input)
    return predicted_intent[0]  # Tek bir değer döndürmek için
