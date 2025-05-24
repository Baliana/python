qnt_adultos = int(input('Quantos adultos vão comparecer?'))
qnt_criancas = int(input('Quantas crianças vão comparecer?'))

total_carne = qnt_adultos * 300 + qnt_criancas * 150
total_entradas =(qnt_adultos + qnt_criancas) * 200
total_cerveja = qnt_adultos * 2.5
total_suco = qnt_criancas * 1
print(f'total de consulmo de carne será:{total_carne}kg \n entradas: {total_entradas}g \n alcool:{total_cerveja}L \n suco:{total_suco}L ')