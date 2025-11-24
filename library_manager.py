import json
import os

SAVE_FILE = "library_data.json"

class LibraryManager:
    def __init__(self):
        self.data = {
            "borrowedBooks": {}   # bookName : username
        }
        self.load()

    def load(self):
        print("Loading library data...")
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except:
                print("Eroare la incarcarea JSON-ului")
                self.save()
        else:
            self.save()

    def save(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    # ------------------------------------------------------------
    # VERIFICĂ DISPONIBILITATEA GLOBALĂ
    # ------------------------------------------------------------
    def isBorrowed(self, bookName):
        return bookName in self.data["borrowedBooks"]

    def whoBorrowed(self, bookName):
        return self.data["borrowedBooks"].get(bookName, None)

    # ------------------------------------------------------------
    # ÎMPRUMUTĂ O CARTE GLOBAL
    # ------------------------------------------------------------
    def borrowBook(self, username, bookName):
        if self.isBorrowed(bookName):
            return False  # deja împrumutată

        self.data["borrowedBooks"][bookName] = username
        self.save()
        return True

    # ------------------------------------------------------------
    # RETURNARE GLOBALĂ
    # ------------------------------------------------------------
    def returnBook(self, username, bookName):
        if self.whoBorrowed(bookName) == username:
            del self.data["borrowedBooks"][bookName]
            self.save()
            return True
        return False

    # ------------------------------------------------------------
    # CĂRȚILE UNUI USER
    # ------------------------------------------------------------
    def getUserBooks(self, username):
        return [
            book for book, user in self.data["borrowedBooks"].items()
            if user == username
        ]
