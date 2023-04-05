'''
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 05/04/23
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def areaPoligono(poligono,n1 = 0,n2 = 0):
    triangulo = f"Area del Triangulo: {(n1*n2)/2}";
    cuadrado = f"Area del Cuadrado: {n1*n1}";
    rectangulo = f"Area del Rectangulo: {n1*n2}";
    if poligono == "triangulo":
        return print(triangulo);
    elif poligono == "cuadrado":
        return print(cuadrado);
    elif poligono == "rectangulo":
        return print(rectangulo);
    else:
        return "Poligono incorrecto";

areaPoligono("triangulo",10,5);
areaPoligono("rectangulo",5,7);
areaPoligono("cuadrado",4);