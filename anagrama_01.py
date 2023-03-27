'''
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 26/03/23
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 * - https://retosdeprogramacion.com/semanales2022
'''

def anagrama (wordOne, wordTwo):
    if wordOne.lower() == wordTwo.lower():
        return False;
    elif sorted(wordOne) == sorted(wordTwo):
        return True;

print(anagrama("roma", "amor"));