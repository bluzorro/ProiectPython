import hashlib
import os
import sqlite3
from datetime import datetime


def initDB():
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print("Initializing Database")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            coverPath TEXT,
            available INTEGER NOT NULL DEFAULT 1
        )
    """)

    # Carti imprumutate

    cur.execute("""
        CREATE TABLE IF NOT EXISTS borrowedBooks
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            book TEXT NOT NULL,
            user TEXT NOT NULL
        )
    """)

    # Users

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)

    # print("DB initialised")

    conn.commit()
    conn.close()


initDB()


def insertInitialBooks(book_list):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    for b in book_list:
        cur.execute("""
            INSERT INTO books (name, author, genre, coverPath, available)
            VALUES (?, ?, ?, ?, ?)
        """, (b.name, b.author, b.genre, b.coverPath, 1))

    conn.commit()
    conn.close()




def loadAvailableBooks():
    # print("Loading available books...")
    from classes import (Carte)
    # print("Imported Carte")
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    cur.execute("SELECT name, author, genre, coverPath FROM books WHERE available = 1")
    rows = cur.fetchall()

    conn.close()

    # print("Am fetchuit toate cartile!")
    # print(rows)

    availableBooks = []
    for (name, author, genre, coverPath) in rows:
        # print(name, author, genre)
        availableBooks.append(Carte(name, author, genre, 200, 300, coverPath))

    # print("Am convertit intr-o lista tot")


    return availableBooks


def isBookAvailable(bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # vedem dacă exista in borrowedBooks
    cur.execute("SELECT 1 FROM borrowedBooks WHERE book = ?", (bookName,))
    row = cur.fetchone()

    conn.close()

    return row is None   # daca nu exista, cartea e disponibila




def borrowBook(username, bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # verificam dacă e deja imprumutata
    cur.execute("SELECT 1 FROM borrowedBooks WHERE book = ?", (bookName,))
    row = cur.fetchone()

    if row is not None:
        conn.close()
        return False  # carte indisponibila

    # altfel o imprumutam
    now = datetime.now()
    formattedNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(formattedNow)  # ex: "2025-02-14 23:59:01"
    cur.execute(
        "INSERT INTO borrowedBooks (book, user, borrowDate) VALUES (?, ?, ?)",
        (bookName, username, formattedNow)
    )

    cur.execute("UPDATE books SET available = 0 WHERE name = ?", (bookName,))

    conn.commit()
    conn.close()
    return True




def returnBook(username, bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # ștergem doar daca user-ul a imprumutat-o
    cur.execute(
        "DELETE FROM borrowedBooks WHERE book = ? AND user = ?",
        (bookName, username)
    )

    cur.execute("UPDATE books SET available = 1 WHERE name = ?", (bookName,))

    changes = conn.total_changes
    conn.commit()
    conn.close()

    return changes > 0   # True daca s-a returnat, False daca nu era imprumutata



def getBorrowedBooks(username):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    cur.execute("SELECT book FROM borrowedBooks WHERE user = ?", (username,))
    rows = cur.fetchall()

    conn.close()

    return [row[0] for row in rows]




