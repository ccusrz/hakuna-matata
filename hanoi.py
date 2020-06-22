#Hanoi towers

def hanoi(disks, rodori, rodtem, roddes):
	if disks == 1:
		print("Disk " + str(disks) + " has moved from " + rodori + " to rod " + roddes)
	else:
		hanoi(disks-1, rodori, roddes, rodtem)
		print("Disk " + str(disks) + " has moved from " + rodori + " to rod " + roddes)
		hanoi(disks-1, rodtem, rodori, roddes)

disks = int(input("Please enter number of disks: ").strip())
rodori = 'A'
rodtem = 'B'
roddes = 'C'
hanoi(disks, rodori, rodtem, roddes)