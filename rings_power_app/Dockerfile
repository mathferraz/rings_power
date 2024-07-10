# Dockerfile for backend (Python)
# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia apenas o requirements.txt inicialmente para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos restantes para o contêiner
COPY . .

# Comando para executar a aplicação FastAPI com recarregamento automático
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
