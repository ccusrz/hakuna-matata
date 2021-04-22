from random import shuffle

def sum(player, f):
	"""
	Retorna la suma total de
	lo que vale cada carta que tenga un jugador,
	sea este el croupier o no
	"""

	acum = 0
	for card in player:
		if card in ('J', 'Q', 'K'): #Si la carta es una J, Q o una K
			acum += 10
		elif card == 'A' and f == 'p': #Si la carta es A y el jugador no es el croupier
			acum += int(input("Would you like your A to be 1 or 11?: "))
		elif card == 'A' and f == 'c': pass #Si la carta es A y el jugador es el croupier
		else: acum += card
	if f == 'c' and acum > 11: acum += 1
	elif f == 'c' and acum < 11: acum += 11
	return acum

def pick_card(player, deck):
	"""
	Simula cuando se toma una carta del mazo
	"""

	player.append(deck[-1])
	deck.pop()

def game(deck, bet):

	#Barajeamos el mazo
	shuffle(deck) 

	#Preparamos los arreglos para las cartas del y el croupier, aparte del número de fichas del jugador
	player = []
	p_fichas = 1 #Una ficha dado a que se requiere una apuesta para jugar
	croupier = []

	#Iniciamos primera ronda, con hold del croupier/casa aún sin ocurrir
	round = 1
	croupier_hold = 0
	while True:

		#En la primera ronda el croupier toma una sola carta y el jugador toma dos
		if round == 1: pick_card(croupier, deck); pick_card(player, deck); pick_card(player, deck);

		#Preguntamos al jugador lo que desee hacer dadas las cartas que posee
		opt = input(f'Croupier: {croupier}\nPlayer: {player}\n\nDear player, what would you like to do?\n1. Ask for card\n2. Hold\n3. Double your bet\nEnter option: ')
		
		#Calculamos la suma total según las cartas que posea el jugador
		acum = sum(player, 'p')

		#Hit me! (Dame una)
		if opt == '1':
			pick_card(player, deck)
			print(f'Player: {player}')
			acum = sum(player, 'p')
			if acum > 21: print(f"You have lost {bet}$ y perdido {p_fichas}"); break; #Si te pasas de 21, adiós

		#Plantarse (Hold)
		elif opt == '2':
			print("You chose to hold")

		#Doblar apuesta, si se está en la primera ronda
		elif opt == '3' and round == 1:
			bet *= 2
			p_fichas += 1
			print(f'Now your bet is {bet}')

		if croupier_hold == 0: 	#Si la casa aún no se ha plantado
			print("Now is croupier's turn to play")
			pick_card(croupier, deck)
			print(f'Croupier: {croupier}')
			croupier_sum = sum(croupier, 'c') #Calculamos la suma total según las cartas que posea el jugador

			"""
			Si las cartas del jugador superan a las del croupier, jugador gana el doble de su apuesta
			también el jugador gana si las cartas del croupier dan mayor que 21
			"""
			if (acum > croupier_sum) or croupier_sum > 21: print(f"Player has won {bet * 2}$ y ha ganado {p_fichas * 2} fichas"); break; 
			elif croupier_sum >= 17: croupier_hold = 1; #Si no, si la suma total de las cartas del croupier es mayor o igual a 17, la casa se planta
		round += 1

def main():

	#Preparando el mazo
	naipes = list(range(2, 11)) * 4
	for _ in range(4):
		naipes.append('J')
		naipes.append('Q')
		naipes.append('K')
		naipes.append('A')	

	#Let's go. Apostar
	bet = float(input("What's your bet? "))
	game(naipes, bet)
	
if __name__ == '__main__':
	main()