"""
if(True):
	façaIsso()
else
	façaAquilo()
-------------------------
if(True):
        façaIsso()
elif(True)
	façaAquilo
-------------------------
switch(valor)
	caso1: façaIsso()
	caso2: façaAquilo()
	caso3: façoIssoEAquilo()

acao =int(input("\ndigite 1 para sim e digite 0 para não: "))

if(acao==1):
	print("\nVoce disse que sim.\n")

else:
	if(acao==0):
		print("\nVoce disse que não.\n")
	else:
		print("\nO numero digitado não é valido\n")
"""
idade = int(input("\nInforme a sua idade: "))

if(idade<=0):
    print("\nA sua idade não pode ser 0 ou menor que 0!\n")
elif(idade>150):
    print("\nA sua idade não pode ser superior a 150 anos!\n")
elif(idade<18):
    print("\nVoce precisa ter mias de que 18 anos!\n")
