# -*- coding: utf-8 -*-
# """
# Created on Fri Oct 22 09:41:17 2021

# Boboqulov Bahrom
# """
  
# mahsulotlar={
#     'olma':2000,'anor':3500,'non':1000,'uzum':5000
#     }
# print(mahsulotlar.keys())
# bozorlik=['olma ','anar','choy','guruch']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print()
# # print(bozorlik)
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"iltimos {buyum} olib keling")
py_l={
      'float':'o"nlik',
      'integer':'butun son',
      'for':'biror amalni qayta bajarish',
      'if':'shartlarni tekshirish'
      }
for key,value, in sorted(py_l.items()):
    print(f"{key.title()}-{value}")