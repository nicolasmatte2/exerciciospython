import math
cO = float(input('Digite o cateto oposto: '))
cA = float(input('Digite o cateto: '))
hipoTenusa = (cA*cA + cO*cO)
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(hipoTenusa)))