# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:39:13 2021

@author: Baxadev
#11-dars
"""
# yosh=int(input("Yoshingizni kiriting?"))
# if yosh<=5:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5 ming so\'m!")
# elif yosh<=18:
#     print("Sizga kirish 10 ming so\'m!")
# elif yosh<=40:
#     print("Sizga kirish 15 miing so\'m!")
# else:
#     print("Sizga kirish mumkinmas!")

# son=float(input("Juft son kiriting"))
# if son%2:
#     print("Bu juft son emas!")
# else:
#     print("Rahmat!")
# park=int(input("yoshingizni kiriting!"))
# if park<=4 or park>=60:
#     narx=0;
# elif park<=12:
#     narx=5000;
# elif park<=18:
#     narx=8000;
# else:
#     narx=10000;
# print("Sizga kirish ",narx," so\'m!")
# x=int(input("Birinchi sonni soningizni kiriting!"))
# y=int(input("Ikkinchi sonni kiriting!"))
# if x==y:
#     print(f"{x}={y}")
# elif x>y:
#     print(f"{x}>{y}")
# else:
#     print(f"{x}<{y}")
# mahsulotlar=['anor','olma','uzum','behi','nok','anjir','urik']
# savat=[]
# for n in range(4):
#   savat.append(input(f"Savatga {n+1} -mahsulotni kiriting!"))
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f"Do\'konimizda {mahsulot} bor")
#     else:
#         print(f"Do\'konimizda {mahsulot} yo\'q!")
# login=['anvar','asror','abror','alisher','amina']
# user=input('Yangi login kiriting!')
# if user.lower() in login:
#     print("Bu login band o\'zingizga boshqa login tanlang!")
# else:
#     print("Xush kelibsiz ",user)
sons=int(input("Istalgan sonni kiriting!"))
for n in range(2,11):
    if not (sons%n):
        print( f"{sons} ni {n} ga qoldiqsiz bolinadi.")
    