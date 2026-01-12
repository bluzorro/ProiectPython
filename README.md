# 📚 Bibliotheca Virtualis

**Bibliotheca Virtualis** este o aplicație desktop realizată în **Python + PyQt6**, care simulează funcționarea unei biblioteci virtuale. Utilizatorii se pot autentifica, pot căuta cărți, le pot împrumuta sau returna, iar starea bibliotecii este sincronizată global pentru toți utilizatorii.

---

## ✨ Funcționalități

- 🔐 **Autentificare utilizator**
  - Login pe bază de username și parolă
  - Datele utilizatorilor sunt stocate într-o bază de date SQLite

- 📖 **Bibliotecă de cărți**
  - Vizualizarea tuturor cărților disponibile
  - Căutare în timp real după titlu, autor sau gen
  - Filtrare după gen și autor

- 📚 **Împrumut & Returnare**
  - Un utilizator poate împrumuta o carte (un singur exemplar per carte)
  - O carte împrumutată nu mai apare ca disponibilă pentru alți utilizatori
  - Returnarea cărților actualizează instant biblioteca

- 👤 **Cartile mele**
  - Fiecare utilizator poate vedea lista cărților împrumutate
  - Afișarea timpului scurs de la împrumut (ex: „împrumutată acum 2 zile”)

- 🛠️ **Admin Panel**
  - Tab special pentru administrator
  - Vizualizarea tuturor cărților împrumutate de toți utilizatorii
  - Posibilitatea de a returna manual orice carte

- 💾 **Persistența datelor**
  - Aplicația folosește **SQLite**
  - Starea bibliotecii este salvată între sesiuni

---

## 🧱 Tehnologii folosite

- **Python 3**
- **PyQt6** – interfață grafică
- **SQLite3** – bază de date locală
- **Qt Stylesheets (QSS)** – stilizare UI

---

## ▶️ Rulare aplicație

1. Clonează repository-ul:
   ```bash
   git clone https://github.com/bluzorro/ProiectPython.git
   ```

2. Instalează dependențele:
   ```bash
   pip install PyQt6
   ```

3. Rulează aplicația:
   ```bash
   python main.py
   ```
