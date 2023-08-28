import re

class Corpus:
    def __init__(self):
        self.text = ""

    def add_document(self, document):
        self.text += document

    def search(self, keyword):
        passages = re.findall(r'\b' + keyword + r'\b', self.text)
        return passages
