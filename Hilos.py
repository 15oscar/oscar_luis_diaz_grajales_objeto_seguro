from Servidor import Server
from Cliente import Client
from threading import Thread


class Hilos:
    def __init__(self, objeto, puerto_server: int, puerto_destino: int):
        self.obj_servidor = Server(objeto, puerto_server)
        self.obj_cliente = Client(objeto, puerto_destino)
        self.obj = objeto

    def start_threads(self):
        thread1 = Thread(target=self.obj_servidor.run)
        thread2 = Thread(target=self.obj_cliente.run, daemon=True)
        thread1.start()
        thread2.start()