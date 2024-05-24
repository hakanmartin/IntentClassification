import pandas as pd
import spacy
import numpy as np
from tqdm import tqdm

# Türkçe modelini yükle
nlp = spacy.load("tr_core_news_md")

# Veriyi oku
try:
    df = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000-4.xlsx')
except FileNotFoundError:
    print("Dosya bulunamadı!")
    exit()

# İlerleme çubuğu oluştur
pbar = tqdm(total=len(df), desc="İşleniyor")

# 'TR' kolonundaki her bir cümle için varlık tanıması yap
for index, text in enumerate(df['TR']):
    if not pd.isna(text):  # Eğer cümle boş değilse işlem yap
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            df.at[index, 'NER'] = 1
        else:
            df.at[index, 'NER'] = 0
    else:
        df.at[index, 'NER'] = np.nan
    pbar.update(1)

# İlerleme çubuğunu kapat
pbar.close()

# Sonucu yeni bir Excel dosyasına yaz
df.to_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000-4.xlsx', index=False)
print("Varlık tanıması tamamlandı ve sonuçlar kaydedildi.")
# spacy ile varlik tanimlama