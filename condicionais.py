#Sinais de comparações
#> maior
#< menor
#>= maior ou igual
#<= menor ou igual
#== comparação de igualdeda
#!= diferete

#idade = int(input("Qual sua idade?"))

#if idade >= 18:
    #print("Parabéns, você é maior de idade!😊👌")
#else:
    #print('você é menor de idade 👎')

# temperatura = int(input('Qual a temperatura now?'))

# if temperatura > 30:
#     print('Cuidado! temperatura elevada')

# elif temperatura < 10:
#     print (' Temperaturas muito baixas!')
# else:
#     print('temperatura Agradavel')

#  #Valores booleanos  => tipo de dado
# dinheiro = 15 
# fome = True 

# if dinheiro > 10 and fome:
#     print('vou comprar um bk')
# else: 
#     print('Não tenho saldo')

# # Prova da policia militar
# #Requisitos
# #Idade >= 18
# #altura >= 1.75
# # ficha criminal deve estar limpa
# idade = 20
# altura = 1.61
# Antecedentes = False
# if idade >= 18:
#     if altura >= 18 and altura >= 1.75 and Antecedentes :
#         print(' Está apto para a prova')
#     else:
#         print(' não esta apto)')


# Criar uma variavel chamada IMC, valores entre 13 e 30
# se o valor for menor que 18.5 deve informar "IMC baixo"
# se o valor for maior que 24.9 informas "IMC alto"
#caso contrário, informar "IMC médio"

imc = 19
if imc < 18.5:
    print('IMC baixo')
elif imc  > 24.9:
    print('IMC alto')
else: 
    print('IMC médio')