# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:12:23 2026

@author: shreya
"""
n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
fact = fact * i
print("Factorial:", fact)
