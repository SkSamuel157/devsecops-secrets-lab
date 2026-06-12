import os

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
API_TOKEN = os.getenv("API_TOKEN")

print("Iniciando aplicação...")

if DATABASE_USER:
    print(f"Usuário do banco carregado: {DATABASE_USER}")
else:
    print("DATABASE_USER não configurado.")

if DATABASE_PASSWORD:
    print("Senha do banco carregada: ***")
else:
    print("DATABASE_PASSWORD não configurado.")

if API_TOKEN:
    print("Token da API carregado: ***")
else:
    print("API_TOKEN não configurado.")