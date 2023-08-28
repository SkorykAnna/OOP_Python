class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = {}

    def add_document(self, doc_id, document):
        self.production[doc_id] = document
        self.ndoc += 1

    def __str__(self):
        return f"Author: {self.name}\nNumber of Documents: {self.ndoc}"
