# Python Base Image
FROM python:3.10-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Code kopieren
COPY . .

# Startbefehl
CMD ["python", "main.py"]
