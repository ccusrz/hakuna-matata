import psyco
psyco.full()
for _ in range(int(input())):
	y = input().split()
	print(int(str(int(y[0][::-1]) + int(y[1][::-1]))[::-1])) 
