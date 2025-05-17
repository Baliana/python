def mostrar_splash():
    print("===================================")
    print("🌟 BEM-VINDO À FORJA DOS AVENTUREIROS 🌟")
    print("===================================")

def mostrar_menu():
    print("\nMenu da Forja:")
    print("1 - Mostrar Relatório")
    print("2 - Apagar Forja")
    print("3 - Fabricar Item")
    print("4 - Receber Moedas")
    print("5 - Atualizar Inventário")
    print("0 - Sair")

def forja():
    mostrar_splash()
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("-> Você escolheu: Mostrar Relatório")
        
        elif escolha == "2":
            print("-> Você escolheu: Apagar Forja")
            break #interromper imediatamente a execução de um loop
        elif escolha == "3":
            print("-> Você escolheu: Fabricar Item")
        elif escolha == "4":
            print("-> Você escolheu: Receber Moedas")
        elif escolha == "5":
            print("-> Você escolheu: Atualizar Inventário")
        elif escolha == "0":
            print("-> Saindo da Forja... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa a forja
forja()
