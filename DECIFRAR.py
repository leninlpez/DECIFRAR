# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:17:53 2020

@author: Lenin

""alfabetos empleados"""
   ATBASH = 'z y x w v u t s r q p o ñ m l k j i h g f e d c b a'
ALFABETO =  'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'


"almacena la forma cifrada del texto"
salida = ''

"Guardar el texto introducido"

texto = input ('Introduce texto: ')

"Ejecuta el cifrado  letra a letra"
 
for simbolo in texto.lower():
    if simbolo in ATBASH:
        
     "Identifica la posicion de cada simbolo" 
     indice = ATBASH.index(simbolo)
     
     "Añade un simbolo al texto cifrado "
     salida += ALFABETO[indice]
     
     "Imprime en pantalla el resultado"
     print (salida)


