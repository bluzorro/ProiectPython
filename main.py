
from PyQt6.QtCore import Qt

class Carte:
    def __init__(self, name, author, genre, launchYear, pages):
        self.name = name
        self.author = author
        self.genre = genre
        self.launchYear = launchYear
        self.pages = pages


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
        
class Library:

    def addCarte(self, name, author, genre, launchYear, pages):
        carte = Carte(name, author, genre, launchYear, pages)
        listaCarti.append(carte)

    def filterAutor(author):
        # Filtered search dupa author, va afisa doar cartilor scrise de autorul respectiv
        listaCurenta.clear()
        for carte in listaCarti:
            if (author == carte.author):
                listaCurenta.append(carte)

        # Functie display/update display si afiseaza cartile care corespund filtrarii


    def filterGenre(genre):
        listaCurenta.clear()
        for carte in listaCarti:
            if (genre == carte.genre):
                listaCurenta.append(carte)

        # Update display

    def imprumutaCarte(self, carte: Carte):
        # WIP
        return

    def returneazaCarte(self, carte: Carte):
        # WIP
        return


listaCarti = [
    Carte("Poor Folk", "Fyodor Dostoyevsky", "Fiction", 1846, 271),
    Carte("White Nights", "Fyodor Dostoyevsky", "Fiction", 1848, 120),
    Carte("Crime and Punishment", "Fyodor Dostoyevsky", "Fiction", 1866, 671),
    Carte("The Gambler", "Fyodor Dostoyevsky", "Fiction", 1867, 210),
    Carte("The Idiot", "Fyodor Dostoyevsky", "Fiction", 1869, 656),

]  # de introdus sau fetch-ed

listaCurenta = [] # cartile ce vor fi afisate dupa search / filter

# Concept menu screen

print("~-~-~-~-~-~-~-~-~-~-~-~")
print(" Bibliotheca Virtualis ")
print("~-~-~-~-~-~-~-~-~-~-~-~\n")

print("Cu ce te putem ajuta?\n")



from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import sys

app = QApplication(sys.argv)
window = QWidget()
# window.setFixedSize(800, 640)
window.setWindowTitle("Bibliotheca Virtualis")

window.setStyleSheet("""
    QWidget {
        background-color: rgb(50, 50, 100);
    }
    
    QLabel { 
        color: white;
        font-size: 24px;
        margin: 0px;
        padding: 0px;
        font-weight: bold;
    }
    
    QLabel[role="separator"] {
        font-size: 24px;
        margin: 5px;
        padding: 0px;
    }
    
    QPushButton {
        background-position: bottom center;
        background-color: rgb(70, 70, 150);
        color: white;
        font-size: 16px;
        margin-bottom: 20px;
        min-width: 100px;
        max-width: 200px;
        padding: 5px;
        font-family: sans-serif;
        border-radius: 0px;
    }
    
    QPushButton:hover {
        background-color: rgb(40, 40, 80);
    }
""")

layout = QVBoxLayout()

firstSep = QLabel("~-~-~-~-~-~-~-~-~-~-~-~")
firstSep.setProperty("role", "separator")
# firstSep.setAlignment(Qt.AlignmentFlag.AlignHCenter)
layout.addWidget(firstSep)

title = QLabel("Bibliotheca Virtualis")
# title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
layout.addWidget(title)

secondSep = QLabel("~-~-~-~-~-~-~-~-~-~-~-~")
secondSep.setProperty("role", "separator")
# secondSep.setAlignment(Qt.AlignmentFlag.AlignHCenter)
layout.addWidget(secondSep)

button = QPushButton("Login")
layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)

window.setLayout(layout)
window.show()
sys.exit(app.exec())


# while (1):
