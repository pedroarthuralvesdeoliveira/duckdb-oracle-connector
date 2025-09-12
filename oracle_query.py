import oracledb
import getpass
import pyarrow
import duckdb

un = "DUCKDB_TO_ORACLE"
cs = "localhost:51521/XEPDB1"
pw = getpass.getpass(f"Enter password for {un}@{cs}: ")

sql = "SELECT * FROM PRODUTOS"

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    # odf = connection.fetch_df_all(statement=sql, arraysize=100)
    # print(odf.column_names())
    # print(f"{odf.num_columns()} columns")
    # print(f"{odf.num_rows()} rows")
    
    for odf in connection.fetch_df_batches(statement=sql, size=4):
        df = pyarrow.table(odf) # .to_pandas()
        duckdb.sql("CREATE TABLE products AS SELECT * FROM df")
        #print(type(df))

    # cursor = connection.cursor()
    # for row in cursor.execute("select * from PRODUTOS"):
    #     print(row)

    # with connection.cursor() as cursor:
        # data = cursor.execute("SELECT SYSDATE FROM DUAL").fetchone()
        # print(data)  #

print(duckdb.sql("SELECT * FROM products"))