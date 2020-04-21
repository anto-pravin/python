import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts(org TEXT, count INTEGER)')

f_name = 'mbox.txt'

fh = open(f_name)
for line in fh:
    
    if not line.startswith('From:'): continue

    content = line.split()

    m = content[1].split('@')
    mail = m[1]

    cur.execute('SELECT count FROM counts where org = ? ', (mail,))

    if cur.fetchone() is None:
        cur.execute('INSERT INTO counts(org, count) VALUES (?,1)',(mail,))
    else:
        cur.execute('UPDATE counts SET count = count + 1 WHERE org = ?',(mail,))
    
    conn.commit()
s = 0
for i in cur.execute('SELECT org,count FROM counts ORDER BY count DESC LIMIT 10'):
    print(str(i[0]),i[1])
    s += i[1]

print(s)

cur.close()