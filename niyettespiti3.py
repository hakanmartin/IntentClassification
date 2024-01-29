import spacy
from spacy.matcher import Matcher
import pandas as pd
from fuzzywuzzy import fuzz

# Excel dosyasını oku
df = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/Niyet-Pattern.xlsx')

nlp = spacy.load("tr_core_news_md")
matcher = Matcher(nlp.vocab)

# Her bir niyet için verileri al ve Matcher'a ekle
for col in df.columns:
    patterns = df[col].dropna().tolist()  # NaN olmayan değerleri al
    intent = col
    for pattern in patterns:
        matcher.add(intent, [[{"LOWER": word.lower()} for word in pattern.split()]])  # Pattern'i Matcher'a ekle

while True:
    # Kullanıcıdan giriş iste
    user_input = input("Metin: ")

    if user_input.lower() == 'q':
        break  # 'q' girilirse döngüden çık

    # Giriş metnini analiz et
    doc = nlp(user_input)

    # Matcher'ı kullanarak niyetleri tespit et
    matches = matcher(doc)

    if matches:
        detected_intents = set()
        for match_id, start, end in matches:
            detected_intents.add(nlp.vocab.strings[match_id])
        print("Niyet:", '#'.join(detected_intents))
        print()
    else:
        highest_similarity = 0.7
        best_match_intent = None
        for token in doc:
            # Her bir token için patternlerle karşılaştırma
            for col in df.columns:
                patterns = df[col].dropna().tolist()
                for pattern in patterns:
                    similarity_ratio = fuzz.ratio(token.lower_, pattern.lower())
                    if similarity_ratio > highest_similarity:
                        highest_similarity = similarity_ratio
                        best_match_intent = col

        if best_match_intent:
            print(f"Yakın eşleşme bulundu. Niyet: {best_match_intent}")
            print()
        else:
            print("Niyet: Niyet bulunamadı :(")
            print()
