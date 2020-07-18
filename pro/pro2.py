def findDuplicate(nums):
	tor = nums[0]
	hare = nums[0]
	print(f'tor: {tor}')
	print(f'hare: {hare}')
	while True:
		
		tor = nums[tor]
		hare = nums[nums[hare]]
		print(f'tor ii: {tor}')
		print(f'hare ii: {hare}', end='\n' * 2)
		if tor == hare:
			break

	ptr1 = nums[0]
	ptr2 = tor
	while ptr1 != ptr2:
		print(ptr1)
		ptr1 = nums[ptr1]
		ptr2 = nums[ptr2]
	return ptr1

print(findDuplicate([3, 1, 3 ,4 ,2]))