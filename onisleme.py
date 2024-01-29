import spacy

# Türkçe modelini yükle
nlp = spacy.load("tr_core_news_md")

# Metni işle
text = "saat 6' dan sonra baltimore' a tüm uçuşlar"
doc = nlp(text)

# Tokenization
formatted_tokens = [f"[{token.text}]" for token in doc]
# Tokenleri tek bir satırda virgülle ayrılmış olarak yazdır
print(",".join(formatted_tokens))

# Lemmatization
print("\nLemmatization:")
for token in doc:
    print(token.text, token.lemma_)

# Cümle analizi
print("\nCümleler:")
for sent in doc.sents:
    print(sent.text)

# Named Entity Recognition (NER)
print("\nNamed Entity Recognition (NER):")
for ent in doc.ents:
    print(ent.text, ent.label_)
