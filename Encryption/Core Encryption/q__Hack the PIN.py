from PIN import key
import random, time

#len(lst) limit was 9000, use numpy array

co, lst= 0, []

for i in key:
  try:
   i = int(i)
   while True:
    try:
     co+=1
     x = random.randint(1000,9999)
     print(x)
     if co%2000==0: time.sleep(0.2)

     if i==x:
       print(f'\n\nHacked your PIN 😈: {x}\n{co} trials\n')
       co = 0
       break
    except KeyboardInterrupt as KI: break
  except KeyboardInterrupt as KI: break
