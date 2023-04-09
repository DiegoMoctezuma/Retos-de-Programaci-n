'''
 * Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 08/04/23
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def invertir(str):
    new_str = ""
    for i in range(len(str)):
        new_str = new_str + str[-(i+1)];
    return new_str;

print(invertir("Hola Mundo"));