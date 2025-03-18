'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def reverse_string (sentence):
    reverse = ''
    cont = 0
    for index in sentence:
        cont += 1
    for index in range (1, cont + 1):
        reverse += sentence[cont - index]
        
        
    print('La frase al revés es: ', reverse)

reverse_string('frank')


### Con recursividad ###

    


def reverse_string_recursive (sentence, index = 0 , reversed_sentence = ''):
    cont = 0
    new_reversed_sentence = reversed_sentence
    for i in sentence:
        cont += 1
    new_reversed_sentence += sentence[(cont - 1) - index]
    
    if(index < cont - 1):
        index += 1
        new_reversed_sentence = reverse_string_recursive(sentence, index, new_reversed_sentence)
    return new_reversed_sentence

print('La frase al revés es: ', reverse_string_recursive('frank'))