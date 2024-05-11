import pandas as pd
import spacy
import numpy as np
from tqdm import tqdm

nlp = spacy.load("tr_core_news_md")

# Veriyi okuma
try:
    df = pd.read_excel('Eğitim-NER.xlsx')
except FileNotFoundError:
    print("Dosya bulunamadı!")
    exit()


pbar = tqdm(total=len(df), desc="İşleniyor")

# 'TR' kolonundaki her bir cümle için varlık tanıması yap
for index, text in enumerate(df['TR']):
    if not pd.isna(text):  # Eğer cümle boş değilse işlem yap
        doc = nlp(text)
        entities = [ent.label_ for ent in doc.ents]  # Sadece varlık etiketlerini al
        if entities:
            df.at[index, 'NER'] = ', '.join(entities)
    else:
        df.at[index, 'NER'] = np.nan  # Eğer cümle boş ise NaN değeri at

    # Her 100 satırda bir ilerleme çubuğunu güncelle
    if index % 100 == 0:
        pbar.update(100)

pbar.close()

# Sonucu yeni bir Excel dosyasına yaz
df.to_excel('Eğitim-NER.xlsx', index=False)
print("Varlık tanıması tamamlandı ve sonuçlar kaydedildi.")
