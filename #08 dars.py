# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 06:44:01 2021

Boboqulov Baxrom
"""
davlatlar=["Uzbekiston","Qozag\'ston","Armaliston","Turkiya","Ummmon"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort( reverse=True)
# print(davlatlar)
davlatlar.reverse()
print(davlatlar)
sonlar=list(range(120,1200,2))
# print(sonlar)
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])
taomlar=['salat','osh','choy','non','qazi']
nonushta=taomlar[:]
nonushta.remove('qazi')
nonushta.remove('osh')
nonushta.remove('salat')
nonushta.append('qaymoq')
nonushta.append('sirchoy')
nonushta.append('asal')
nonushta=tuple(nonushta)
nonushta=list(nonushta)
nonushta[2]="asalchoy"
print(taomlar)
print(nonushta)