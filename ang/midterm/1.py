#author: uzielsrz 
#date: 31/8/2020 12:06 pm

def foo(num):
	aux = 0
	for digit in num:
		aux += int(digit) ** 2
	if aux == 89: return 1
	elif aux == 1: return 0
	return foo(str(aux))
	
def string_numbers(N):
	for i in range(1, N+1):
		if foo(str(i)): print(f'{i}: infeliz')
		else: print(f'{i}: feliz')

string_numbers(int(input('Enter N: ').strip())) 
