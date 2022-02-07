# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:34:41 2021

@author:Bahrom
"""
# otam={
#       'ism':'Intizom Qurbonov',
#       'yosh':'45',
#       'vil':'qashqadaryo',
#       'malumot':'o\'rta maxsus'
#       }
# print(f"Otamninig ismi {otam['ism'].title()}, yoshi {otam['yosh']} da, {otam['vil'].title()}da tug'ilgan,\
#       malumoti {otam['malumot'].capitalize()}")
# taomlar={
#     'ali':'osh',
#     'vali':'sho\'rva',
#     'abror':'norin',
#     'asror':'lapsha',
#     'sardor':'jizz'
#     }
# print(f" Abror {taomlar['ali'].upper()}ni juda yaxshi ko'radi.")
py_i_l={
        'integer':'butun son',
        'float':"O'nlik son",
        "string":'matn',
        'list':'ro\'yxat'
        }
# kalit=input("Kalit so'znini kiriting.").lower()
# print(py_i_l.get(kalit, ))
kalit=input("Kalit so'znini kiriting.").lower()
tarjima=py_i_l.get(kalit, )
if tarjima==None:
    print(None)
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")




