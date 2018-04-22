# Criando e escrevendo em arquivosde texto (modo 'w').

arq = open('arq1.txt', 'w')
arq.write("Hugo Oliveira\n")
arq.write("Criando um arquivo de texto\n")
arq.write("Arquivo criado por mim\n")
arq.close()

# Lendo o arquivo criado:
arq = open('arq1.txt', 'r')
for linha in arq:
    linha = linha.rstrip()
    print(linha)

arq.close()

#===================================================================================
# Acrescentando texto ao arquivo criado (modo 'a')
'''
texto = input("Digite uma frase para acrescentar ao arquivo:\n>>> ")
arq = open('arq1.txt', 'a')
arq.write(texto + "\n")
print("Operação concluída no arquivo " + arq.name + " usando o modo de acesso " + arq.mode)
arq.close()

print("\nTexto alterado: ")
arq = open('arq1.txt', 'r')
for linha in arq:
    linha = linha.rstrip() # Retira a quebra de linha
    print(linha)
arq.close()
'''
