from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que voçê deseja: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))