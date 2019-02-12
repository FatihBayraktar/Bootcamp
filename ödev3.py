# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:52:11 2019

@author: USER
"""

#Sıcaklık birim dönüştürme programı

sıcaklık=input("Sıcaklık değerini giriniz (ör: 35C,102F) : ")
değer=int(sıcaklık[:-1])
birim_1=sıcaklık[-1]
if birim_1.upper() =="C":
    sonuç=int(round((9*değer)/5 + 32))
    birim_2="F"
elif birim_1.upper =="F":
    sonuç=int(round((değer-32)*5 / 9))
    birim_2="C"
else:
    print("doğru bir değer giriniz")
    quit()
print(sıcaklık,"---->",sonuç,birim_2)

    
    
#kelime ters çevirme
    
kelime=str(input("Bir kelime giriniz:"))
tersi=kelime[::-1]
print("\n\n",kelime,"--->",tersi)

#fibonacci

nterms=50
n1=0
n2=1
count = 0
while count < nterms:
    print(n1,end=' , ')
    nth= n1+n2
    n1=n2
    n2=nth
    count +=1
        
#çarpım tablosu

sayı=int(input("Bir sayı giriniz :"))
print("{} x 1 =".format(sayı),sayı*1)
print("{} x 2 =".format(sayı),sayı*2)
print("{} x 3 =".format(sayı),sayı*3)
print("{} x 4 =".format(sayı),sayı*4)
print("{} x 5 =".format(sayı),sayı*5)
print("{} x 6 =".format(sayı),sayı*6)
print("{} x 7 =".format(sayı),sayı*7)
print("{} x 8 =".format(sayı),sayı*8)
print("{} x 9 =".format(sayı),sayı*9)

#üslü ifade alma

my_list=[x**3 if x%2==0 else x**2 for x in range(1,21)]
print(*my_list)




