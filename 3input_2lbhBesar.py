bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
    

if bilangan1 > bilangan2 and bilangan1 > bilangan3:
    print ("bilangan pertama ({}) lebih besar dari bilangan kedua ({}) dan lebih besar dari bilangan ketiga ({})." .format (bilangan1, bilangan2, bilangan3))
elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
    print ("bilangan kedua ({}) lebih besar dari bilangan pertama ({}) dan lebih besar dari bilangan ketiga ({})." .format (bilangan1, bilangan2, bilangan3))
elif bilangan3 > bilangan1 and bilangan3 > bilangan2:
    print ("bilangan ketiga ({}) lebih besar dari bilangan pertama ({}) dan lebih besar dari bilangan kedua ({})." .format (bilangan1, bilangan2, bilangan3))
elif bilangan1 == bilangan2 and bilangan1 and bilangan2 > bilangan3:
    print ("bilangan pertama dan bilangan kedua sama ({}) bilangan pertama dan kedua lebih besar dari bilangan ketiga ({}).".format (bilangan1,bilangan2,bilangan3))
elif bilangan1 == bilangan3 and bilangan1 and bilangan3 > bilangan2:
    print ("bilangan pertama dan bilangan ketiga sama ({}) bilangan pertama dan ketiga lebih besar dari bilangan kedua ({}).".format (bilangan1,bilangan2,bilangan3))
elif bilangan2 == bilangan3 and bilangan2 and bilangan3 > bilangan1 :
    print ("bilangan ketiga dan bilangan kedua sama ({}) bilangan kedua dan ketiga lebih besar dari bilangan pertama ({}). ".format (bilangan1, bilangan2,bilangan3))
else:
    print ("ketiga bilangan sama besar")