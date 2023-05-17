#laços condicionais
palavra = 'abc'
while palavra != "":
    palavra = input('Palavra: ')
    significado = input("Significado: ")
    dicionario[palavra] = significado

print(dicionario)