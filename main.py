from Hilos import Hilos
from ObjetoSeguro import Objetoseguro

if __name__ == "__main__":
     name = input("Ingresa tu nombre:")
     obj_1 = Objetoseguro(name)
     puerto_s = int(input("Ingresa tu puerto:"))
     puerto_d = int(input("Puerto de destino:"))
     obj_1_hilos = Hilos(obj_1, puerto_s, puerto_d)
     obj_1_hilos.start_threads()