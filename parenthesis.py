str = input("Enter a character string: ").strip()

a = ''
for i in range(len(str)):
	if i < len(str):
		if str[i] in str[i+1:] or str[i] in str[0:i]:
			a += ')'
		else:
			a += '('

print(a)


