from math import hypot
catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto Adjacente: '))

# Hip² = CO² + CA² --> Hip = (CO² +  CA²)^ 0.5

hipotenusa = hypot(catetoOposto, catetoAdjacente)
# hipotenusa = ( (catetoOposto**2) + (catetoAdjacente**2) ) ** 0.5
print('A hipotenusa é igual a {:.2f}'.format(hipotenusa))