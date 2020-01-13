dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco_dia = dias * 60
preco_km = km * 0.15
preco_total = preco_dia + preco_km

print('O total a pagar é de R${:.2f}'.format(preco_total))