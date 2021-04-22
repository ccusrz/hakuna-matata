#author: uzielsrz
#created: 2020-09-15 23:00:08.113986

"""
Sample database:
[{"id": 1001, "mo": 123}, {"id": 1001, "mo": 123}, {"id": 1001, "mo": 123}, {"id": 1001, "mo": 123}]
"""

import json

def check(file, id):
	for row in file: 
		if str(row["id"]) == id: return True
	return False

def current_balance(file, id):
	for row in file:
		if str(row["id"]) == id: print(f'Current balance: {row["mo"]}$'); return;

def withdraw(file, id):
	for row in file:
		if str(row["id"]) == id: 
			amount = int(input("Enter amount to be withdrawn: "))
			while amount > row["mo"]: amount = int(input("Entered amount exceeds current balance. Enter amount to be withdrawn: "))
			row["mo"] -= amount
			print("Money has been withdrawn succesfully.")
			return

def deposit(file, id):
	for row in file:
		if str(row["id"]) == id: 
			amount = int(input("Enter amount to be deposited: "))
			while amount < 0: amount = int(input("Entered amount is invalid. Enter amount to be deposited: "))
			row["mo"] += amount
			print("Money has been deposited succesfully.")
			return

def transfer(file, id):
	ne_id = input("Enter ID of interest: ")
	while not check(file, ne_id): 
		ne_id = input("That ID is not registered. Enter ID of interest or Enter 'q' to quit: ")
	if ne_id in ('q', 'Q'): return
	for row in file:
		if str(row["id"]) == id: 
			amount = int(input("Enter amount to be transferred: "))
			while amount > row["mo"]: amount = int(input("Entered amount exceeds current balance. Enter amount to be transferred: "))
			row["mo"] -= amount
			break

	for row in file:
		if str(row["id"]) == ne_id:
			row["mo"] += amount
			print("Money has been transferred succesfully.")
			return

def main():
	id = input("Enter ID: ").strip()
	with open("db.json", "r") as db:
		js = json.load(db)
		while True and check(js, id):
			opt = input(f"\n\nUser {id}, what would you like to do?\n1. View balance\n2. Withdraw\n3. Deposit\n4. Transference\n5. Exit\nEnter option:")
			if opt == '1': current_balance(js, id);
			elif opt == '2': withdraw(js, id);
			elif opt == '3': deposit(js, id);
			elif opt == '4': transfer(js, id);
			elif opt == '5': 
				print("Thanks for using our service"); 
				break;
		else: print("ID not registered on the database"); 

	with open("db.json", "w") as db:
		json.dump(js, db)

if __name__ == '__main__':
	main()

