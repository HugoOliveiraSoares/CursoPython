import pandas as pd
import matplotlib.pyplot as plt
# Carrega a base de dados
dataset = pd.read_csv('/home/hugo/Documentos/CursoPython/DataScience/minerandodadosGit/mdrepo/kc_house_data.csv',sep=',')
op = int(input("selecione o grafico a ser plotado:\n"
                "\t>>> 1)Preço\n"
                "\t>>> 2)Bedrooms x Price\n"
                "\t>>> 3)\n"
                "\t>>> "))

if (op == 1):
    dataset['price'].plot()
    plt.show()
elif (op == 2):
    dataset.plot(x='bedrooms',y='price',kind='scatter', title='Bedrooms x Price',color='r')
    plt.show()
elif (op == 3):
    dataset.plot(x='bathrooms',y='price',kind='scatter',color='y')
    plt.show()
