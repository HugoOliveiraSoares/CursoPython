salario = float(input('Qual é o salario do funcionario? R$ '))
new_salario = salario + (salario * 0.15)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'
        .format(salario, new_salario))