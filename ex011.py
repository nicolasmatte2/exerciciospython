a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
p = a*l/2
print('Sua parede tem dimensao de {}x{} e sua area de e de {}m²\nPara pintar essa parede, voce precisara de {:.2f}l de tinta.'.format(a, l, a*l, p))