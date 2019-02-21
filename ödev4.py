# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:59:16 2019

@author: USER
"""

#Şiir sorusu

with open("Davet.txt","r") as f:
    lines=f.readlines()
print(len(lines))
for line in lines:
    print(line)


with open("Davet.txt","r") as f:
    dizeler=f.readlines()

lineList = [line.strip().split() for line in open("Davet.txt").readlines()]

bir=lineList[0][0]
iki=lineList[1][0]
üç=lineList[2][0]
dört=lineList[3][0]
beş=lineList[4][0]
altı=lineList[5][0]
yedi=lineList[6][0]   
sekiz=lineList[7][0]
dokuz=lineList[8][0]
on=lineList[9][0]
onbir=lineList[10][0]
oniki=lineList[11][0]

with open("birinci_kelimeler.txt","w") as g:
    g.write(bir)
    g.write(iki)
    g.write(üç)
    g.write(dört)
    g.write(beş)
    g.write(altı)
    g.write(yedi)
    g.write(sekiz)
    g.write(dokuz)
    g.write(on)
    g.write(onbir)
    g.write(oniki)
    


with open("birinci_kelimeler.txt","r") as h:
    kelimeler=h.readline()
    print(kelimeler)




#Asal Sayı Sorusu

a=17
def kontrol(a):
    count=0
    if a<=2:
        print("Sayı Asaldır")
    elif a%2!=0:
        for b in range(2,(a//2+1)):
            if (a%b)==0:
                count+=1
        if count==0:
            print("Sayı asaldır")
    else:
        print("Sayı asal değildir")
kontrol(a)

#Liste eleman sorusu

Liste=[1,1,2,2,3,3,4,4]
yeni_liste=[]
def yeni():
    for x in Liste:
        yeni_liste.append(x)
    return
print(yeni_liste)
    

#Yaş Hesaplama

from datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age)


