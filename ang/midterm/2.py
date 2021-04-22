# -*- coding: utf-8 -*-
#author: uzielsrz 
#date: 31/8/2020 12:34 pm

L = int(input('Enter Ln: ')) 
H =  int(input('Enter H: '))
speed = L / 12 #Asumimos la velocidad, dado que el día dura 12 horas
time = H / speed #Calculamos el tiempo en horas, H forma parte de la fórmula dado que es la distancia total que nos interesa
if L > H: print(f'Time when reaching H: {time} hours')
else: print('The snail didn\'t get out of the pit')  

