import socket



class Server:
    def __init__(self, objeto, port: int):
        self.__HOST = '127.0.0.1'
        self.__PORT = port
        self.obj = objeto


    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__HOST, self.__PORT))
            s.listen(5)
            conn, addr = s.accept()
            self.listen_client(conn, addr)


    def listen_client(self, conn, addr):
         with conn:
             llave_recibida = conn.recv(130)
             self.obj.llave_pub_receptor =llave_recibida.decode('utf-8')
             nombre_receptor = conn.recv(64)
             self.obj.nombre_receptor =nombre_receptor.decode('utf-8')
             print(f'Conectado con {self.obj.nombre_receptor}. Direccion: {addr}')
             print("Finalizar comunicación [q]")
             while True:
                 data = conn.recv(512)
                 if not data:
                     break
                 mensaje = self.obj.descifrar_msj(data)
                 print(f"{self.obj.nombre_receptor}: {mensaje}")
             print("*"*5 + "Conexion finalizada" + "*"*5)


