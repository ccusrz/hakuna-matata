# -*- coding: utf-8 -*-
#author: uzielsrz 
#date: 31/8/2020 2:32 pm

from math import exp, sin

def f(x):
	return exp(x) + sin(x)

def gold(A, B, Error):
	L, M = 0, 0
	while B-A >= Error:	
		L = A + 0.382*(B-A)
		M = A + 0.618*(B-A)
		if f(L) > f(M): 
			A = L
			L = M
			M = A + 0.618*(B-A)
		else:
			B = M
			M = L
			L = A + 0.382*(B-A)	
	return (A,B)

max = gold(float(input("A: ").strip()), float(input("B: ").strip()), float(input("Error: ").strip()))
print(max)  

