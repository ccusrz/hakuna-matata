#Less chaotic implementation of a z-rhombus.

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
floors = int(input().strip())

#Calculating the intermediate axis of simmetry
inter_floor = (floors * 2) + 1

#Filling in one triangle and also diagonals
triangle = []
white_spaces = 0
while inter_floor >= 1:
    aux = ""
    for i in range(white_spaces):
        aux += " "
    for i in range(inter_floor):
        aux += "z"
    triangle.append(aux)
    white_spaces += 1
    inter_floor -= 2

#Printing out the two triangles
for i in triangle[::-1]:
    print(i)
for i in triangle[1:]:
    print(i)
