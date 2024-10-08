#4. Tratamento de Dados
#Leitura de Dados:

  df = pd.read_sql("SELECT * FROM indicadores", con=engine)

#Limpeza e Transformação:

  # Convertendo coluna 'data' para datetime
df['data'] = pd.to_datetime(df['data'])

# Removendo registros com valores nulos
df = df.dropna()

# Criando uma nova coluna baseada em condições
df['categoria'] = df['valor'].apply(lambda x: 'Alto' if x > 500 else 'Baixo')
