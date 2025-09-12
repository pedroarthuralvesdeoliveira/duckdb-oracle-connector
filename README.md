# 🦆 Conector DuckDB ↔️ Oracle

Este projeto demonstra como integrar o banco de dados Oracle ao DuckDB utilizando `oracledb`, `pyarrow` e `duckdb`.

> ⚠️ **Aviso**: O DuckDB não possui suporte nativo para Oracle, então este conector funciona como uma ponte via Python, carregando os dados de Oracle em batches e criando tabelas no DuckDB com pyarrow.

## ✅ Requisitos

- Python 3.9+
- `uv` para gerenciamento de dependências
- Acesso a um banco de dados Oracle (com DSN configurado)
- Oracle Client (se necessário para sua plataforma)

## 📦 Instalação

### Usando uv

```bash
uv pip install oracledb pyarrow duckdb
```

### Usando requirements.txt

```txt
oracledb
pyarrow
duckdb
```

```bash
pip install -r requirements.txt
```

## 🚀 Como usar

```python
import oracledb
import pyarrow
import duckdb

# Substitua pelas suas credenciais
user = "SEU_USUARIO"
password = "SUA_SENHA"
dsn = "SEU_DSN"  # ex: "localhost/orclpdb1"

# Sua query Oracle
sql = "SELECT * FROM PRODUTOS"

# Conexão com Oracle e criação da tabela no DuckDB
with oracledb.connect(user=user, password=password, dsn=dsn) as connection:
    for odf in connection.fetch_df_batches(statement=sql, size=4):
        df = pyarrow.table(odf)
        duckdb.sql("CREATE OR REPLACE TABLE products AS SELECT * FROM df")

# Consulta no DuckDB
print(duckdb.sql("SELECT * FROM products"))
```

## 🧠 Como funciona

1. **Conecta ao banco Oracle** usando `oracledb`
2. **Executa a query em batches** com `fetch_df_batches`
3. **Converte cada batch** em `pyarrow.Table`
4. **Cria uma tabela temporária** (ou persistente) no DuckDB a partir desses dados
5. **Consulta os dados** diretamente no DuckDB

## 📝 Observações

- Esse método é efetivo para leitura de dados Oracle no DuckDB, mas é um processo intermediário via Python
- Você pode converter os dados para Pandas, se preferir (`df.to_pandas()`), mas pyarrow oferece melhor performance com DuckDB
- Ideal para pipelines de análise de dados, ETL, ou exploração rápida de dados

## 🛠️ Roadmap / Sugestões

- [ ] Suporte para escrita no Oracle?
- [ ] Configuração via `.env`
- [ ] CLI para rodar queries Oracle e salvar no DuckDB

---

**Contribuições são bem-vindas!** 🎉