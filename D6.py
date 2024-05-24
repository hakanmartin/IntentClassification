import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore
from nltk import word_tokenize, pos_tag, ne_chunk  # type: ignore
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


try:
    df = pd.read_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000.xlsx')
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
            entities.append(f"{entity.label()} ({' '.join(c[0] for c in entity.leaves())})")
    return entities if entities else ['0']


# 'TR' kolonundaki her bir cümle için varlık tanıması yapma
for index, text in enumerate(df['TR']):
    if isinstance(text, str):  # Eğer cümle bir string ise işlem yap
        entities = entity_recognition_nltk(text)
        df.at[index, 'NER'] = ', '.join(entities)
    else:
        df.at[index, 'NER'] = ''  # Eğer cümle boş ise boş string ata

    if index % 100 == 0:
        pbar.update(100)

pbar.close()

# Sonucu yeni bir Excel dosyasına yazma
df.to_excel('/Users/haticeguler/Desktop/IntentClassification/Test-1000.xlsx', index=False)
print("Varlık tanıması tamamlandı ve kaydedildi.")


# nltk ile varlik tanimlama