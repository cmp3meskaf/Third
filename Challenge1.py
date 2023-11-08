# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:16:06 2023

@author: CMP3MESKAF
"""



# Let the user enter the starting number, the ending number, and the amount by which to count.

start = int(input("What number should I count from: "))
end = int(input("What number should I count to: "))

while start != end:
    print(start)
    if start < end:
        start = start + 1
    if start > end:
        start = start - 1

print(end)
input('Finished! Press enter.')