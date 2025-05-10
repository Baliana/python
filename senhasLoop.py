import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numeros = list(range(11))
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
welcome = """
 ____                  __     ___           _       
| __ )  ___ _ __ ___   \ \   / (_)_ __   __| | ___  
|  _ \ / _ \ '_ ` _ \   \ \ / /| | '_ \ / _` |/ _ \ 
| |_) |  __/ | | | | |   \ V / | | | | | (_| | (_) |
|____/ \___|_| |_| |_|    \_/  |_|_| |_|\__,_|\___/ 
"""

print(welcome)

# Listas de letras, números e símbolos
letras = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numeros = list('0123456789')
simbolos = list('!@#$%^&*()-_=+[]{};:,.<>?')


nr_letras = int(input("Quantas letras terá sua senha? \n"))
nr_numero = int(input("Quantos números terá sua senha? \n"))
nr_simbolos = int(input("Quantos caracteres especiais terá sua senha? \n"))

# Cria uma lista vazia chamada senha
senha = []


for nr_letras in range(nr_letras):
    senha.append(random.choice(letras))

for nr_numero in range(nr_numero):
    senha.append(random.choice(numeros))

for nr_simbolos in range(nr_simbolos):
    senha.append(random.choice(simbolos))

random.shuffle(senha) #Ela embaralha os elementos da lista senha


senha_final = ''.join(senha)

print(f"Sua senha gerada é: {senha}")



# pip install pyinstaller  <-- instala o pacote para gerar EXECUTAVEIS a partir dos aquibos .py
# pyinstaller "nome do seu arquivo" .py  <-- gera o executavel do seu programa


