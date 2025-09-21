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
uv add oracledb pyarrow duckdb
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

Altere a consulta na variável `sql` para se adequar ao que precisa. 
Ajuste o nome da tabela no segundo argumento da função `load_sync_data_to_duckdb` para como preferir. 

```bash
uv run main.py
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
- [X] Configuração via `.env`
- [ ] CLI para rodar queries Oracle e salvar no DuckDB

---


**Contribuições são bem-vindas!** 🎉
