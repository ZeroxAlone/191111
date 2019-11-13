# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:20:51 2019

@author: lisa_
"""

def RLEEncode():
    Code = input("Enter a code: ")
    Code += " "
    FinalCode = ""
    Count = 1
    for i in range(1, len(Code)):
        if Code[i-1] != Code[i]:
            FinalCode += str(Count) + Code[i-1]
            Count = 1
        else:
            Count += 1
    
    print(FinalCode)

RLEEncode()
                
def RLEDecode():
    Code = input("Enter a code: ")
    Count = ""
    FinalCode = ""
    for i in Code:
        if i.isdigit():
            Count += i
        else:
            FinalCode += i * int(Count)
            Count = ""
    
    print(FinalCode)
    
RLEDecode()