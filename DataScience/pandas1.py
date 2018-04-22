import pandas as pd

# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

# Analize de dados
print(type(dataset))
print('Mostra algumas linhas da base de dados----------------------------------\n')
print(dataset.head()) # Mostra algumas linhas da base de dados
print('Lista todas as colunas do arquivo---------------------------------------\n')
print(dataset.columns) # Lista todas as colunas do arquivo
print('Conta quantas linhas tem o arquivo--------------------------------------\n')
print(dataset.count()) # Conta quantas linhas tem o arquivo
print('Mostra as estatisticas--------------------------------------------------\n')
print(dataset.describe()) # Mostra as estatisticas
print()

# Explorando os dados
print('Explorando os dados-----------------------------------------------------\n')
print(pd.value_counts(dataset['bedrooms'])) # agrupa as informações e faz a soma por linhas do dataset.
print(dataset.loc[dataset['bedrooms'] == 3]) # visualiza informações do dataset
print('------------------------------------------------------------------------\n')
print(dataset.loc[(dataset['bedrooms']==3) & (dataset['bathrooms'] > 2)])
print(dataset.sort_values(by='price', ascending=False)) # ordena a exibição do dataset pela coluna
print(dataset[dataset['bedrooms']==4].count()) #  quantidade de imóveis que tem 4 quartos
