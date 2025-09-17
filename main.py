import duckdb
from oracle_data_loader import connect_to_oracle, load_data_to_duckdb

def main():
    """Função principal para executar o fluxo de trabalho."""
    sql = "SELECT * FROM PRODUTOS"
    try:
        with connect_to_oracle() as connection:
            load_data_to_duckdb(connection, "products", sql)
            
        print(duckdb.sql("SELECT * FROM products"))
    except oracledb.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
