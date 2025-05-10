import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#criar uma lista com as variaveis 
movimentos = [pedra,papel,tesoura]
escolha = int(input('escolha entre 1 - pedra, 2 - Papel, 3 - Tesoura: '))
 
jogador = pedra

if escolha ==1:
    jogador = pedra
elif escolha == 2:
    jogador = papel
elif escolha == 3:
    jogador = tesoura
else:
    print('Selecione numero de 1 á 3')
    quit()

escolha_cpu = random.choice(movimentos)

#if jogador == escolhaCPU

if jogador == pedra and escolha_cpu == tesoura or jogador == tesoura and escolha_cpu == papel or jogador == papel and escolha_cpu == pedra:
    print(f'{jogador} {escolha_cpu} \n Você Ganhou')
elif escolha_cpu == pedra and jogador == tesoura or escolha_cpu == tesoura and jogador == papel or escolha_cpu == papel and jogador == pedra:
    print(f'{jogador} {escolha_cpu} \n Você Perdeu')

else: 
    print(f"{jogador} {escolha_cpu}\n \n Empatou!")