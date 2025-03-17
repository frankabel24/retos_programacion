### Challenges from Youtube Intermediate ###

'''
EJERCICIO 1
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
def fizzbuzz (initial, finish):

    for i in range (initial,finish):
        if(i%3 == 0 and i%5 == 0):
            print('fizzbuzz')
        elif(i%3 == 0):
            print('fizz')
        elif(i%5 == 0):
            print('buzz')
        else:
            print(i)

fizzbuzz(1,101)

'''
EJERCICIO 2
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

'''
def is_anagramas (word_one, word_two):
    if(word_one.lower() == word_two.lower()):
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagramas("Anor43521", "Ron12345a"))   

'''
EJERCICIO 3
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''
def fibonacci ():
    
    prev = 0
    next = 1
    for i in range (0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

print(fibonacci())

### FIBONACCI CON RECURSIVIDAD ####

# memoria: almacenara los valores previos
fibonacci_cache={}

def fibonacci(n):
    # si el valor esta almacenado en fibonacci_cache solo lo retornamos
    if(n in fibonacci_cache):
        return fibonacci_cache[n]

    if n==1:
        val=1
    elif n == 2:
        val=1
    elif n > 2:
        val = fibonacci(n-1) + fibonacci(n-2)
        

    # agregamos resultados a memoria fibonacci_cache
    fibonacci_cache[n] = val
    # retornamos valor
    return val


for x in range(1,5):
    print(x, " : " ,fibonacci(x))