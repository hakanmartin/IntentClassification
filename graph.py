import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from tqdm import tqdm

# Excel dosyasını oku ve bir DataFrame'e yükle
veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/ProjeVeriSetiEn_TR.xlsx')

metinler = veri_seti['TR'].values.astype('U')

# TF-IDF vektörleştiriciyi tanımlayın ve uygulayın
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(metinler)

X = tfidf_vectors
y = veri_seti['INTENT']

# Farklı random_state değerleri için doğrulukları saklayacak boş bir liste oluşturma
accuracies = []

random_states = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

for random_state in tqdm(random_states, desc="Grafik Oluşturuluyor:", ncols=90, colour='blue'):
    # Eğitim ve test veri setlerine ayırma
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    # Support Vector Machine modeli oluşturma ve eğitme
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)

    # Test veri seti üzerinde tahmin yapma
    y_pred = svm_model.predict(X_test)

    # Model performansını değerlendirme ve doğrulukları listeye ekleme
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Doğrulukları görselleştirme
plt.plot(random_states, accuracies, marker='o')
plt.title('Random State Değerlerine Göre Model Doğruluğu')
plt.xlabel('Random State')
plt.ylabel('Doğruluk')
plt.xticks(random_states)
plt.grid(True)
plt.show()
