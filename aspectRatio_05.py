'''
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 08/04/23
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
'''

from urllib.request import urlopen
from PIL import Image

def mcd(h,w):
    a = h;
    b = w;
    while b != 0:
        a, b = b, a % b;
    img_ratio = (h/a, w/a);
    return img_ratio;

def aspect_ratio(url):
    try:
        with urlopen(url) as f:
            with Image.open(f) as img:
                height, width = img.size;
                aspect_ratio = mcd(height, width);
                print(f"Tamaño {height} x {width}");
                print(f"El aspect ratio es {int(aspect_ratio[0])}:{int(aspect_ratio[1])}");
    except Exception as e:
        print("No se ha podido calcular el aspect ratio");
        print(e);


img_url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png";
aspect_ratio(img_url);
