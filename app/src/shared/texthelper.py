import spacy
from spacy.cli import download

try:
    nlp = spacy.load('en_core_web_md')
except OSError:
    download('en_core_web_md')
    nlp = spacy.load('en_core_web_md')


def score_documents(query, docs):
    if type(query) == str and len(query) > 3:
        question = nlp(query)
    else:
        return []

    for d in docs:
        d['score'] = question.similarity(nlp(d['title']))
    return sorted(docs, key=lambda d: d['score'], reverse=True)