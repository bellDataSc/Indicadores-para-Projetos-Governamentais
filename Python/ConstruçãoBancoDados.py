#2. Construção do Banco de Dados
#Usando banco de dados PostgreSQL.

#Conexão ao Banco de Dados:

  from sqlalchemy import create_engine

#Exemplo de string de conexão (ajuste de acordo com seu banco de dados)

  engine = create_engine('postgresql://usuario:senha@host:porta/nome_do_banco')

#Teste a conexão

  connection = engine.connect()

#Criação de Tabelas:

  connection.execute("""
CREATE TABLE indicadores (
    id SERIAL PRIMARY KEY,
    indicador_nome VARCHAR(255),
    valor NUMERIC,
    data DATE
);
""")


