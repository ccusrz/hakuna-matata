#author: uzielsrz 
#date: 31/8/2020 1:48 pm

import math

def op(x, odd, even):
	return float(((1 - x) ** even) / math.factorial(odd))

def cond(x):
	while x > 1 or x < 0:
		x = float(input('X must be between 0 and 1, try again: ').strip())			  
	return x

tol = float(input('Tolerance: ').strip())
n = int(input('N: ').strip())
x = float(input('X: ').strip())
if x > 1 or x < 0: x = cond(x) 

result = op(x, 1, 2)
i = 3
j = 4
_ = 2 

while _ < n:
	if _ % 2 > 0: result -= op(x, i, j)
	else: result += op(x, i, j)
	if abs(result) < tol: break	
	print(result)
	i += 2
	j += 2
	_ += 1
	
print(f'Result: {result}')