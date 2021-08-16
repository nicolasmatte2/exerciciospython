n = float(input('Qual o salario do funcionario? R$'))
print('Um funcionario que recebia R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n, n+(n*15/100)))