### Challenges from Youtube ###

'''
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
