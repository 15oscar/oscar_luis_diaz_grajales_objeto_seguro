import rsa
import base64
class ObjetoSeguro():
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.key_public, self.__key_private = self.gen_llaves()

    def gen_llaves(self):
        self.key_public, self.__key_private = rsa.newkeys(1024)
        return self.key_public, self.__key_private

    def llave_publica(self):
        return self.key_public

    def codificar(self, msj:str):
        codificar = base64.b64encode(msj.encode('ascii'))
        return codificar

    def cifrar_msj(self, pub_key, msj): #Aqui hay una duda de los tipos de variables
        text_cifrado = rsa.encrypt(msj, pub_key)  # Se cifra el texto ingresado por el usuario, con la llave publica generada
        return text_cifrado

    def decifrar(self, msj: bytes):
        text_deci = rsa.decrypt(msj, self.__key_private)
        return text_deci

    def decodificar(self, msj:bytes):
        decodificar = (base64.b64decode((msj.decode('ascii')).encode('ascii'))).decode('ascii')
        return decodificar

    def almacenar_msj(self, msj:str):
        if self.nombre == "Alicia":
            file = open("RegistoMsj_Alicia.txt", "w")
            file.write(msj)
            file.close()
        elif self.nombre == "Beto":
            file = open("RegistoMsj_Beto.txt", "w")
            file.write(msj)
            file.close()
        return 1

alicia = ObjetoSeguro("Alicia")
alicia.gen_llaves()
llaveAlicia = alicia.llave_publica()

beto = ObjetoSeguro("Beto")
beto.gen_llaves()
llaveBeto = beto.llave_publica()
# en este apartado se manda el mensaje de alicia a beto
mensaje= alicia.codificar(" Hola betito")
mensajeAlicia = alicia.cifrar_msj(llaveBeto, mensaje)

# beto recibe el mensaje y lo decifra
m=beto.decifrar(mensajeAlicia)
md= beto.decodificar(m)
print(beto.almacenar_msj(md))
print(md)

# En este apartado se manda un mensaje de beto a alicia

mensaje2 = beto.codificar(" hola alicia")
mensajeBeto = beto.cifrar_msj(llaveAlicia,mensaje2)

# alicia recibe el mensaje y lo decifra

m2 = alicia.decifrar(mensajeBeto)
md2 = alicia.decodificar(m2)
print(alicia.almacenar_msj(md2))
print(md2)