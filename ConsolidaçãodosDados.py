#5. Consolidação dos Dados
#Agrupamento e Resumo:

#Calculando a média dos valores por categoria

  resumo = df.groupby('categoria')['valor'].mean().reset_index()

#Salvando os Resultados:
#Salvando em um novo arquivo CSV

  resumo.to_csv('resumo_indicadores.csv', index=False)

# Inserindo resumo de volta no banco de dados

  resumo.to_sql('resumo_indicadores', con=engine, if_exists='replace', index=False)
