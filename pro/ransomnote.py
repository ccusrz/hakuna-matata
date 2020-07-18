
#Solución del chino:
from collections import defaultdict

class Solution(object):
	def canSpell(self, magazine, note):
		letters = defaultdict(int)
		for c in magazine:
			letters[c] += 1

		for c in note:
			if letters[c] <= 0:
				return False
			letters[c] -= 1
		return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], input("Enter word: ").strip()))


"""
Mi solución:

class Solution(object):
	def canSpell(self, basis, word):
		for letter in word:
			if not letter in basis:
				return False
				break
		return True

basis = ['a', 'b', 'c', 'd', 'e', 'f'] 
word = input("Enter word: ").strip()
print(Solution().canSpell(basis, word))
"""


