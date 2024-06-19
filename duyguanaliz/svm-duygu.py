import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Veri setlerini okuma
egitim_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Egitim-3972-4.xlsx')
test_veri_seti = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test3-1000.xlsx')

# NER sütunlarını al
egitim_nerler = egitim_veri_seti['NER'].values.reshape(-1, 1)
test_nerler = test_veri_seti['NER'].values.reshape(-1, 1)

# Etiketleri tanımlama
y_train = egitim_veri_seti['INTENT']
y_test = test_veri_seti['INTENT']

# Modeli oluşturma ve eğitme
svm_model = SVC(kernel='linear')
svm_model.fit(egitim_nerler, y_train)

# Tahmin yapma
y_pred = svm_model.predict(test_nerler)

# Doğruluk hesaplama
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")

# Sınıflandırma raporu
print(classification_report(y_test, y_pred, zero_division=1))
