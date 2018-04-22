"""
manipulador = open('arquivo.txt', 'r')
print("\nMétodo read()\n")
print(manipulador.read())

manipulador.seek(0)

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMétodo readlines():\n")
print(manipulador.readlines())
print(manipulador.readlines())

manipulador.close()
"""
#===============================================================================
print("Teste de abertura de arquivos em Python:\n")

manipulador = open('arquivo.txt', 'r')
arq = open('arquivo.txt', 'r')

cont = 0

for linha in manipulador:
    linha = linha.rstrip() # retira a quebra de linha
    print(linha)

for linha in arq:
    cont = cont + 1
print("Numero de linhas no arquivo:", cont)

arq.close()
manipulador.close()
