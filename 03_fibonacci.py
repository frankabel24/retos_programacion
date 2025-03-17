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