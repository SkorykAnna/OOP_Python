class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.type = "Document"

    def getType(self):
        return self.type

class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, comment_count):
        super().__init__(titre, auteur, date, url, texte)
        self.comment_count = comment_count
        self.type = "RedditDocument"

    def __str__(self):
        return f"Reddit Document\nTitle: {self.titre}\nAuthor: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}\nComment Count: {self.comment_count}"

class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, auteurs[0], date, url, texte)
        self.auteurs = auteurs
        self.type = "ArxivDocument"

    def __str__(self):
        return f"Arxiv Document\nTitle: {self.titre}\nAuthors: {', '.join(self.auteurs)}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}"
