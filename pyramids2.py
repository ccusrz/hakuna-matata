#Less chaotic implementation of a z-character double-pyramid given an arbitrary boundary that
#that determines the numbers of floors of both upper and lower pyramids.

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
floors = int(input().strip())

#Calculating the intermediate floor between the two pyramids
inter_floor = (floors * 2) + 1

#Filling in one pyramid and also outlining it with white spaces
pyramid = []
white_spaces = 0
while inter_floor >= 1:
    aux = ""
    for i in range(white_spaces):
        aux += " "
    for i in range(inter_floor):
        aux += "z"
    pyramid.append(aux)
    white_spaces += 1
    inter_floor -= 2

#Printing out two pyramids
for i in pyramid[::-1]:
    print(i)
for i in pyramid[1:]:
    print(i)
