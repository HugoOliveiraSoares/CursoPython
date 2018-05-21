import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

dataset['price'].hist(bins = 30, color = 'red') # Plota o grafico, o parametro bins (quantidade de caixas para agrupar os dados)
dataset[['bedrooms','bathrooms']].hist(bins=30,alpha=0.5,color='Green') # parametro alpha define a opacidade do grafico
plt.show()# Mostra o grafico
