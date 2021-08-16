import random
sorteio = [0, 1, 2, 3, 4, 5]
print('Estou pensando em um numero entre 0 e 5. Tente adivinhar qual é...')
n = int(input('Em que numero eu pensei? '))
print('Processando...')
if random.choice(sorteio) == n:
    print('Parabens voce acertou!')
else:
    print('Voce errou feio!')


