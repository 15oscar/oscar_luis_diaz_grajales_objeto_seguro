from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import base64



class Objetoseguro():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__llave_s = generate_eth_key()
        self.__llave_p = self.__llave_s.public_key
        self.__llave_s = self.__llave_s.to_hex()
        self.__llave_p = self.__llave_p.to_hex()
        self.llave_pub_receptor = None
        self.nombre_receptor = None



    def llave_publica(self) -> str:
        return self.__llave_p

    def cifrar_msj(self, msj: str) -> bytes:
         mensaje_codificado = self.__codificar64(msj)
         mensaje_cifrado = encrypt(self.llave_pub_receptor, mensaje_codificado)
         return mensaje_cifrado

    def descifrar_msj(self, msj: bytes) -> str:
         text_deci = decrypt(self.__llave_s, msj)
         text_plano = self.__decodificar64(text_deci)
         return text_plano

    @staticmethod
    def __codificar64(msj: str) -> bytes:
        codificar = base64.b64encode(msj.encode('ascii'))
        return codificar

    @staticmethod
    def __decodificar64(msj: bytes) -> str:
        decodificar = (base64.b64decode((msj.decode('ascii')).encode('ascii'))).decode('ascii')
        return decodificar

    def recibir_llave_publica(self, llave: str):
        self.llave_pub_receptor = llave
