largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
# 2m² = 1l
area = largura * altura
litros = area / 2
print('Sua parede tema a dimensão de {}X{} e sua área é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litros))