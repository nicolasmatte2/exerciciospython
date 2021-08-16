n = int(input('Qual e a velocidade do seu carro? '))
if n == 80:
    print('Tudo certo, continue dirigindo assim!')
else:
    print('Multado! voce escedeu o limite de velocidade de 80 km/h')
    print('Voce excedeu o limite em {}'.format(n-80))
    print('Voce deve pagar a multa de R${}'.format((n-80)*7))
    