import sqlite3
import csv

# Connexion à la base
conn = sqlite3.connect('ventes.db')
cursor = conn.cursor()

# Création de la table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventes (
   id_vente INTEGER PRIMARY KEY, 
   id_client INTEGER,
   id_produit INTEGER,
   quantite INTEGER,
   date_achat TEXT,
   FOREIGN KEY (id_client) REFERENCES clients(id_client),
   FOREIGN KEY (id_produit) REFERENCES produits(id_produit)
)
''')

# Lecture du fichier CSV et insertion des données
with open('ventes.csv', 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Ignorer la première ligne (entêtes)

    for row in csv_reader:
        cursor.execute('''
        INSERT INTO ventes (id_vente, id_client, id_produit, quantite, date_achat)
        VALUES (?, ?, ?, ?, ?)
        ''', row)

# Enregistrer et fermer la connexion
conn.commit()
conn.close()
 
######################################################################################################################################

# Connexion à la base
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Création de la table
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
   id_client INTEGER PRIMARY KEY,
   nom TEXT,
   ville TEXT,
   date_inscription TEXT
)
''')

# Lecture du fichier CSV et insertion des données
with open('clients.csv', 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Ignorer la première ligne (entêtes)

    for row in csv_reader:
        cursor.execute('''
        INSERT INTO clients (id_client, nom, ville, date_inscription)
        VALUES (?, ?, ?, ?)
        ''', row)

# Enregistrer et fermer la connexion
conn.commit()
conn.close()

########################################################################################################################################

######################################################################################################################################

# Connexion à la base
conn = sqlite3.connect('produits.db')
cursor = conn.cursor()

# Création de la table
cursor.execute('''
CREATE TABLE IF NOT EXISTS produits (
   id_produit INTEGER PRIMARY KEY,
   nom TEXT,
   categorie TEXT,
   prix_unitaire INTEGER
)
''')

# Lecture du fichier CSV et insertion des données
with open('produits.csv', 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Ignorer la première ligne (entêtes)

    for row in csv_reader:
        cursor.execute('''
        INSERT INTO produits (id_produit, nom, categorie, prix_unitaire)
        VALUES (?, ?, ?, ?)
        ''', row)

# Enregistrer et fermer la connexion
conn.commit()
conn.close()