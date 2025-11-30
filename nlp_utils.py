import spacy
nlp = spacy.load("en_core_web_md")

def extract_keywords(text, top_n=10):
    doc = nlp(text)
    # Extract nouns and proper nouns as potential keywords
    keywords = [chunk.text for chunk in doc.noun_chunks if len(chunk.text) > 2]
    keywords = list(dict.fromkeys(keywords))
      # Remove duplicates
    return keywords[:top_n]