print('Discount table:')
products_list1 = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85] 
products_list2 = [i-(i*0.6) for i in products_list1] 
products_list3 = [i-(i-(i*0.6)) for i in products_list1]
for i in range(len(products_list1)):
   print(round(products_list1[i], 2), round(products_list2[i], 2), round(products_list3[i], 2))