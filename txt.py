import pandas as pd

# 1 ler o CSV
df = pd.read_csv("Dataset_python.csv")

# 2 ver as 15 primeiras linhas
#print(df.head(15))

# 3 Obter a dimensão do dataset
#print(df.shape)

# 4 remover a primeira linha do dataset
#df.to_csv("Dataset_python.csv", index=False, header=False)
#print(df.head(2))

# 5 adicionar headers novos
#n = df.shape[1]
#df.columns = [f"coluna{i+1}" for i in range(n)]
#df.to_csv("Dataset_python.csv", index=False)
#print(df.head(2))

# 6 apresentar o nome das colunas
#print(df.columns)

# 7 trocar o nome de uma coluna a escolha
#df.rename(columns={'coluna1': 'Nome'}, inplace=True)
#print(df.head(2))

# 8 trocar o nome da primeira coluna de index para indice
#df.index.name = 'Indice'
#print(df.head())

#  9 Obter um sumário da estatística descritiva para cada coluna
summary = df.describe(include="all")
print(summary)