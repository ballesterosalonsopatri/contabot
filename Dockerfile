# Usar imagen base ligera de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
COPY app.py .
COPY templates/ templates/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto (CAMBIADO a 8080 para coincidir con app.py)
EXPOSE 8080

# Comando para ejecutar
CMD ["python", "app.py"]

# Para ejecutar:
# docker build -t contabot .
# docker run -p 8080:8080 --env-file .env contabot
