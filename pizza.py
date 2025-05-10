tamanho = input('Digite o tamnho da pizza desejada(P = Pequena, M = Média, G = Grande)')
queijo = input('Deseja adicionar extra de queijo R$5,oo? ')
borda = input('Deseja adicionar borda recheada R$7,oo ? ')

adicional1 = False
adicional2 = False
valor_tamanho = 0
Valor1 = 0
valor2 = 0

if tamanho == 'p':
    valor_tamanho = 20
elif tamanho =='M':
    valor_tamanho = 30
elif tamanho =='G':
    valor_tamanho = 45
else:
   valor_tamanho = 20 

if queijo == "s":
    adicional1 = True
    Valor1 =5
else:
    adicional1 = False


if borda == "s":
    adicional2 = True
    valor2 =7
else:
    adicional2 = False

total = valor_tamanho  + Valor1 + valor2
print(f'O valor total da sua pizza é de R${total}')

