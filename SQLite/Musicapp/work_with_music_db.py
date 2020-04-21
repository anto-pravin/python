import xml.etree.ElementTree as et
import sqlite3

conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

cur.execute('''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')

cur.execute('''CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')

cur.execute('''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);''')

cur.execute('''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

fname = 'Library.xml'

def lookup(d,key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = et.parse(fname)
items = stuff.findall('dict/dict/dict')
print('count: ',len(items))
for item in items:
    if ( lookup(item, 'Track ID') is None ) : continue

    name = lookup(item,'Name')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    genre = lookup(item,'Genre')
    count = lookup(item, 'Play Count')
    rating = lookup(item, 'Rating')
    length = lookup(item, 'Total Time')

    print(name, artist, album, count, rating, length,genre)
    if name is None or artist is None or album is None or genre is None: 
        continue

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album(artist_id, title) VALUES (?,?)',(artist_id,album))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Track(title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)',(name, album_id, genre_id, length, rating, count))

    conn.commit()
    