#1.0
import sqlite3 as s
from string import ascii_letters as al
import  random
print('WELCOME TO CORE ENCRYPTION')
#fd = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Transfer INITIAL/Projects/Encryption/SAMPLE TEXT/'


#2.0
def n_l():
     encrypted_msg = ""

     l2 = key - 10
     encrypted_msg += chr(l2)
     cur.execute(f'INSERT INTO Crypto (code) VALUES (?)',(encrypted_msg.encode(),))



#3.0
conet = s.connect('Crypto.sqlite')
cur = conet.cursor()
switch = 0

#4.0
T = input('Change PIN? ').lower().startswith('y')
if T:
 try:
  try:
   key = int(input('\n\nInput PIN... '))
   print(f'PIN: {key}')
  except:
   print('\n\nPIN is number only')
   key = int(input('Input PIN... '))
   print(f'Password: {key}')
 except: pass

if not T:
 key = random.randint(1000,9999) #default
 print(f'\nDefault PIN: {key}')


hold = None


#s = open('sample.txt').read().split(' ')
co = 0
inp = input('Press 1 or ENTER to use sample data...\nPress 2 to input your preferred file name...\nPress 3 to input the data, word for word...')


#5.1
if inp.strip()=='1' or inp.strip()=='':
	print('sample.txt')
	#inp = open(fd+'sample.txt').read()
	inp = open('sample.txt').read()

#5.2
elif inp.strip()=='2':
	inp = open(input('Input File Alias: ')).read()

#5.3
elif inp.strip()=='3':
	count, inp = 0, ''
	while True:
		try:
			count+=1
			imm = input("\n\nType Done when you\'re Done...\nWrite your Note: ")+'\n'
			inp += imm
			print('Number',str(count)+'.')
			if imm.lower().startswith('done'): break
		except: 
			print('ERROR!')
			break
	print('\n\nDone!\n\n')





#6.0
for line in inp.split('\n'):
 if co>0: n_l()
 co+=1
 for g in line.split(' '):
  msg = g.lower().strip()
  encrypted_msg = ""

  for l in msg:
   if ord(l) == 32: continue
   if ord(l) == 10:
    n_l()
    continue
    
   if True:
     l2 = key - ord(l)
     encrypted_msg += chr(l2)
   else:
    try: encrypted_msg += 1
    except: continue

  #Databasing
  if switch == 0:
   switch = 1
   
   if input('\n\nDrop Table? ').lower().startswith('y'):
    cur.execute('DROP TABLE IF EXISTS Crypto')
    cur.execute('DROP TABLE IF EXISTS PIN')
    cur.execute('CREATE TABLE Crypto (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,code TEXT)')
    cur.execute('CREATE TABLE PIN (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,code TEXT)')
    cur.execute(f'INSERT INTO PIN (code) VALUES (?)',(f'{key}'.encode(),))
   else: cur.execute(f'INSERT INTO PIN (code) VALUES (?)',(f'{key}'.encode(),))
  if not len(encrypted_msg)<1:
   cur.execute(f'INSERT INTO Crypto (code) VALUES (?)',(encrypted_msg.encode(),))




conet.commit()
cur.close()
print('\n\nDone...')
