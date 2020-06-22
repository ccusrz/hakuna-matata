#Merge sort in ascending order

def mergesort(arr, il, sl):
	if len(arr) > 2:
		return merge1(mergesort(arr[il:(sl//2)], il, len(arr[il:(sl//2)])), mergesort(arr[(sl//2):sl], il, len(arr[(sl//2):sl]))) 
	elif len(arr) == 1:
		return arr
	else:
		return merge1(arr, [])

def merge1(iarr, sarr):
	arr = []
	if len(iarr) == 2 and len(sarr) == 0:
		#Swaping unities
		if iarr[0] >= iarr[1]:
			arr = iarr[0]
			iarr[0] = iarr[1]
			iarr[1] = arr
			return iarr
		else:
			return iarr
	else:
		return merge2(arr, iarr, sarr)

def merge2(arr, iarr, sarr):
	if len(sarr) == 0:
		arr.extend(iarr)
		return arr
	elif len(iarr) == 0:
		arr.extend(sarr)
		return arr
	else:
		if iarr[0] >= sarr[0]:
			arr.append(sarr[0])
			sarr.remove(sarr[0])
			return merge2(arr, iarr, sarr)
		else:
			
			arr.append(iarr[0])
			iarr.remove(iarr[0])
			return merge2(arr, iarr, sarr)

def main():
	arr = list(map(int, input("Enter numbers separated by white spaces: ").strip().split()))
	print(mergesort(arr, 0, len(arr)))

if __name__ == '__main__':
    main()