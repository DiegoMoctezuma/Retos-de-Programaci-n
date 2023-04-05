'''
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 04/04/23
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def numPrimo(num):
    if num < 2:
        return False;
    for n in range(2,10):
        if n != num:
            if num%n == 0:
                return False;
    return True;

for i in range(101):
    if numPrimo(i):print(i);
