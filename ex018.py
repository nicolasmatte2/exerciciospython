import math
n = float(input('Digite o angulo que voce deseja: '))
print('O angulo de {:.2f} tem SENO de {:.2f}\nO angulo de {:.2f} tem COSSENO de {:.2f}\nO angulo de {:.2f} tem TANGENTE de {:.2f}'.format(n, math.sin(math.radians(n)), n, math.cos(math.radians(n)), n, math.tan(math.radians(n))))