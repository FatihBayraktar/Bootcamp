# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:15:32 2019

@author: USER
"""

gunler = {'pazartesi':1,'salı':2,'çarşamba':3,'perşembe':4,'cuma':5,'cumartesi':6,'pazar':7}
print(gunler)
birinci = input('Birinci Gün :')
ikinci = input('İkinci Gün :')
del gunler['pazartesi']
del gunler['salı']
print(gunler)
aylar = [['Ocak'],[31],['Şubat'],[28],['Mart'],[31],['Nisan'],[30],['Mayıs'],[31],
         ['Haziran'],[30],['Temmuz'],[31],['Ağustos'],[31],['Eylül'],[30],['Ekim'],[31],
         ['Kasım'],[30],['Aralık'],[31]]

ilkbahar = ['Mart','Nisan','Mayıs']
yaz = ['Haziran','Temmuz','Ağustos']
sonbahar = ['Eylül','Ekim','Kasım']
kış = ['Aralık','Ocak','Şubat']
adlar = aylar[0:23:2]
günler = aylar[1:24:2]
print(adlar,günler)
adlar_günler = (adlar,günler)
print(adlar_günler)
yaz_gunler = adlar_günler[1][5:8]
print(yaz_gunler[0])
yaz_toplam = yaz_gunler[0] + yaz_gunler[1] + yaz_gunler[2]
print(yaz_toplam)