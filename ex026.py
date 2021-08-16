n = str(input('Escreva uma frase qualquer: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(n.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(n.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(n.rfind('A')+1))