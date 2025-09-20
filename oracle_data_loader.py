import oracledb
import getpass
import os
import pyarrow as pa
import duckdb

def sync_connect_to_oracle(): 
    """Conecta ao banco de dados Oracle e retorna o objeto de conexão."""
    un = os.getenv("UN")
    cs = os.getenv("CS") + ":" + os.getenv("PORT") + "/" + os.getenv("SERVICE") # os.getenv(f"{CS}:{PORT}/{SERVICE}") # "localhost:51521/XEPDB1"
    pw = getpass.getpass(f"Enter password for {un}@{cs}: ")
    return oracledb.connect(user=un, password=pw, dsn=cs)

def load_sync_data_to_duckdb(connection, table_name, sql_query):
    """
    Carrega dados do Oracle para o DuckDB em batches usando PyArrow.
    Cria uma tabela no DuckDB com o nome especificado.
    """
    first_batch = True
    with connection.cursor() as cursor:
        for odf in cursor.fetch_df_batches(statement=sql_query, size=100_000):
            arrow_table = pa.table(odf) 

            if first_batch: 
                duckdb.sql(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM arrow_table")
                first_batch = False
            else: 
                duckdb.sql(f"INSERT INTO {table_name} SELECT * FROM arrow_table")