#Chaotic implementation of a z-rhombus.

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

#We determine each side's altitude
floors = int(input())
x = 1

#Calculation of diagonal angles
white_spaces = (x+2*floors)+(floors+3)

#Printing out the upper triangle
for i in range(floors):
    for j in range(white_spaces):
        print(" ", end = "")
    white_spaces -= 1
    for j in range(x):
        print("z", end = "")
    x += 2
    print("")

#Printing out intermediate axis
for i in range(x+3): 
    print(" ", end = "")
for i in range(x):
    print("z", end = "")
print("")

#Printing out the lower triangle
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
