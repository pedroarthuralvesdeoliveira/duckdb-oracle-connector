import oracledb
import getpass
import pyarrow as pa
import duckdb

def connect_to_oracle(): 
    """Conecta ao banco de dados Oracle e retorna o objeto de conexão."""
    un = "DUCKDB_TO_ORACLE"
    cs = "localhost:51521/XEPDB1"
    pw = getpass.getpass(f"Enter password for {un}@{cs}: ")
    return oracledb.connect(user=un, password=pw, dsn=cs)

def load_sync_data_to_duckdb(connection, table_name, sql_query):
    """
    Carrega dados do Oracle para o DuckDB em batches usando PyArrow.
    Cria uma tabela no DuckDB com o nome especificado.
    """
    with connection.cursor() as cursor:
        for odf in cursor.fetch_df_batches(statement=sql_query, size=4):
            df = pyarrow.table(odf) 
            duckdb.sql(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")