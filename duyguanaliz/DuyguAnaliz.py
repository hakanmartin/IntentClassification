import pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import warnings

# Uyarıları sessize alma
warnings.filterwarnings("ignore", category=FutureWarning)

try:
    df = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test3-1000.xlsx')
except FileNotFoundError:
    print("Dosya bulunamadı!")
    exit()

pbar = tqdm(total=len(df), desc="İşleniyor")

# Model ve tokenizer'ı yükle
model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def sentiment_analysis(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    scores = outputs.logits[0].detach().numpy()
    scores = torch.nn.functional.softmax(torch.tensor(scores), dim=0)
    labels = ['Negative', 'Neutral', 'Positive']
    sentiment = labels[scores.argmax()]

    # Sentimenti rakamlarla temsil et
    sentiment_mapping = {'Neutral': 1, 'Positive': 2, 'Negative': 3}
    return sentiment_mapping[sentiment]


# 'TR' kolonundaki her bir cümle için duygu analizi yapma
for index, text in enumerate(df['TR']):
    if isinstance(text, str):  # Eğer cümle bir string ise işlem yap
        sentiment = sentiment_analysis(text)
        df.at[index, 'DA'] = sentiment
    else:
        df.at[index, 'DA'] = np.nan  # Eğer cümle boş ise NaN ata

    pbar.update(1)

pbar.close()

# Sonucu yeni bir Excel dosyasına yazma
df.to_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test3-1000.xlsx', index=False)
print("Duygu analizi tamamlandı ve kaydedildi.")

# duygu analizi yapar, DA kolonuna 1, 2, ya da 3 yazarr.