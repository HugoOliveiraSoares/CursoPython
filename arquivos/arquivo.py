import sys
arq = open("arquivo.txt","w")
arq .write("Ola mundo")
arq .write("manipulando")
arq .write("arquivos")
arq.close()

arq = open("arquivo.txt")
for i in arq:
    sys.stdout.write(i)


"""
print(arq.readlines())
arq.close()
"""
