import urllib.parse
from sqlalchemy import create_engine
import dotenv
import os

dotenv.load_dotenv()

# Credenciais Azure DB
server = os.getenv("AZURE_SQL_SERVER_DB")
database = os.getenv("DATABASE_NAME")
username = os.getenv("USERNAME_AZURE_DB_SERVER")
password = os.getenv("PASSWORD_AZURE_DB_SERVER")

password_encoded = urllib.parse.quote_plus(password)

AZURE_DB_CONNECTION_STRING = f"mssql+pyodbc://{username}:{password_encoded}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"