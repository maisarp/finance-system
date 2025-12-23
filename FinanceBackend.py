import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

# 1. Inicializa a API
app = FastAPI(
    title="Finance System API",
    description="Backend para controle de gastos pessoais e cartões",
    version="1.0.0"
)

# Configuração do Banco de Dados (SQL Server)
CONNECTION_STRING = {SQL_SERVER_CONNECTION_STRING}

# 2. Rota Raiz (Só para testar se a API está viva)
@app.get("/")
def read_root():
    return {"message": "Bem-vinda ao seu Sistema Financeiro! 🚀"}

# 3. Rota Real: Consultar Dívidas da Yasmin
@app.get("/dividas-yasmin")
def get_yasmin_debts():
    try:
        engine = create_engine(CONNECTION_STRING)
        with engine.connect() as connection:
            # Query SQL
            query = text("""
                SELECT p.Name, i.Amount, i.DueDate, pu.Description
                FROM Installments i
                JOIN Purchases pu ON i.PurchaseId = pu.Id
                JOIN Persons p ON pu.PersonId = p.Id
                WHERE p.Name = 'Yasmin' AND i.DueDate BETWEEN '2024-12-01' AND '2025-01-31'
            """)
            result = connection.execute(query)
            
            # Transforma o resultado do banco em uma lista de dicionários (JSON)
            lista_dividas = []
            for row in result:
                lista_dividas.append({
                    "quem": row.Name,
                    "valor": float(row.Amount), # Convertendo Decimal para Float
                    "vencimento": str(row.DueDate),
                    "compra": row.Description
                })
            
            return lista_dividas

    except Exception as e:
        return {"erro": str(e)}

# 4. O "Pulo do Gato" para rodar no Visual Studio
if __name__ == "__main__":
    # Roda o servidor na porta 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)