class Author:
    def __init__(self, name):
        self.name = name
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def display_documents(self):
        print(f"Author: {self.name}")
        for doc in self.documents:
            doc.display_info()
            print()

    def __repr__(self):
        return f"Author: {self.name}, Documents: {len(self.documents)}"
