import sqlite3

conn = sqlite3.connect(r'.\NF3.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE "Nachname" (
	"Nachname"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Nachname")
)""")

cur.execute("""INSERT INTO Nachname (`Nachname`) VALUES
('Muster'),
('Foerster'),
('Mayer'),
('Beckmann'),
('Mueller'),
('Becker'),
('Baumann'),
('Schaefer'),
('Koehler'),
('Metzger')""")
conn.commit()

cur.execute("""CREATE TABLE "Vorname" (
	"Vorname"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Vorname")
)""")

cur.execute("""INSERT INTO Vorname (`Vorname`) VALUES
('Anton'),
('Franz'),
('Frank'),
('Christine'),
('Christoph'),
('Anne'),
('Stephan'),
('Stefan'),
('Friederike'),
('Karl'),
('Heinz'),
('Heinrich')""")
conn.commit()

cur.execute("""CREATE TABLE "Datum" (
	"Datum"	TEXT NOT NULL,
	PRIMARY KEY("Datum")
)""")

cur.execute("""INSERT INTO Datum (`Datum`) VALUES
('1955-03-12'),
('1955-11-21'),
('1957-07-06'),
('1984-09-28'),
('1987-02-25'),
('1990-07-05'),
('1991-10-13'),
('1992-07-02'),
('1993-01-01'),
('1994-10-10')""")
conn.commit()

cur.execute("""CREATE TABLE "Land" (
	"Land"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Land")
)""")

cur.execute("""INSERT INTO Land (`Land`) VALUES
('Germany'),
('England'),
('France'),
('China'),
('USA'),
('Canada'),
('Russland'),
('Indien'),
('Brasilien')""")
conn.commit()

cur.execute("""CREATE TABLE "Strasse" (
	"Strassenname"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Strassenname")
)""")

cur.execute("""INSERT INTO Strasse (`Strassenname`) VALUES
('Broadway'),
('Kudamm'),
('Muenchener Strasse'),
('Berliner Strasse'),
('Uferstrasse'),
('Hauptstrasse'),
('Untere Starsse'),
('Bahnhof Strasse'),
('Poststrasse'),
('Highway')""")
conn.commit()

cur.execute("""CREATE TABLE "Hausnummer" (
	"Nummer"	INTEGER NOT NULL,
	"Zusatz"	TEXT,
	PRIMARY KEY("Nummer")
)""")

cur.execute("""INSERT INTO Hausnummer (`Nummer`, `Zusatz`) VALUES
('1', null),
('2', null),
('3', null),
('11', null),
('23', null),
('45', 'Hinterhaus'),
('56', null),
('67', null),
('130', null),
('145', '3. OG')""")
conn.commit()

cur.execute("""CREATE TABLE "Adresse" (
	"Adresse_ID"	INTEGER NOT NULL,
	"Land"	TEXT NOT NULL,
	"Code"	INTEGER NOT NULL,
	"Ort"	TEXT NOT NULL,
	"Strasse"	TEXT NOT NULL,
	"Hausnummer"	INTEGER NOT NULL,
	PRIMARY KEY("Adresse_ID"),
	FOREIGN KEY("Land") REFERENCES "Land",
	FOREIGN KEY("Strasse") REFERENCES "Strasse",
	FOREIGN KEY("Hausnummer") REFERENCES "Hausnummer",
	FOREIGN KEY("Ort") REFERENCES "Ort"
)""")

cur.execute("""CREATE TABLE "Person" (
	"Person_ID"	INTEGER,
	"Nachname"	TEXT NOT NULL,
	"Vorname"	TEXT NOT NULL,
	"Geburtstag"	TEXT NOT NULL,
	"Geburtsort"	TEXT NOT NULL,
	"Geburtsland"	TEXT NOT NULL,
	"Adresse"	INTEGER,
	PRIMARY KEY("Person_ID"),
	FOREIGN KEY("Vorname") REFERENCES "Vorname",
	FOREIGN KEY("Geburtstag") REFERENCES "Datum",
	FOREIGN KEY("Adresse") REFERENCES "Adresse"("Adresse_ID"),
	FOREIGN KEY("Nachname") REFERENCES "Nachname"
)""")
conn.commit()
conn.close()
