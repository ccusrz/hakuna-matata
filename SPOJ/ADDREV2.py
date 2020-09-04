#Second approach for https://www.spoj.com/problems/ADDREV/
#author: ccusrz
#2020-09-01|23:53:56
for _ in range(int(input())):
	y = input().split()
	print(int(str(int(y[0][::-1]) + int(y[1][::-1]))[::-1])) 
