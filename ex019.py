import random
p = str(input('Primeiro Aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto Aluno: '))
lista = [p, s, t, q]
print('O aluno escolhido foi {}'.format(random.choice(lista)))