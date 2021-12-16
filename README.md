# oscar_luis_diaz_grajales_objeto_seguro
Proyecto Final Objeto seguro con la implementacion de socket e hilos

Objetivo:
El proyecto consiste en tener una comunicacion cifrada en ambas partes, es decir del objeto A al objeto B y del Objeto B al Objeto A que todo esto sea transparente para el usuario.

Funcionamiento del programa:
La comunicacion se hace a traves de socketa en este caso de un socket cliente y un socket servidor, en el programa se tiene que escoger el puerto del servidor y el puerto del cliente( que en este caso debe ser el puerto a del servidor al que se quiere conectar). El cifrado y decifrado de los mensaje enviados, se hace mediante curvas elipticas utilizando la libreria eciespy. Se utilizan hilos para crear multiples procesos.



Comentarios:
El archivo que se debe de correr es el main.py
y los demas son el archivo Hilos.py, ObjetoSeguro.py, Servidor.py, Cliente.py y Hilos.py todos deben estar en una misma carpeta y tener en cuenta el hecho de utilizar la librerias correspondientes.
