import socket
import time
import random
import threading

HOST = '127.0.0.1'  # Adresse locale
PORT = 65432  # Port d'écoute

messages = [
    "Transfert de fichiers en cours...",
    "Protocole activé...",
    "Puissance = 85",
    "Connexion au serveur distant...",
    "Alerte : tentative d'intrusion détectée !"
]


def start_socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"🔒 Serveur en attente de connexion sur {HOST}:{PORT}...")

    conn, addr = server.accept()
    print(f"✅ Connexion établie avec {addr}")

    while True:
        message = random.choice(messages)
        print(f"📡 Envoi : {message}")
        conn.sendall(message.encode())
        time.sleep(3)  # Envoie un message toutes les 3 secondes


# Lancer le serveur socket dans un thread
def run_socket_server():
    socket_thread = threading.Thread(target=start_socket_server)
    socket_thread.daemon = True  # Le thread sera automatiquement fermé à la fermeture de l'application
    socket_thread.start()
