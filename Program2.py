try:
   x = float(input('x = '))
   if x < 2:
    print('Micro')
    if x > 2 and x < 3:
     print('Very minor')
   if x > 3 and x < 4:
     print('Minor')
   if x > 4 and x < 5:
     print('Light')
   if x > 5 and x < 6:
     print('Moderate')
   if x > 6 and x < 7:
     print('Strong')
   if x > 7 and x < 8:
     print('Major')
   if x > 8 and x < 10:
     print('Great')
   if x > 10: 
      print('Meteoric')
except ValueError:
     print('Ви ввели не число')