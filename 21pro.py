# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:03:16 2021

@author: lenovo
"""

def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()} bahosini kiriting.")
        baholar[ism]=int(baho)
    return baholar
talabalar=['ali','alimardon','azizbek','Laziz']
baholar=bahola(talabalar)




