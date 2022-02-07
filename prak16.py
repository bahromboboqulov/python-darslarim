# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:35:06 2021

@author: Bahrom
"""
# temur={
#      'ism':"Amir Temur",
#      'tyil':1336,
#      'vyil':1405,
#      'tjoy':'Yakkabog\' tumani, Xojailg\'or qishlog\'i'
#           }
# alisher={
#      'ism':'Alisher Navoiy',
#      'tyil':1441,
#      'vyil':1501,
#      'tjoy':'Hirotda'
#         }
# umar={'ism':"Umar Muxtor",
#       'tyil':1857,
#      'vyil':1931,
#      'tjoy':'Liviya'
#      }
# person=[temur,alisher,umar]
# for k in person:
#     print(f"{k['ism'].title()} "
#           f"{k['tyil']}da tug'ilgan."
#           f"{k['vyil']}da vafot etgan."
#           f"{k['tjoy']}da tug'ilgan")

# temur={
#      'ism':"Amir Temur",
#      'tyil':1336,
#      'vyil':1405,
#      'tjoy':'Yakkabog\' tumani, Xojailg\'or qishlog\'i',
#      'asar':'Temur Tuzuklari'
#           }
# alisher={
#      'ism':'Alisher Navoiy',
#      'tyil':1441,
#      'vyil':1501,
#      'tjoy':'Hirotda',
#      'asar':'Xamsa'

#         }
# umar={'ism':"Umar Muxtor",
#       'tyil':1857,
#      'vyil':1931,
#      'tjoy':'Liviya',
#      'asar':'Turli xil darsliklar.'
#      }
# person=[temur,alisher,umar]
# for k in person:
#     print(f"{k['ism'].title()}")
#     print(f"{k['asar'].title()}")
        
kinolar={
    'ali':'Qirq qaroqchi',
    'vali':'Ish chashmasi',
    'soli':'Gullar shahri',
    'sori':'Alamlar '
    }
for ism,klar  in kinolar.items():
    print(f"{ism.title()}ning yaxshi ko'rgan kinosi:{klar}")
    
