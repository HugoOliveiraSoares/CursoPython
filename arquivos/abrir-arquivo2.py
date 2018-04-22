"""
print("Retornando somente as linhas que possuem a palavra Python:\n")
arq = open('arquivo.txt', 'r')
cont = 0

for linha in arq:
    linha = linha.rstrip() # retira a quebra de linha
    if 'Python' in linha:
        cont = cont + 1
        print(linha)

print("\nForam retornandas", cont, "linhas")
arq.close()
"""
print("Retornando somente as linhas que possuem a palavra Python:\n")
palavra = input("Digite a palavra para busca: ")
arq = open('arquivo.txt', 'r')
cont = 0

for linha in arq:
    linha = linha.rstrip() # retira a quebra de linha
    if palavra in linha:
        cont = cont + 1
        print(linha)

print("\nForam retornandas", cont, "linhas")
arq.close()
