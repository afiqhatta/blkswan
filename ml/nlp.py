import spacy

nlp = spacy.load('en')


class Document:
    def __init__(self, text):
        self.text = text
        self.entities = []
        self.doc = nlp(text)

    def print_entities(self):
        for ent in self.doc.ents:
            print(ent.text)

    def get_entities(self):
        for ent in self.doc.ents:
            self.entities.append(ent)


