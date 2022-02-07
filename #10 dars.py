# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:20:29 2021

@author: Bahrom
10 dars
# """
avtolar=['Tiko','Matiz','Spark','bmw','Volvo']
for avto in avtolar:
    if avto=='bmw':
        print(avto.upper())
    else:
        print(avto.capitalize())
ism=input('Ismingizni kiriting\n>>>')
if ism.lower()=='ali':# Bu yerda == belgisini o'niga !=belgisini ham qo'llasa bo'ladi faqat o'rni almashadi. 
    print("Salom Ali")
else:
    print("Uzr biz Alini kutyabmiz!")

javob=int(input("5Х6 nechchiga teng!"))
if javob !=30:
    print("false")
else:
    print("true")
yosh=int(input("Yoshingizni kiriting\n<<<"))
if yosh <=18:
    print('Sizga kirish mumkin emas')
else:
    print("Xush kelibsiz!")
login=input('Yangi login tanlang!\n<<<')
if len(login)<=5:
    print("Login 6 tadan kam bo\'lmaslik kerak!")
yil=int(input("Tug\'lgan yilingizni kiriting!"))
if 2021-yil<18:
    print(f"Siz {2021-yil} yoshda ekansiz.")
    print("Sizga kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
covid=int(input("Yoshingiz nechchida?"))
if covid>=70:
    print("Siz risk guruhda ekansiz")
# AMALIYOT MASHQLAR
cars=['toyota','mazda','gm','bmw','tikko']
for car in cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.capitalize())
cars=['toyota','mazda','gm','bmw','tikko']
for car in cars:
    if car!='gm':# != bilan bajarildi.
        print(car.capitalize())
    else:
        print(car.upper())
login=input("Ismingizni kiriting!\n<<<")
if login.lower()=='admin':
    print('Xush kelibsiz ,Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
else:
    print('Xush kelibsiz',login.title())
x=int(input('Birinchi sonni kiriting!'))
y=int(input('Ikkinchi sonni kiriting!'))
if y==x: print(f"sonlar teng: {x}={y}")
son=float(input("Istalgan sonni kiriting?"))
print("Manfiy son") if son<0 else print("Musbat son")