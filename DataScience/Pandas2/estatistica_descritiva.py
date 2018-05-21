import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

print("media: ", dataset['bedrooms'].mean())                #faz a media do numero dos quartos
print("valor maximo: ", dataset['bedrooms'].max())          #valor maximo
print("valor minimo: ", dataset['bedrooms'].min())          #valor minimo
print("desvio padrão: ", dataset['bedrooms'].std())         #distribuição dos dados no dataset
print("\nvalor de simetria:\n", dataset.skew())             #valor de simetria do dataset| skew = 0 valor simetrico, skew != 0 valor assimetrico
print("\ndescrição:\n", dataset['bedrooms'].describe())     # descrição do objeto
