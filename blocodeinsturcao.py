
num1 = int(input("\nDigite um número: "))

if(num1 > 10):
    print("O valor é maior que 10!\n")
    if (num1 <= 15):
        print("O valor é maior que 10, mas menor que 15!\n")
    else:
        if (num1 <= 50):
            print("O valor é maior que 10, mas é menor que 50!\n")
        else:
            print("O valor é maior que 50!\n")

elif(num1 > 5):
    print("O número é menor que 10, mas maior que 5!\n")
    if (num1==7):
        print("O numero é igual a 7!")

else:
    print("O valor é menor que 5!\n")
