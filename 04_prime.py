'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''

def is_prime (number):
    numbers = (1,2,3,4,5,6,7,8,9)
    cont = 0
    for index in numbers:
        if((number/index) == 0 or (number/index) == number):
            cont + 1
    print('Contador: ', cont)
is_prime(4)