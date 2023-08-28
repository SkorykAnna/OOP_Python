class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = {}

    def add_document(self, doc_id, document):
        self.ndoc += 1
        self.production[doc_id] = document

    def get_document_ids(self):
        return list(self.production.keys())
