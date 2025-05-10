import random
#o random da um resultado aleatorio(como um sorteio)
print(random.randint(1,6))

jogadores = [
    'Yuri Alberto', 
    'Rodrigo Garro',
    'Hugo Souza',
    'Angel Roomero',
    'André Carrillo',
    'Talles Magno',
    'Memphis Depay'
    ]
jogadores1 = random.choice(jogadores)
jogadores2 = random.choice(jogadores)
print(F'A disputa será entre {jogadores1} VS {jogadores2}')


# numeros decimais/quebrados
print(random.random())# de 0 até 1

#embaralhar/shuffle
random.shuffle(jogadores)
print(jogadores)


#escolhendo jogada
movimentos = ['Papel','Tesoura','Pedra']
escolha_cpu = random.choice(movimentos)
print(escolha_cpu)

#simulando um bola 8- mágica

pergunta = input('Digite sua pergunta: \n')
print(f'Você Pergntou---{pergunta} ---')
resposta = ['Sim, com toda Certeza',
            'Não, com taltal absoluta',
            'Nunca',
            'Humm... Não sei não em...',
            'Provavelmente sim',
            'Provavelmente não']

bola8 = random.choice(resposta)
print(f'🎱 responde: {bola8}')

letras = ['a','b','c','d']
numero = ['1','2','3','4']
simbolos = ['@','!','#','&']

caractere1 = random.choice(letras)
caractere2 = random.choice(numero)
caractere3 = random.choice(simbolos)
novaSenha = caractere1 + caractere2 + caractere3
print(novaSenha)

