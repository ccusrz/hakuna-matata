#Binary search variation
def ternarysearch(arr, li, ls, k):
	if li == ls:
		return False
	else:
		subdiv = int(ls// 2.8)
		if subdiv == 0:
			if k in (arr[0], arr[1]):
				return True
			else:
				return False
		elif arr[ls-1] < k:
			return False
		elif k in (arr[subdiv-1], arr[(2*subdiv)-1], arr[ls-1]):
			return True
		else:
			if arr[subdiv-1] > k:
				return ternarysearch(arr[li:subdiv], li, subdiv, k)
			elif arr[subdiv-1] < k:
				if arr[(2*subdiv)-1] > k:
					return	ternarysearch(arr[subdiv:2*subdiv], li, len(arr[subdiv:2*subdiv]), k)
				else:
					return	ternarysearch(arr[(2*subdiv):ls], li, len(arr[(2*subdiv):ls]), k)

arr = list(map(int, input("Enter n numbers: ").strip().split()))
k = int(input("What number is to be found?: ").strip())
arr.sort()
if ternarysearch(arr, 0, len(arr), k):
	print("k it's there")
else:
	print("k it's not there")

