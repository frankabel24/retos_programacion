'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area (self):
        return self.base * self.height /2
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area (self):
        return self.length * self.width
    
class Square:
    def __init__(self, side):
        self.side = side
    def area (self):
        return self.side * self.side
    
def calcular_area (polygon):
    if (polygon == 'Triangle'):
        base = float(input("Cual es la base del triangulo? "))
        height = float(input("Cual es la altura del triangulo? "))
        triangulo = Triangle(base, height)
        print('El area del triangulo es: ', triangulo.area())
    elif(polygon == "Rectangle"):
        length = float(input('Cual es el largo del rectangulo? '))
        width = float (input('Cual es el ancho del rectangulo? '))
        rectangulo = Rectangle(length, width)
        print('El area del rectangulo es: ', rectangulo.area())
    elif(polygon == 'Square'):
        side = float (input('Cual es el lado del cuadrado? '))
        cuadrado = Square(side)
        print ('El area del cuadrado es: ', cuadrado.area())
    
calcular_area("Triangle")
calcular_area("Rectangle")
calcular_area("Square")