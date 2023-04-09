'''
 * Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 09/04/23
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def binario(num):
    binary = "";
    while num != 0:
        num_binario = num % 2;
        num = int(num/2);
        binary = str(num_binario) + binary;
    return binary;
