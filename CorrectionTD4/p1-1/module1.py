#1.1
    # Was created .py document that we have in same folder/directory ("Document.py" file) wich includes:
 #class Document:
 #    def __init__(self, titre, auteur, date, url, texte):
  #       self.titre = titre
  #       self.auteur = auteur
 #        self.date = date
 #        self.url = url
 #        self.texte = texte

    #To add sth to file Document we can do this way (below code) or go to 1.2
from Document import Document

doc = Document(
     "Logistics Coordination Based on Inventory Management and Transportation Planning by Third-Party Logistics (3PL)",
     "Mariusz Kmiecik",
     "4 July 2022",
     "https://www.mdpi.com/2071-1050/14/13/8134",
     "Currently, there is still a strong trend in research and in the market connected with the role of 3PL (third-party logistics) companies and the trend of developing and creating coordination in logistics networks."
)
