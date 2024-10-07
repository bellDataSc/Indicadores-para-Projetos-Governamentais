#3. Inserção de Dados
#Inserir dados diretamente usando SQL ou utilizando pandas.

#Inserção via SQL:

  connection.execute("""
INSERT INTO indicadores (indicador_nome, valor, data) VALUES
('Indicador A', 123.45, '2023-10-01'),
('Indicador B', 678.90, '2023-10-02');
""")


#Inserção via Pandas:

  import pandas as pd

#Dados de exemplo

  data = {
    'indicador_nome': ['Indicador C', 'Indicador D'],
    'valor': [101.22, 334.55],
    'data': ['2023-10-03', '2023-10-04']
}

  df = pd.DataFrame(data)

#Inserindo dados no banco de dados

  df.to_sql('indicadores', con=engine, if_exists='append', index=False)
