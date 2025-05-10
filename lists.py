jogadores = [
    'Yuri Alberto', 
    'Rodrigo Garro',
    'Hugo Souza',
    'Angel Roomero',
    'André Carrillo',
    'Talles Magno',
    'Memphis Depay'
    ]
#adicionar no final
jogadores.append("Cristiano Ronaldo")
print(jogadores)
#adicionar em qualquer posição
jogadores.insert(0,"Gabriel Martinelli")
print(jogadores)
#remover da lista 
jogadores.remove("Yuri Alberto")
print(jogadores)
#verifica se o valor esta na lista 
if"André Carrillo" in jogadores:
    print('André Carrillo faz parte do elenco')
else:
    print('Esse jogador não pertece mais ao clube')

#categoriza a lista em ordem alfabetica
jogadores.sort()
print(jogadores)
#faz ao inveso 
jogadores.reverse()
print(jogadores)

movimentos = ['Papel','Tesoura','Pedra']
escolha = int(input('escolha entre 0 - Papel, 1 - Tesoura,2 - Pedra'))
print(movimentos[escolha ])