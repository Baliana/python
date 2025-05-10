import arts, random, json

BASE = "Desafio #10 - google/dados.json"

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, mode='r', encoding='UTF-8') as arquivo:
        return json.load(arquivo)

def duelo_de_termos(termos):
    print(arts.logo)
    print("Bem-vindo ao duelo de popularidade do Google!\n")

    pontos = 0
    continuar = True

    while continuar:
        termo1, termo2 = random.sample(termos, 2)

        print(f"Quem é mais pesquisado?")
        print(f"A: {termo1['term']}")
        print(f"B: {termo2['term']}")
        escolha = input("Qual termo é mais pesquisado? A ou B: ").strip().upper()

        if escolha not in ["A", "B"]:
            print("Escolha inválida!!")
            continue

        escolhido = termo1 if escolha == "A" else termo2
        outro = termo2 if escolha == "A" else termo1

        if escolhido["searches"] >= outro["searches"]:
            print(" Você acertou!")
            pontos += 1
        else:
            print(" Você errou!")
            print(f"{escolhido['term']}: {escolhido['searches']} buscas")
            print(f"{outro['term']}: {outro['searches']} buscas")
            print(f" Pontuação final: {pontos}")
            continuar = False
            break

        continuar = input("\nQuer continuar? (s/n): ")

    print("\nObrigado por jogar!")

termos = carregar_dados(BASE)
duelo_de_termos(termos)
