# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:58:30 2021

Dars 17
# """
# son=1
# while son<=5:
#     print(son, end='')
#     son=son+1

# print('Kiritilgan sonni kvadratini hisoblaydigan dastur.')
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun <exit> deb yozing):"
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2 )
#     else:
#         print('Dastur tugadi!')

# print('Kiritilgan sonni kvadratini hisoblaydigan dastur.')
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun <exit> deb yozing):"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2 )


# print('Kiritilgan sonni kvadratini hisoblaydigan dastur.')
# savol="Istalgan sonni kiriting"
# savol+="(dasturni to'xtatish uchun <exit> deb yozing):"

# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:
#         print(float(qiymat)**2 )



# sonlar=list(range(1,11,))
# for son in sonlar:
#     if son==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")






# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")



son =1
while son<10:
    son += 1
    if son%2!=0:
        # continue
        print("...")
    else:
        print(son)