#Código para descobri a satisfação dos clientes
print('(1)Excelente' '\n' '(2)Bom' '\n' '(3)Regular' '\n' '(4)Ruim' '\n' '(5)Péssimo')
satisfacao = input("Avalie nossos serviços: ")

if satisfacao == '1' or satisfacao == '2':
    print('Que bom, ficamos felizes em saber disso!')
if satisfacao == '3':
    print('O que poderíamos ter feito diferente?')
    regular = input('Digite suas sugestões: ')
if satisfacao == '4' or satisfacao == '5':
    print('Poxa, sentimos muito! Por gentileza digite "S" caso queira conversar com um de nossos representantes e descrever melhor a situação' '\n' 'Digite "M" para enviar uma mensagem por aqui' '\n' 'Digite "N" se quiser encerrar a conversa')
    letras = input('Digite aqui sua opção: ').lower()
    if letras == 's':
        print('Um de nossos representantes entrará em contato')
    if letras == 'm':
        mensagem = input('Digite sua mensagem: ')
    if letras == 'n':
        pass

print('Agradecemos a atenção e tenha um ótimo dia!')