"""
a = 10
b = 25
c = 66

x = int(input("Digite um numero: "))

if (x == a or x == b or x == c):
if (x in [a,b,c]):
    print("Esta contido")
else:
    print("Não esta contido")
"""

cor = ["azul", "amarelo","vermelho", "branco"]

while True:
    x = input("Digite o nome de uma cor,"
                "ou digite 0 para sair: ")

    if (x == "0"):
        break
    elif x in cor:
        print("Essa cor está contida!\n")
    else:
        print("Está não está contida!\n")
