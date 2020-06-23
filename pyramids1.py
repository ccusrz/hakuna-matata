#Chaotic implementation of a z-character double-pyramid.

"""
3-levels output example:
     z
    zzz
   zzzzz
  zzzzzzz
   zzzzz
    zzz
     z
"""

floors = int(input())
x = 1

#Calculation of first n white spaces
white_spaces = (x+2*floors)+(floors+3)

#Printing out the first pyramid
for i in range(floors):
    for j in range(white_spaces):
        print(" ", end = "")
    white_spaces -= 1
    for j in range(x):
        print("z", end = "")
    x += 2
    print("")

#Printing out intermediate floor
for i in range(x+3): 
    print(" ", end = "")
for i in range(x):
    print("z", end = "")
print("")

#Printing out the second pyramid
white_spaces = x + 4
x-=2
for i in range(floors):
    for j in range(white_spaces):
        print(" ", end = "")
    white_spaces += 1
    for j in range(x):
        print("z", end = "")
    x -= 2
    print("")
