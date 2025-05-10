# # Blocos de código/ funcionalidades reutilizaveis
# # Ex: print()
# # Funções tipicamente tem nome, parâmetros e retorno


# def mensagem():
#     print("Olá Mundo")

# mensagem()


# def mensagens(nome):
#     print(f"O nome é {nome}")
#     # Chamando a função 
# mensagens('Julia')

# def duplicar(numero):
#     resultado = numero * 2
#     return resultado
# # Retorno precisa ser explicito

# print(duplicar(5))


# # Função com input para escolher um numero e somando dois, retornando o resultado
# valor = int(input("Escolha um número: "))

# def somar(valor):
#     resultado_soma = valor + 4
#     return resultado_soma
# print(somar(valor))

# # -------- Python - tem dois parametros, posicional e palavra-chave --------

# def coffe_machine(qntd_cafe, qntd_agua):
#     print(f"Fazendo café com {qntd_cafe}mg de pó e {qntd_agua}ml de água")


# # Parametro Posicional
# coffe_machine(150,20)

# # Parametro Palavra chave
# coffe_machine(qntd_agua=150, qntd_cafe=20)


# letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#           'u', 'v', 'w', 'x', 'y', 'z']

# def codificar(texto_original, desloc):
#     texto_modificado = ''
#     for caracter in texto_original:
#         if caracter in letras:
#             posicao_original = letras.index(caracter)
#             nova_posicao = (posicao_original + desloc) % len(letras)
#             texto_modificado += letras[nova_posicao]
#         else:
#             texto_modificado += caracter
#     return texto_modificado  # <--- fora do for!

# print(codificar("rato", 1))


letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

def codificar(texto_original, desloc):
    
    texto_modificado = ''
    for caracter in texto_original:
        if caracter in letras:
            posicao_original = letras.index(caracter)
            nova_posicao = (posicao_original - desloc) % len(letras)
            texto_modificado += letras[nova_posicao]
        else:
            texto_modificado += caracter
    return texto_modificado  # <--- fora do for!

print(codificar("rato", -1))
