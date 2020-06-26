#Short implementation of a z-rhombus

#Getting each side altitude
per = int(input().strip())

#And with this copy, the diagonals
diag = per

#Upper triangle
for i in range(per+1):
	print(" " * diag, end = "")
	print(" z" * i)
	diag -= 1

#Intermedium simmetry axis
print("z", end = "")
print(" z" * per)

#Lower triangle
for i in range(per+1):
	print(" " * i, end = "")
	print(" z" * per)
	per -= 1
