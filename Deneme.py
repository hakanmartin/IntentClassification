import pandas as pd
import nltk
from tqdm import tqdm
from nltk import word_tokenize, pos_tag, ne_chunk

try:
    df = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test-1000.xlsx')
except FileNotFoundError:
    print("Dosya bulunamadı!")
    exit()

pbar = tqdm(total=len(df), desc="İşleniyor")


def entity_recognition_nltk(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    named_entities = ne_chunk(tagged_words)
    entities = []
    for entity in named_entities:
        if hasattr(entity, 'label'):
            entities.append(entity.label())
    return entities


# 'TR' kolonundaki her bir cümle için varlık tanıması yapma
for index, text in enumerate(df['TR']):
    if isinstance(text, str):  # Eğer cümle bir string ise işlem yap
        entities = entity_recognition_nltk(text)
        if entities:
            df.at[index, 'NER'] = ', '.join(entities)
    else:
        df.at[index, 'NER'] = ''  # Eğer cümle boş ise boş string ata


    if index % 100 == 0:
        pbar.update(100)

pbar.close()

# Sonucu yeni bir Excel dosyasına yazma
df.to_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Test-1000.xlsx', index=False)
print("Varlık tanıması tamamlandı ve kaydedildi.")
