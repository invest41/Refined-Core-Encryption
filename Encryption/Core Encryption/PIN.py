# SET UP CODE
import sqlite3 as s
conet = s.connect('Crypto.sqlite')
cur = conet.cursor()



# Retrieve/Main Code
key = ()
d = cur.execute('SELECT * FROM PIN')

if __name__=='__main__':
	for i in d: key += (i[1].decode(),)
	print(key)

#Key detail
lk = len(key)
if lk >1: print(f'{lk} KEYS PRESENT...')



#END CODE
conet.commit()
cur.close()
