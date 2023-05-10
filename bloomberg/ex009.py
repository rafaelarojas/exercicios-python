#Código para arrumar erros de escrita como a palavra "azlu"
import random

cores = [
    ["a", "z", "u", "l"],
]

def palavra_certa(palavra):
    letras = list(palavra)
    while letras not in cores:
        random.shuffle(letras)
    return letras

palavra_input = "azlu"
palavra_certa_resultado = palavra_certa(palavra_input)
print(f'Palavra informada: {palavra_input}' + '\n' + 'Palavra certa: ' + ''.join(palavra_certa_resultado))

