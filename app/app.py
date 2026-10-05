import os
import socket
from flask import Flask
import redis

app = Flask(__name__)

# Se connecte au serveur Redis nommé 'db-service' (exigé par le sujet)
r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'db-service'),
    port=6379,
    socket_connect_timeout=2
)

@app.route('/')
def hello():
    try:
        # Incrémente la clé 'hits' à chaque visite
        hits = r.incr('hits')
    except redis.ConnectionError:
        hits = "impossible de se connecter à la base de données"

    # Récupère le nom/ID du conteneur actuel
    container_id = socket.gethostname()

    # Message exact demandé dans les consignes
    return f"Bonjour ! Cette page a été vue {hits} fois. Je suis le conteneur [{container_id}]."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)