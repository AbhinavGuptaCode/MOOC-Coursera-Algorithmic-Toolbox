# -*- coding: utf-8 -*-
"""
Created on (date)

@author: %AbhinavGuptaCode
"""



# Uses python3
import sys

def gcd_naive(a, b):
    if a==b:
        return a
    
    divisor=min(a,b)
    dividend=max(a,b)
    remainder=1
    
    while remainder!=0:
        remainder=dividend%divisor
        dividend=divisor
        divisor=remainder   

    return dividend

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
