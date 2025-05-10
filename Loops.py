#For: serve para vc colocar no seu codig qunado ele tem um resultado que vc ja sabe ou fim ja previsto (ex:0 á 100)
#While: fim for desconhecido

#Loop FOR, simulando séries  da academia
#RANGE => faixa intervalo
# Series, 10 repetiçõe
#RANGE: INTERVALO

# for serie  in range(1,11):
#     print(f"Estou fazendo a repetição {serie} 💪")

# deuses = ["Zeus", "Apolo", "Poseidon", "Hades"]

# for deus in deuses:
#     print(f"{deus} é um Deus Grego")


#não esquecer da condição  de saida
#opcao = ""
#while opcao != "sair":
  #  opcao = input("Digite 'Sair' para sair do loop")


import random
# dado = 0 
# jogadas = 0

# while dado != 6:
#     dado = random.randint(1,6)
#     print(f"Jogando o dado tiramos: {dado}")
#     jogadas += 1 # -=1
# print(f"Conseguimos o 6 em {jogadas}")

# #LOOP com CONDICIONAIS
# #Receber N numeros  informar qual é Par ou Impar

# for num in range(0,13):
#     #um numero é par se o resto da divisão do numero por 2 for 0
#     #caso o resto da divisão não seja 0 é impar
#     #Caso o resto da divisão não seja 0, é par[# o operador '%' pega o resto da divisão
#     if num % 2 == 0:
#         print(f"{num} é par")
#     else:
#         print(f"{num} é impar")

# resposta = input('Digite o nome de um Deus Grego: \n')
# if resposta in deuses:
#     print(f"{resposta} é um Deus Grego")
# else: print(f"{resposta} Não é um Deus Grego ")

#------------------------------------------------------------------------
#Desafio
#------------------------------------------------------------------------

# #Desafio 1
# var = 1 
# for number in range(1,101):
#     print(f"o number é {var}")
#     var +=1

#Desafio 2
 
# Numero= int (input("Digite a Tabuada que você deseja:"))
# tabuada = 1

# for tabuada in range (1,11):
#     result = Numero * tabuada 
#     print (f"{Numero} x {tabuada} = {result}")
#     tabuada +=1


# #desafio3
# sorteio = 0
# jogadas = 0
# while sorteio != 777:
#     sorteio = random.randint(111,999)
#     print(f"Jogando o sorteio tiramos: {sorteio}")
#     jogadas += 1 # -=1
# print(f"Conseguimos o 777 em {jogadas}")

#Desafio 4
escolha = int(input('Digite o número que deseja saber o fatorial: '))
resultado = 1
processo = ""

for numero in range(escolha, 0, -1):
    resultado *= numero
    if processo == "":
        processo = str(numero)  #"str" transfoma uma função que converte algo para texto. nesse caso o numero que eu escolhi para texto 
    else:
        processo += f" * {numero}"

print(f"{escolha}! = {processo} = {resultado}")

#Desafio 5
# almas = ["justa", "injusta", "neutra",
#          "justa", "injusta", "neutra"
#          "justa", "injusta", "neutra"
#          "justa", "injusta", "neutra"
#          "justa", "injusta", "neutra"
#          "justa", "injusta", "neutra"]

# condenadas = 0 
# redimidas = 0 

# for espirito in almas:
#     if espirito == "justa":
#         redimidas +=1 
#     elif espirito == 'injusta':
#         redimidas += 1
#     elif espirito == "neutra":
#         redimidas += 1
#     else: 
#         print("Acabou")

# print(f"Zeus está escolhendo o destinos das almas mais crueis ja existida na terra \n almas condenadas = {condenadas} \n Almas que se safaram {redimidas}")

