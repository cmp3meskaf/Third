# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:23:33 2023

@author: CMP3MESKAF
"""


# print backwards.

word = input("What word do you want to print backwards? ")
backwards = ""

for i in word:
    backwards = i + backwards
    
print(backwards)

input("Press enter to exit")