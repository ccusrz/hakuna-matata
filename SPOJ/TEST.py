#https://www.spoj.com/problems/TEST/
#author: ccusrz
#2020-09-01|22:38:10
x = []
l = int(input().strip())
while(l != 42):
	x.append(l)
	l = int(input().strip())
	
for _ in x:
	print(_)
