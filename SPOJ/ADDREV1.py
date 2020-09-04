#First approach for https://www.spoj.com/problems/ADDREV/
#author: ccusrz
#2020-09-01|23:31:38
x = []
for _ in range(int(input())):
	sum = 0
	for l in input().split():
		sum += int(l[::-1])	
	x.append(sum)
 
for _ in x:
	print(str(_)[::-1].strip('0'))
