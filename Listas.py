#Iterando listas

lista_num = [100,200,300,400,500,700,50]
#lista_indice = range(4)  #[0,1,2,3]

'''
for item in range(len(lista_num)):
    lista_num[item] += 1000
print(lista_num)
'''
#funçao enumerate
for idx,item in enumerate(lista_num):
    lista_num[idx] += 1000
print(lista_num)
