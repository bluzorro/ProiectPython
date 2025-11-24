import sys
from library_manager import LibraryManager
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QGridLayout, QScrollArea, QHBoxLayout, QComboBox, QTabWidget, QSizePolicy
)


class Carte:
    def __init__(self, name, author, genre, launchYear, pages, coverPath):
        self.name = name
        self.author = author
        self.genre = genre
        self.launchYear = launchYear
        self.pages = pages
        self.coverPath = coverPath


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Library:

    def addCarte(self, carte: Carte):
        # carte = Carte(name, author, genre, launchYear, pages)
        listaCarti.append(carte)

    def filterAutor(self, author):
        # Filtered search dupa author, va afisa doar cartilor scrise de autorul respectiv
        listaCurenta.clear()
        for carte in listaCarti:
            if author == carte.author:
                listaCurenta.append(carte)

        # Functie display/update display si afiseaza cartile care corespund filtrarii

    def filterGenre(self, genre):
        listaCurenta.clear()
        for carte in listaCarti:
            if genre == carte.genre:
                listaCurenta.append(carte)

        # Update display

    def imprumutaCarte(self, carte: Carte):
        # WIP
        return

    def returneazaCarte(self, carte: Carte):
        # WIP
        return




listaCarti = [
    Carte("Poor Folk", "Fyodor Dostoyevsky", "Fiction", 1846, 271,
          "https://covers.openlibrary.org/b/title/Poor%20Folk-L.jpg"),

    Carte("White Nights", "Fyodor Dostoyevsky", "Fiction", 1848, 120,
          "https://covers.openlibrary.org/b/title/White%20Nights-L.jpg"),

    Carte("Crime and Punishment", "Fyodor Dostoyevsky", "Fiction", 1866, 671,
          "https://covers.openlibrary.org/b/title/Crime%20and%20Punishment-L.jpg"),

    Carte("The Gambler", "Fyodor Dostoyevsky", "Fiction", 1867, 210,
          "https://covers.openlibrary.org/b/title/The%20Gambler-L.jpg"),

    Carte("The Idiot", "Fyodor Dostoyevsky", "Fiction", 1869, 656,
          "https://covers.openlibrary.org/b/title/The%20Idiot-L.jpg"),

    Carte("Demons", "Fyodor Dostoyevsky", "Political Fiction", 1872, 768,
          "https://covers.openlibrary.org/b/title/Demons-L.jpg"),

    Carte("The Brothers Karamazov", "Fyodor Dostoyevsky", "Philosophical Fiction", 1880, 824,
          "https://covers.openlibrary.org/b/title/The%20Brothers%20Karamazov-L.jpg"),

    Carte("War and Peace", "Leo Tolstoy", "Historical Fiction", 1869, 1225,
          "https://covers.openlibrary.org/b/title/War%20and%20Peace-L.jpg"),

    Carte("Anna Karenina", "Leo Tolstoy", "Fiction", 1877, 864,
          "https://covers.openlibrary.org/b/title/Anna%20Karenina-L.jpg"),

    Carte("The Death of Ivan Ilyich", "Leo Tolstoy", "Fiction", 1886, 86,
          "https://covers.openlibrary.org/b/title/The%20Death%20of%20Ivan%20Ilyich-L.jpg"),

    Carte("The Master and Margarita", "Mikhail Bulgakov", "Fantasy", 1967, 480,
          "https://covers.openlibrary.org/b/title/The%20Master%20and%20Margarita-L.jpg"),

    Carte("Dead Souls", "Nikolai Gogol", "Satire", 1842, 432,
          "https://covers.openlibrary.org/b/title/Dead%20Souls-L.jpg"),

    Carte("Fathers and Sons", "Ivan Turgenev", "Fiction", 1862, 244,
          "https://covers.openlibrary.org/b/title/Fathers%20and%20Sons-L.jpg"),

    Carte("1984", "George Orwell", "Dystopian", 1949, 328,
          "https://covers.openlibrary.org/b/title/1984-L.jpg"),

    Carte("Animal Farm", "George Orwell", "Political Satire", 1945, 112,
          "https://covers.openlibrary.org/b/title/Animal%20Farm-L.jpg"),

    Carte("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 281,
          "https://covers.openlibrary.org/b/title/To%20Kill%20a%20Mockingbird-L.jpg"),

    Carte("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 180,
          "https://covers.openlibrary.org/b/title/The%20Great%20Gatsby-L.jpg"),

    Carte("Lord of the Flies", "William Golding", "Allegorical Fiction", 1954, 224,
          "https://covers.openlibrary.org/b/title/Lord%20of%20the%20Flies-L.jpg"),

    Carte("Brave New World", "Aldous Huxley", "Dystopian", 1932, 268,
          "https://covers.openlibrary.org/b/title/Brave%20New%20World-L.jpg"),

    Carte("Dune", "Frank Herbert", "Science Fiction", 1965, 412,
          "https://covers.openlibrary.org/b/title/Dune-L.jpg"),

    Carte("Foundation", "Isaac Asimov", "Science Fiction", 1951, 255,
          "https://covers.openlibrary.org/b/title/Foundation-L.jpg"),

    Carte("Neuromancer", "William Gibson", "Cyberpunk", 1984, 271,
          "https://covers.openlibrary.org/b/title/Neuromancer-L.jpg"),

    Carte("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction", 1979, 224,
          "https://covers.openlibrary.org/b/title/The%20Hitchhiker%27s%20Guide%20to%20the%20Galaxy-L.jpg"),

    Carte("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 310,
          "https://covers.openlibrary.org/b/title/The%20Hobbit-L.jpg"),

    Carte("The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy", 1954, 423,
          "https://covers.openlibrary.org/b/title/The%20Fellowship%20of%20the%20Ring-L.jpg"),

    Carte("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 332,
          "https://covers.openlibrary.org/b/title/Harry%20Potter%20and%20the%20Philosopher%27s%20Stone-L.jpg"),

    Carte("Dracula", "Bram Stoker", "Horror", 1897, 418,
          "https://covers.openlibrary.org/b/title/Dracula-L.jpg"),

    Carte("Frankenstein", "Mary Shelley", "Gothic Fiction", 1818, 280,
          "https://covers.openlibrary.org/b/title/Frankenstein-L.jpg"),

    Carte("The Shining", "Stephen King", "Horror", 1977, 447,
          "https://covers.openlibrary.org/b/title/The%20Shining-L.jpg"),

    Carte("Meditations", "Marcus Aurelius", "Philosophy", 180, 256,
          "https://covers.openlibrary.org/b/title/Meditations-L.jpg"),

    Carte("Beyond Good and Evil", "Friedrich Nietzsche", "Philosophy", 1886, 240,
          "https://covers.openlibrary.org/b/title/Beyond%20Good%20and%20Evil-L.jpg"),

    Carte("The Republic", "Plato", "Philosophy", -380, 416,
          "https://covers.openlibrary.org/b/title/The%20Republic-L.jpg"),

    Carte("Sapiens", "Yuval Noah Harari", "History", 2011, 443,
          "https://covers.openlibrary.org/b/title/Sapiens-L.jpg"),

    Carte("Man's Search for Meaning", "Viktor Frankl", "Psychology", 1946, 200,
          "https://covers.openlibrary.org/b/title/Man%27s%20Search%20for%20Meaning-L.jpg"),

    Carte("The Art of War", "Sun Tzu", "Strategy", -500, 112,
          "https://covers.openlibrary.org/b/title/The%20Art%20of%20War-L.jpg"),

    Carte("The Road", "Cormac McCarthy", "Post-Apocalyptic", 2006, 287,
          "https://covers.openlibrary.org/b/title/The%20Road-L.jpg"),

    Carte("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 277,
          "https://covers.openlibrary.org/b/title/The%20Catcher%20in%20the%20Rye-L.jpg")
]

  # de introdus sau fetch-ed

listaCurenta = []  # cartile ce vor fi afisate dupa search / filter


# -------------------------------------------------------------------
#                          MAIN PAGE
# -------------------------------------------------------------------


class MainPage(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Bibliotheca Virtualis")
        self.setWindowIcon(QIcon("appIcon.png"))
        self.setMinimumSize(900, 600)

        self.manager = LibraryManager()
        self.username = username

        # Load in cartile user-ului
        borrowedNames = self.manager.getUserBooks(self.username)

        self.myBooks = [
            c for c in listaCarti
            if c.name in borrowedNames
        ]

        self.allBooks = [c for c in listaCarti if not self.manager.isBorrowed(c.name)]



        # CONTINUTUL PRINCIPAL
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # SEPARATOR SUS
        firstSep = QLabel("~-~-~-~-~-~-~-~-~-~-~")
        firstSep.setProperty("role", "separator")
        firstSep.setFixedHeight(28)  # elimină spațiul excesiv
        layout.addWidget(firstSep)

        # TITLU
        title = QLabel("Bibliotheca Virtualis")
        title.setFixedHeight(35)
        layout.addWidget(title)

        # SEPARATOR JOS
        secondSep = QLabel("~-~-~-~-~-~-~-~-~-~-~")
        secondSep.setProperty("role", "separator")
        secondSep.setFixedHeight(28)
        layout.addWidget(secondSep)

        subtitle = QLabel("Bine ai venit, " + username + "!")
        subtitle.setProperty("role", "subtitle")
        subtitle.setStyleSheet("""
            QLabel {
                color: rgb(180, 180, 255);
                font-size: 20px;
                qproperty-alignment: AlignCenter;
            }
        """)

        layout.addSpacing(50)
        layout.addWidget(subtitle)
        layout.addSpacing(40)

        # ---------- SEARCH + FILTRE ----------
        searchRow = QWidget()
        searchLayout = QHBoxLayout(searchRow)
        searchLayout.setContentsMargins(0, 0, 0, 0)
        searchLayout.setSpacing(10)

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Cauta carte, autor sau gen...")
        self.searchBar.textChanged.connect(self.applyFilters)

        self.genreFilter = QComboBox()
        self.genreFilter.addItem("Toate genurile")
        self.genreFilter.currentIndexChanged.connect(self.applyFilters)

        self.authorFilter = QComboBox()
        self.authorFilter.addItem("Toti autorii")
        self.authorFilter.currentIndexChanged.connect(self.applyFilters)

        searchLayout.addWidget(self.searchBar)
        searchLayout.addWidget(self.genreFilter)
        searchLayout.addWidget(self.authorFilter)

        layout.addWidget(searchRow)
        layout.addSpacing(20)

        # -------------------- TAB WIDGET --------------------
        self.tabs = QTabWidget()
        self.tabs.addTab(QWidget(), "Carti disponibile")
        self.tabs.addTab(QWidget(), "Cartile mele")
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: none;
            }
            
            QTabWidget::tab-bar { alignment: center; }

            
            QTabBar::tab {
                background: rgb(30,30,70);
                color: white;
                min-width: 160px;
                padding: 15px 25px;
                font-size: 18px;    
                border-radius: 4px;         
                margin: 0px 6px;
            }
            
            QTabBar::tab:selected {
                background: rgb(80,80,180);
            }
        """)
        self.tabs.currentChanged.connect(self.onTabChanged)
        layout.addWidget(self.tabs)

        # Grid-ul
        self.gridWidget = QWidget()
        self.grid = QGridLayout(self.gridWidget)
        self.grid.setSpacing(15)
        self.gridWidget.setLayout(self.grid)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("border: none;")

        self.scroll.setWidget(self.gridWidget)

        self.tabs.widget(0).setLayout(QVBoxLayout())
        self.tabs.widget(0).layout().addWidget(self.scroll)

        # --- TAB 1 (My Books) ---
        self.myScroll = QScrollArea()
        self.myScroll.setWidgetResizable(True)
        self.myScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.myScroll.setStyleSheet("border: none;")

        self.myGridWidget = QWidget()
        self.myGrid = QGridLayout(self.myGridWidget)
        self.myGrid.setSpacing(15)

        self.myScroll.setWidget(self.myGridWidget)

        self.tabs.widget(1).setLayout(QVBoxLayout())
        self.tabs.widget(1).layout().addWidget(self.myScroll)

        self.reloadAllBooksGrid(self.allBooks)
        self.populateFilters(listaCarti)

        # Stil general
        self.setStyleSheet("""
            QMainWindow {
                    background-color: rgb(50, 50, 100);
                }

            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
                qproperty-alignment: AlignCenter;
            }

            #BookTitle {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }

            #BookAuthor {
                color: rgb(200, 200, 255);
                font-size: 14px;
            }

            QLabel[role="separator"] {
                font-size: 24px;
                font-weight: normal;
            }

            QLabel[role="subtitle"] {
                font-size: 24px;
                font-weight: normal;
            }

            QPushButton {
                background-color: rgb(70, 70, 150);
                color: white;
                font-size: 18px;
                padding: 8px 15px;
                border-radius: 4px;
                
            }
            
            QPushButton:hover {
                background-color: rgb(80, 80, 180);
            }

            QScrollBar:vertical {
                background: transparent;
                width: 10px;
                margin: 0px;
            }

            QScrollBar::handle:vertical {
                background-color: rgb(100, 100, 170);
                min-height: 30px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: rgb(140, 140, 200);
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }




            #BookCard {
                background-color: rgb(40, 40, 90);
                border: 1px solid rgb(80, 80, 150);
                border-radius: 6px;
            }


            QLineEdit, QComboBox {
                background-color: rgb(30, 30, 70);
                color: white;
                font-size: 16px;
                padding: 6px 10px;
                border: 1px solid rgb(80, 80, 150);
                border-radius: 4px;
                min-width: 200px;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 20px;
                background: rgb(60, 60, 120);
            }
            
        """)


    def onTabChanged(self, index):
        if index == 0:  # Available Books
            self.reloadAllBooksGrid(self.allBooks)
        elif index == 1:  # My Books
            self.reloadMyBooksGrid()

    def addBooksToGrid(self, bookList, minCardWidth=180):
        # aflam latimea disponibila in viewport
        viewportWidth = self.scroll.viewport().width()

        # luam marginile grid-ului (left + right)
        margins = self.grid.contentsMargins()
        horizMargin = margins.left() + margins.right()

        spacing = self.grid.horizontalSpacing() if self.grid.horizontalSpacing() is not None else self.grid.spacing()


        available = max(1, viewportWidth - horizMargin)

        # calculam câte coloane încap la minCardWidth
        # formula: cols = floor( (available + spacing) / (minCardWidth + spacing) )
        # adaugam spacing la available astfel incat ultima coloana sa nu ceara un spacing suplimentar
        cols = max(1, int((available + spacing) // (minCardWidth + spacing)))

        # calculeaza latimea reala a unui card astfel incat toate sa incapa
        totalSpacing = spacing * (cols - 1)
        cardWidth = max(1, int((available - totalSpacing) / cols))

        row = 0
        col = 0
        for carte in bookList:

            if bookList != self.myBooks:
                card = self.createBookCard(carte)
            else:
                card = self.createBookCard(carte, True)

            card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            card.setMinimumWidth(cardWidth)


            if bookList != self.myBooks:
                self.grid.addWidget(card, row, col)
            else:
                self.myGrid.addWidget(card, row, col)

            col += 1
            if col >= cols:
                col = 0
                row += 1

        # distribuim in mod egal spatiu pe rand
        for c in range(cols):
            self.grid.setColumnStretch(c, 1)



    def createBookCard(self, carte, myBook=False):

        card = QWidget()
        card.setObjectName("BookCard")

        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # --- COVER IMAGE ---
        cover = QLabel()
        cover.setObjectName("CoverLabel")
        # cover.setProperty("role", "cover")
        cover.setFixedSize(140, 200)
        cover.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cover.setText("Cover\n(140x200)")
        cover.setStyleSheet("background-color: rgb(20,20,50); border-radius: 4px; color: rgb(200,200,255);")
        layout.addWidget(cover, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- TITLU ---
        title = QLabel(carte.name)
        title.setStyleSheet("color: white; font-weight: bold; font-size: 16px;")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- AUTOR ---
        author = QLabel(carte.author)
        author.setStyleSheet("color: rgb(200,200,255); font-size: 14px;")
        layout.addWidget(author, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- GEN ---
        genre = QLabel(carte.genre)
        genre.setStyleSheet("color: rgb(160,160,230); font-size: 13px;")
        layout.addWidget(genre, alignment=Qt.AlignmentFlag.AlignCenter)

        if myBook == False:
            btn = QPushButton("Imprumuta")
            # btn.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            btn.clicked.connect(lambda checked, c=carte: self.imprumutaCarte(c))

            layout.addWidget(btn)
        else:
            btn = QPushButton("Returneaza")
            # btn.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            btn.clicked.connect(lambda checked, c=carte: self.returneazaCarte(c))

            layout.addWidget(btn)

        return card



    def populateFilters(self, books):
        genres = set()
        authors = set()

        for c in books:
            genres.add(c.genre)
            authors.add(c.author)

        # sortate frumos
        for g in sorted(genres):
            self.genreFilter.addItem(g)

        for a in sorted(authors):
            self.authorFilter.addItem(a)



    def applyFilters(self):
        search = self.searchBar.text().lower().strip()
        genre = self.genreFilter.currentText()
        author = self.authorFilter.currentText()

        result = []

        for c in self.allBooks:
            ok = True

            # search bar
            if search:
                if (search not in c.name.lower() and
                        search not in c.author.lower() and
                        search not in c.genre.lower()):
                    ok = False

            # filter gen
            if genre != "Toate genurile" and c.genre != genre:
                ok = False

            # filter autor
            if author != "Toti autorii" and c.author != author:
                ok = False

            if ok:
                result.append(c)

        self.reloadAllBooksGrid(result)


    def reloadAllBooksGrid(self, books):
        # stergem cardurile existente

        scrollPos = self.scroll.verticalScrollBar().value()

        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # updatam grid-ul
        self.allBooks.sort(key=lambda b: b.name)
        self.addBooksToGrid(books)
        self.scroll.verticalScrollBar().setValue(scrollPos)

    def reloadMyBooksGrid(self):
        scrollPos = self.scroll.verticalScrollBar().value()

        while self.myGrid.count():
            item = self.myGrid.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        self.myBooks.sort(key=lambda b: b.name)
        self.addBooksToGrid(self.myBooks)
        self.scroll.verticalScrollBar().setValue(scrollPos)


# -------------------------------------------------------------------
#                          LOGIN PAGE
# -------------------------------------------------------------------


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bibliotheca Virtualis – Login")
        self.setWindowIcon(QIcon("appIcon.png"))
        self.setFixedSize(500, 450)

        self.setupUI()
        self.setupStyle()

    def setupUI(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 20, 10, 20)

        # SEPARATOR SUS
        firstSep = QLabel("~-~-~-~-~-~-~-~-~-~-~")
        firstSep.setProperty("role", "separator")
        firstSep.setFixedHeight(28)
        self.layout.addWidget(firstSep)

        # TITLU
        title = QLabel("Bibliotheca Virtualis")
        title.setFixedHeight(35)
        self.layout.addWidget(title)

        # SEPARATOR JOS
        secondSep = QLabel("~-~-~-~-~-~-~-~-~-~-~")
        secondSep.setProperty("role", "separator")
        secondSep.setFixedHeight(28)
        self.layout.addWidget(secondSep)

        # Username
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.layout.addWidget(self.username)

        # Password
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Password")
        self.layout.addWidget(self.password)

        self.layout.addSpacing(20)

        # Login Button
        loginButton = QPushButton("Login")
        loginButton.clicked.connect(self.doLogin)
        self.layout.addWidget(loginButton)

        # self.layout.addStretch(1)

    def setupStyle(self):
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(50, 50, 100);
                font-family: sans-serif;
            }

            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
                qproperty-alignment: AlignCenter;
            }

            QLabel[role="separator"] {
                font-size: 24px;
                font-weight: normal;
            }

            QLineEdit {
                background-color: rgb(30, 30, 70);
                color: white;
                font-size: 16px;
                padding: 6px 10px;
                border: 1px solid rgb(80, 80, 150);
                border-radius: 4px;
                min-width: 250px;
                max-height: 30px;
            }

            QLineEdit:focus {
                border: 1px solid rgb(120, 120, 200);
                background-color: rgb(40, 40, 90);
            }

            QPushButton {
                background-color: rgb(70, 70, 150);
                color: white;
                font-size: 18px;
                padding: 8px 15px;
                border-radius: 4px;
                min-width: 150px;
                margin-top: 10px;
            }

            QPushButton:hover {
                background-color: rgb(80, 80, 180);
            }
        """)

    # -------------------------------
    def doLogin(self):
        userName = self.username.text()
        if (userName == ""):
            return
        self.main = MainPage(userName)
        self.main.show()
        self.close()


# -------------------------------------------------------------------
#                           START APP
# -------------------------------------------------------------------

app = QApplication(sys.argv)
login = LoginPage()
login.show()
sys.exit(app.exec())
