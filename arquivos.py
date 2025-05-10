produtos = {
    "GTA VI": 700,
    "Good of War": 300,
    "Minicraft": 29
}

#leitura= "R"ead
#gravação="w"rite
#acentuar= "A"append

#Salvar esse dicionario em um arquivo
#em operações de gravação, o arquivo não precissa exisir

with open("carrinho_compras.txt", mode="w", encoding="UTF-8") as arquivo:
    #estamos desmembrando o dicionario em strings para salvar
    for jogo, valor in produtos.items():
        arquivo.write(f"{jogo}:{valor} \n")

carrinho_usuario = {}
with open("carrinho_compras.txt", mode="r", encoding="UTF-8") as arquivo:
    #começar a triste saga de formatar o dicionario 
    conteudo = arquivo.readlines()
    
    for linha in conteudo:
        linha = linha.strip()
        descricao, valor = linha.split(":", 1)
        print(descricao, valor)
        #pegamos o nome do produto e slavamos como uma chave no dicionario, o valor do produto vita a "descrição" do dicionario
        carrinho_usuario[descricao] = valor
    print(carrinho_usuario)


import json

with open("carrinho_compras.json", mode='w') as arquivo:
    json.dump(produtos, arquivo)
# Cursor  baixar 


with open("carrinho_compras.json", mode='r') as arquivo:
    carrinho_json = json.load(arquivo)
    print(carrinho_json)