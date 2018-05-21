import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

#correlacao = dataset.corr() # implementa por padrão é a correlação de Pearson.
correlacao = dataset.corr('spearman') # implementa por padrão é a correlação de Spearman.
print(correlacao)
