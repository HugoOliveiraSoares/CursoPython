import pandas as pd
# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

# Adicionar dados
dataset['size'] = (dataset['bedrooms']* 20) #cria uma coluna chamada “size” em que tem como valor o tamanho do imovel em m²(quartos*20)
#print(dataset['size'])
# Cria uma coluna que ira caracteriar(cat_size) a casa em
def categoriza(s):
    if s >= 80:
        return 'Big' # Grande
    elif s >= 60:
        return 'Medium' # Media
    elif s >= 40:
        return 'Small' # Pequena

dataset['cat_size'] = dataset['size'].apply(categoriza) # aplica uma função em todas as linhas ou colunas de um dataframe
print(dataset['cat_size'])
print('\n----------------------------------------------------\n')
print(pd.value_counts(dataset['cat_size']))
# Removendo Dados
print('\nRemovendo Dados-------------------------------------\n')
dataset.drop(['cat_size'], axis=1, inplace=True) # a opção axis=1 define que queremos excluir uma coluna e não uma linha
dataset.drop(['size'], axis=1, inplace=True)
# Dropa linhas com bedrooms = 0 e maiores que 30
dataset.drop(dataset[dataset.bedrooms==0].index ,inplace=True)
dataset.drop(dataset[dataset.bedrooms>30].index ,inplace=True)
