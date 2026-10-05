# Image de base ultra-légère (Alpine)
FROM python:3.11-alpine

# Dossier de travail dans le conteneur
WORKDIR /app

# Optimisation du cache 
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du code source
COPY app/ /app/

# Sécurité : Utilisateur non-root
RUN adduser -D appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]