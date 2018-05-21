import pandas as pd
# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

print(dataset.isnull().sum())# isnull: faz uma verificação em todas linhas e colunas em busca de valores faltando
                              # sum: retorna a quantidade valores nulos ou faltantes por colunas
print('-----------------------------------\n')
dataset.dropna(inplace = True)# Remove todas as linhas com colunas sem valores
                              # O parâmetro inplace=True é para as modificações serem persistidas em memória.
print(dataset.isnull().sum())
print('-----------------------------------\n')
dataset.dropna(how='all', inplace=True)
print(dataset.isnull().sum())
dataset['floors'].fillna(dataset['floors'].mean(), inplace=True)
print('-----------------------------------\n')
print(dataset.isnull().sum())
print('-----------------------------------\n')
dataset['bedrooms'].fillna(1, inplace=True)
print(dataset.isnull().sum())
