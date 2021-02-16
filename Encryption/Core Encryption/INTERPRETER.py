import sqlite3 as s
import time as t
from sys import path
#path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Transfer INITIAL/Projects/Encryption/PIN')
import PIN



conet = s.connect('Crypto.sqlite')
cur = conet.cursor()
counter, emp = 0, 0
while True:
 # Confirm PASSWORD
 key = input('What is the decoding key? ')
 if len(key)<1:
  key = PIN.key
  print(f'PASSWORD: {key}')
  if len(key)>1:
   print('\n\nMORE THAN ONE KEY')
   print('Take stock and Input appropriate Key (in the next 5 seconds)')
   sl = 5
   for zzz in range(sl,0,-1):
    print(f'{zzz}...')
    t.sleep(1)
   continue
  else: 
  	try: key = int(key[0])
  	except: 
  		emp += 1
  		if emp>3: break
  		continue
 else:
  key = int(key)
  print(f'PASSWORD: {key}')


 error = None

 show = cur.execute('SELECT * FROM Crypto')
 T = input('Decode Fast or Slow? ').lower().startswith('s')
 if T: thyme = 0.5
 if not T: thyme = 0

 co, lst2 = 0, []
 for s in show:
  if co%10 == 0:
   print(end='\n\n')
   for tic in range(3):
    print('Decoding...')
    t.sleep(thyme)
   
   print(end='\n\n')
  co+=1
  print(f'{s[0]}. ',end = '')
  lst = []
  cou = 0
  for i in s[1].decode():
   try:
    if cou == 0:
     cou = None
     print(chr(key - ord(i)).upper(),end = '')
     lst.append(chr(key - ord(i)))
     continue
    lst.append(chr(key - ord(i)))
    print(chr(key - ord(i)),end = '')
   except:
    error = 'This Message is an error...'
    continue
  print()
  lst2.append(''.join(lst))
 




 sentence = ' '.join(lst2).title()


 if not error == None: print(f'\n\nError: {error}')
 print(f'\n\nMESSAGE:\n\n{sentence}')
 print(f'\n\nPASSWORD: {PIN.key}\n\n')
 if input('Done Interpreting? ').lower().startswith('y'): break
 
 counter+=1
 if counter == len(PIN.key): break

conet.commit()
cur.close()
