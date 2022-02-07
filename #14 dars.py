# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:23:43 2021

Bahrom Boboquolov
#14-dars
"""
# talaba_0={'ism':'Anvar','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['yosh']} yoshda,\
#       {talaba_0['t_yil']}-yilda tug\'lgan")
      
# telfonlar={
#     'ali':'iphone',
#     'vali':'mi',
#     'gaday':'samsung',
#     'toga':'artel'
#     }
# telfonlar['gaday']='nokia'
# del telfonlar['toga']
# print(telfonlar)
# telefon=telfonlar.get('ali','Bunday so\'z yo\'q!')
# print(telefon)
# otam={
#       'ism':'Intizom',
#       'tyil':1976,
#       'tuman':'kitob'
#       }
# print(f"Otamning ismi {otam['ism'].title()},\
#       {otam['tyil']}-yilda\
#           {otam['tuman'].title()}da tug\'lgan.")
# taomlar={
#     'ali':'osh',
#     'vali':'shurpa',
#     'gaday':'non va choy',
#     'toga':'tolka kabob'
#     }
# print(taomlar)
# taom=taomlar.get('ali')
# print(f" Ali faqat {taom}ni yaxshi ko\'radi.")
lugat_py={
    'float':'O\'lik son',
    'int':'Butun son',
    'list':'ro\'yxat',
    'string':'Matn',
    'tuple':'O\'zgarmas ro\'yxat'
    }
kalit=input("Kalit so\'zni kiritig.").lower()
key=lugat_py.get(kalit)
if key==None:
    print('Bunday so\'z yo\'q.')
else:
    print(f"{kalit.lower()} so'zi {key}  deb tarjima qilinadi.")