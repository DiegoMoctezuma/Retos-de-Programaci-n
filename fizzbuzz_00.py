'''
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 25/03/23
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 * - https://retosdeprogramacion.com/semanales2022
'''

def fizzbuzz(num): 
    fizz = num%3;
    buzz = num%5;
    if fizz == 0 and buzz == 0:
        print(f"{num}.- FizzBuzz");
    elif fizz == 0:
        print(f"{num}.- Fizz");
    elif buzz == 0:
        print(f"{num}.- Buzz");
    else:
        print(f"{num}");


contador = 0;
while contador <= 100:
    fizzbuzz(contador);
    contador = contador+1;
