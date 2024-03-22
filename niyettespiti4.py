import spacy
from spacy.matcher import Matcher
import pandas as pd
from fuzzywuzzy import fuzz


def process_user_input(user_input):
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

    final_intent = "-1"  # Başlangıçta varsayılan olarak "Niyet bulunamadı"

    doc = nlp(user_input)

    matches = matcher(doc)

    if matches:
        detected_intents = set()
        for match_id, start, end in matches:
            detected_intents.add(nlp.vocab.strings[match_id])
        final_intent = '#'.join(detected_intents)
    elif final_intent == "-1":  # Eğer daha önce bir niyet bulunmamışsa
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
        elif final_intent == "-1":  # Eğer daha önce bir niyet bulunmamışsa
            found_time_entity = any(token.ent_type_ == "TIME" for token in doc)
            found_city_entity = any(token.ent_type_ == "GPE" for token in doc)

            if found_time_entity:
                final_intent = "atis_flight_time"
            elif found_city_entity:
                final_intent = "atis_city"

    return final_intent

if __name__ == '__main__':
    process_user_input()
