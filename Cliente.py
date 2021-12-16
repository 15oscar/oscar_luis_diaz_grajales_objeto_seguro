import socket



class Client:
    def __init__(self, objeto, port: int):
       self.__HOST = '127.0.0.1'
       self.__PORT = port
       self.obj = objeto

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    s.connect((self.__HOST, self.__PORT))
                    break
                except ConnectionError:
                    continue
            llave = self.obj.llave_publica()
            s.sendall(llave.encode('utf-8'))
            nombre = self.obj.nombre
            s.sendall(nombre.encode('utf-8'))
            while True:
                mensaje = input()
                if mensaje == "q":
                    break
                if mensaje == "consultar":
                    print("aun esta a prueba")
                    continue
                mensaje_cifrado = self.obj.cifrar_msj(mensaje)
                s.sendall(mensaje_cifrado)
            print("*"*5 + "Conexion finalizada" + "*"*5)


