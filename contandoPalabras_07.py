'''
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 09/04/23
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''

import string

def contador(txt):
    lista = txt.lower().translate(str.maketrans("","",string.punctuation)).split(" ");
    new_list = [];
    for p in lista:
        if not new_list.count(p):
            n = lista.count(p);
            print(f"La palabra '{p}' se ha repetido {n} veces.")
            new_list.append(p);

contador("Hola, Mundo. hola. mundo, HOLA, MUNDO");