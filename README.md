## Crypto Tools

**Crypto Tools** is een verzameling van twee eenvoudige Python command-line applicaties die draaien om versleuteling en beveiliging van tekst en wachtwoorden.
De scripts zijn ontwikkeld als oefening in het toepassen van functies, loops, inputvalidatie en datastructuren binnen Python.

### Inhoud van de repo

#### 1. Caesar Cipher (`caesar_cipher.py`)

Een klassieke encryptietool waarmee je tekst kunt versleutelen en ontsleutelen met behulp van een zelfgekozen shift.

Functies:

* Tekst versleutelen volgens het Caesar Cipher-principe
* Tekst ontsleutelen met dezelfde shift
* Interactief menu met gebruikersinvoer
* Volledig uitgevoerd met standaard Python-functionaliteit

Gebruikte concepten:

* Dictionaries voor letter-naar-getal mapping
* For- en while-loops
* Functies en conditionele statements
* Stringmanipulatie

---

#### 2. Wachtwoord Generator (`wachtwoord_generator.py`)

Een interactieve CLI-tool om willekeurige wachtwoorden te genereren en tijdelijk te beheren.

Functies:

* Willekeurige wachtwoorden genereren van 1–64 karakters
* Wachtwoorden koppelen aan applicatienamen
* Opgeslagen wachtwoorden bekijken, opzoeken en verwijderen
* Alle wachtwoorden tegelijk wissen
* Schone interface via automatische schermverversing

Gebruikte concepten:

* Lijsten en dictionaries voor databeheer
* Functies en inputvalidatie
* Gebruik van `random`, `os` en `platform` modules
* Heldere CLI met gestructureerde menu’s

---

### Vereisten

* **Python 3.x**
* Geen externe libraries nodig

### Over dit project

Deze twee tools zijn ontwikkeld binnen de module *Programming Fundamentals* van de NOVI Hogeschool bootcamp.
Het doel van de opdracht was om zelfstandig CLI-tools te bouwen die gebruikmaken van logica, datastructuren en herbruikbare functies.
