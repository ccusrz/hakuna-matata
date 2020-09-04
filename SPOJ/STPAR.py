import psyco
psyco.full()
p = input()
while p != '0':
	s = [1001]
	x = -1
	q = list(map(int, input().split()))
	if sorted(q) == q: print('yes')
	else:
		for i in range(1, len(q)):
			if q[i] > 1000 or q[i] < x: 
				print('no')
				break
			elif q[i-1] > q[i]: 
				s.append(q[i-1])
			elif q[i] > s[-1]:
				x = s.pop() 
				for tops in s[::-1]:
					if tops > q[i]: break
					x = s.pop()
				s.append(q[i])
			else: x = q[i-1]
		else: print('yes')		 
	p = input()
		