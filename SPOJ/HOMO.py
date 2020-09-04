#author: ccusrz
#2020-09-04@08:36:19
#I won't forget you "p = k.values()". Such a bastard :)
homo = 0
k = {}                    
for i in range(int(input())):
	x = input().split()
	if x[0] == 'insert':
		if x[1] in k: 
			k[x[1]] += 1
			if k[x[1]] == 2: homo += 1 
		else: k[x[1]] = 1
	else:
		if x[1] not in k: pass
		elif k.get(x[1]) > 1: 
			if k[x[1]] == 2: homo -= 1
			k[x[1]] -= 1	
		else: del k[x[1]]
	if homo > 0:
		if len(k) > 1: print('both')
		else: print('homo')
	else:
		if len(k) > 1: print('hetero')
		else: print('neither')
