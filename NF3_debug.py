# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sqlite3
import numpy as np
import pandas as pd
import time
import ipywidgets as widgets


# %%
conn = sqlite3.connect('Normalform3.db')
cur = conn.cursor()

def tables_in_sqlite_db(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables
    
tabs = tables_in_sqlite_db(conn)
print(tabs)


# %%
# conn.row_factory = sqlite3.Row
# cursor = conn.execute('SELECT * FROM Person')
# # instead of cursor.description:
# row = cursor.fetchone()
# names = row.keys()
# print(names)


# %%
# conn.row_factory = sqlite3.Row
# cursor = conn.execute('SELECT * FROM Adresse')
# # instead of cursor.description:
# row = cursor.fetchone()
# names = row.keys()
# print(names)


# %%
cur.execute("""SELECT * FROM Vorname""")
vornamen = cur.fetchall()
print(vornamen)


# %%
cur.execute("""SELECT * FROM Nachname""")
nachnamen = cur.fetchall()
print(nachnamen)


# %%
cur.execute("""SELECT * FROM Land""")
laender = cur.fetchall()
print(laender)


# %%
cur.execute("""SELECT * FROM Ort""")
orte = cur.fetchall()
print(orte)


# %%
cur.execute("""SELECT * FROM Datum""")
daten = cur.fetchall()
print(daten)


# %%
cur.execute("""SELECT * FROM Strasse""")
strassen = cur.fetchall()
print(strassen)


# %%
cur.execute("""SELECT * FROM Hausnummer""")
hausnummern = cur.fetchall()
print(hausnummern)


# %%
# cur.execute("""SELECT * FROM Adresse""")
# adressen = cur.fetchall()
# print(adressen)


# %%
# print(type(adressen))
# print(type(adressen[0]))

# %% [markdown]
# ## Fülle Adressen ##
# 

# %%
num_adressen = 100_000
print('num_adressen:', num_adressen)
num_laender = len(laender)
print('num_laender:', num_laender)
num_orte = len(orte)
print('num_orte:', num_orte)
num_strassen = len(strassen)
print('num_strassen:', num_strassen)
num_hausnr = len(hausnummern)
print('num_hausnr:', num_hausnr)


# %%
def create_Adresse():
    land = laender[int(np.random.uniform() * num_laender - 0.5)]
    code = int(np.random.uniform() * 100_000 - 0.5)
    ort = orte[int(np.random.uniform() * num_orte - 0.5)]
    strasse = strassen[int(np.random.uniform() * num_strassen - 0.5)]
    hausnr = hausnummern[int(np.random.uniform() * num_hausnr - 0.5)]
    adresse = (str(land[0]), code, str(ort[0]), str(strasse[0]), int(hausnr[0]))
    return adresse


# %%
a = create_Adresse()
print(a)


# %%
# for i in range(num_adressen):
#     adr = create_Adresse()
#     insert = """INSERT INTO Adresse
#         (Land, Code, Ort, Strasse, Hausnummer)
#         VALUES
#         (?, ?, ?, ?, ?);"""
#     cur.execute(insert, adr)

# %% [markdown]
# ## Fülle die Person Tabelle ##
# 

# %%
num_personen = 10_000_000
print('num_personen:', num_personen)
num_nachname = len(nachnamen)
print('num_nachname:', num_nachname)
num_vorname = len(vornamen)
print('num_vorname:', num_vorname)
num_geburtstag = len(daten)
print('num_geburtstag:', num_geburtstag)
num_geburtsort = len(orte)
print('num_geburtsort:', num_geburtsort)
num_geburtsland = len(laender)
print('num_geburtsland:', num_geburtsland)


# %%
def create_Person():
    nachname = nachnamen[int(np.random.uniform() * num_nachname - 0.5)]
    vorname = vornamen[int(np.random.uniform() * num_vorname - 0.5)]
    geburtstag = daten[int(np.random.uniform() * num_geburtstag - 0.5)]
    geburtsort = orte[int(np.random.uniform() * num_geburtsort - 0.5)]
    geburtsland = laender[int(np.random.uniform() * num_laender - 0.5)]
    adresse = int(np.random.uniform() * 100_000 - 0.5)
    person = (str(nachname[0]), str(vorname[0]), str(geburtstag[0]), str(geburtsort[0]), str(geburtsland[0]), adresse)
    return person


# %%
pers = create_Person()
print(pers)


# %%
# for i in range(num_personen):
#     pers = create_Person()
#     insert = """INSERT INTO Person
#         (Nachname, Vorname, Geburtstag, Geburtsort, Geburtsland, Adresse)
#         VALUES
#         (?, ?, ?, ?, ?, ?);"""
#     cur.execute(insert, pers)


# %%
cur.execute("SELECT COUNT(*) FROM Person")
num_person3 = cur.fetchall()
num_pers3 = num_person3[0][0]
print(num_person3[0][0])


# %%
c = conn.execute("SELECT * FROM Person WHERE Person_ID = 1")
row = c.fetchone()
names = row.keys()
print(names)

print()
c = conn.execute("SELECT * FROM Adresse WHERE Adresse_ID = 1")
row = c.fetchone()
names = row.keys()
print(names)

print()
cur.execute("SELECT * FROM Person WHERE Person_ID = 1")
head = cur.fetchall()
print(head)
print(head[0][6])

print()
select = 'SELECT * FROM Adresse WHERE Adresse_ID = ' + str(head[0][6])
print('select:', select)
cur.execute(select)
row = cur.fetchone()
print(row)


# %%
pers2 = head[0]
print(pers2)

adr2 = row
print(adr2)

print()
pers2 = head[0]
print(pers2[1:-1])

adr2 = row
print(adr2[1:])

print()
pers3 = pers2[1:-1] + adr2[1:]
print(pers3)


# %%
conn2 = sqlite3.connect('NF1.db')
cur2 = conn2.cursor()


# %%
# create = """CREATE TABLE "Person" (
# 	"Person_ID"	INTEGER,
# 	"Nachname"	TEXT NOT NULL,
# 	"Vorname"	TEXT NOT NULL,
# 	"Geburtstag"	TEXT NOT NULL,
# 	"Geburtsort"	TEXT NOT NULL,
# 	"Geburtsland"	TEXT NOT NULL,
# 	"Land"	TEXT NOT NULL,
# 	"Code"	TEXT NOT NULL,
# 	"Ort"	TEXT NOT NULL,
# 	"Strasse"	TEXT NOT NULL,
# 	"Hausnummer"	TEXT NOT NULL,
# 	PRIMARY KEY("Person_ID")
# )"""

# cur2.execute(create)


# %%
# zum Zurücksetzen Zelle ausführen

perf = widgets.IntProgress(
    value=0,
    min=0,
    max=100,
    description='Berechne:',
    bar_style='', # 'success', 'info', 'warning', 'danger' or ''
    style={'bar_color': 'lightgreen'},
    orientation='horizontal')
act = widgets.FloatText()
act.value = '0'
display(perf, act)


# %%
perf.value = 0
act.value = 0
display(perf, act)
t0 = time.perf_counter()

for i in range(num_pers3):
# for i in range(3):
    count = 0
    if (0 == i % 100_000):
        perf.value += 1
        act.value += 1

    # print(i)
    # select Person
    sp = 'SELECT * FROM Person WHERE Person_ID = ' + str(i+1)
    cur.execute(sp)
    p = cur.fetchone()
    # print(p)

    # add Adresse
    if (0 == p[6]):
        p[6] += 1
    sa = 'SELECT * FROM Adresse WHERE Adresse_ID = ' + str(p[6])
    cur.execute(sa)
    a = cur.fetchone()
    # print(a)

    # build Person string
    pers = p[1:-1] + a[1:]

    # print(pers)

    insert = """INSERT INTO Person
        (Nachname, Vorname, Geburtstag, Geburtsort, Geburtsland, Land, Code, Ort, Strasse, Hausnummer)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    cur2.execute(insert, pers)


# %%
conn.commit()
conn.close()


# %%
conn2.commit()
conn2.close()


# %%



