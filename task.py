#TODO #1 Crie uma classe chamada Deus com os atributos nome, domínio e símbolo.
#TODO #2 Crie um método chamado apresentar() que irá imprimir uma introdução básica sobre o deus
#TODO #3 Crie um método chamado realizar_milagre() que irá imprimir um algo como "{deus} realiza um milagre divino relacionado ao(à) {domínio}"

#TODO #4 Crie uma classe de controle chamada Olimpo, o único atributo dessa classe deve ser deuses, inicializada como uma lista VAZIA.
#TODO #5 Crie um método chamado adicionar_deus, que irá receber um Objeto deus como parâmetro e irá colocá-lo na lista deuses(feito na etapa #4)
#TODO #6 Crie um método chamado mostrar_deuses(), que irá exibir todos os Deuses presente no Olimpo.


#TODO #7 Crie um novo atributo na classe Deus chamado seguidores, inicialize esse atributo como 0 por padrão.
#TODO #8 Crie um método chamado adicionar_seguidores() que recebe uma quantidade como parâmetro e adiciona X novos seguidores para o deus, invoque esse método para adicionar 100 seguidores para um deus qualquer e 500 para outro deus qualquer.
#TODO #9 Crie um método chamado maior_deus() na classe Olimpo que deve mostrar qual deus tem o maior número de seguidores. Dica: Use um dicionário para armazenar o nome e os seguidores do deus com mais seguidores.

class Deus:
    def __init__(self, nome, dominio, simbolo):
        self.nome = nome
        self.dominio = dominio
        self.simbolo = simbolo
        self.seguidores = 0  # TODO #7

    def __str__(self):
        return f"{self.nome} do domínio {self.dominio} e é representado pelo símbolo: {self.simbolo} com {self.seguidores} seguidores"

    def apresentar(self):  # TODO #2
        print(f"Eu sou {self.nome}, deus(a) do(a) {self.dominio}, simbolizado por {self.simbolo}.")

    def realizar_milagre(self):  # TODO #3
        print(f"{self.nome} realiza um milagre divino relacionado ao(à) {self.dominio}.")
 
    def adicionar_seguidores(self, quantidade):  # TODO #8
        self.seguidores += quantidade
        print(f"{self.nome} agora tem {self.seguidores} seguidores.")

class Olimpo:
    def __init__(self):
        self.deuses = []  # TODO #4

    def adicionar_deus(self, deus):  # TODO #5
        self.deuses.append(deus)
        print(f"{deus.nome} foi adicionado(a) ao Olimpo.")

    def mostrar_deuses(self):  # TODO #6
        print("Deuses presentes no Olimpo:")
        for deus in self.deuses:
            print(f"- {deus}")

    def maior_deus(self):  # TODO #9
        if len(self.deuses) == 0:
            print("Não há deuses no Olimpo.")
            return

        maior = self.deuses[0]  # Começa assumindo o primeiro deus como o maior
        for deus in self.deuses:
            if deus.seguidores > maior.seguidores:
                maior = deus

        print(f"O maior deus atualmente é {maior.nome} com {maior.seguidores} seguidores.")


# Criando deuses
deus1 = Deus("Poseidon", "Água", "💧")
deus2 = Deus("Zeus", "Raio", "⚡")
deus3 = Deus("Afrodite", "Beleza", "💅")

# Adicionando seguidores
deus1.adicionar_seguidores(100)  # TODO #8
deus2.adicionar_seguidores(500)  # TODO #8

# Criando o Olimpo
olimpo = Olimpo()

# Adicionando deuses ao Olimpo
olimpo.adicionar_deus(deus1)
olimpo.adicionar_deus(deus2)
olimpo.adicionar_deus(deus3)

# Mostrando deuses
olimpo.mostrar_deuses()

# Milagre e apresentação
deus3.apresentar()
deus3.realizar_milagre()

# Verificando o maior deus

olimpo.maior_deus()