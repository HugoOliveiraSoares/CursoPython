import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')

plt.style.use('ggplot')
dataset.boxplot(column='bedrooms')
dataset.boxplot(column='price', by='bedrooms')
plt.show()
