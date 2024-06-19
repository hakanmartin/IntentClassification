import spacy
from spacy.matcher import Matcher
import pandas as pd
from fuzzywuzzy import fuzz

# Excel dosyasını oku
df = pd.read_excel('/Users/hakanmartin/PycharmProjects/pythonProject1/1Donem/Niyet-Pattern.xlsx')

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

    final_intent = "-1"  # Başlangıçta varsayılan olarak "Niyet bulunamadı"

    # Giriş metnini analiz et
    doc = nlp(user_input)

    # Matcher'ı kullanarak niyetleri tespit et
    matches = matcher(doc)

    if matches:
        detected_intents = set()
        for match_id, start, end in matches:
            detected_intents.add(nlp.vocab.strings[match_id])
        final_intent = '#'.join(detected_intents)
    else:
        highest_similarity = 0.7
        best_match_intent = None

        # FuzzyWuzzy ile benzerlik kontrolü
        for token in doc:
            for col in df.columns:
                patterns = df[col].dropna().tolist()
                for pattern in patterns:
                    similarity_ratio = fuzz.ratio(token.lower_, pattern.lower())
                    if similarity_ratio > highest_similarity:
                        highest_similarity = similarity_ratio
                        best_match_intent = col

        if best_match_intent:
            final_intent = best_match_intent
        else:
            found_time_entity = any(token.ent_type_ == "TIME" for token in doc)
            found_city_entity = any(token.ent_type_ == "GPE" for token in doc)

            if found_time_entity:
                final_intent = "atis_flight_time"
            elif found_city_entity:
                final_intent = "atis_city"

    print(f"Niyet: {final_intent}")
    print()
