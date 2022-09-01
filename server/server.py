from socket import *
from dataReader import update_csv_file
from dataReader import path
import os

s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("+\nIP Address: {}\n".format(s.getsockname()[0]))
s.close()

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
currentData = update_csv_file()
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str(conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)

    print(mensaje)
    m = mensaje.split(' ')
    if m[0] == "GET":

        if m[1] in currentData:
            mensajeRespuesta = m[1]
            SEPARATOR = ":><:"
            BUFFER_SIZE = 1024 # send 1024 bytes each time step
            filename = path+mensajeRespuesta
            print(os.path.getsize(filename))
            filesize = os.path.getsize(filename)
            print(filename)
            conexionSocket.send(f"{filename}{SEPARATOR}{filesize}".encode())
            with open(filename, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    conexionSocket.sendall(bytes_read)
        else:
            mensajeRespuesta = "404: Not Found"
            print(mensajeRespuesta)
            conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    elif 'help' == mensaje:
        mensajeRespuesta = """
        Commands:
            get [filename] : Retrieve file
            help           : Show help menu
        """
        print(mensajeRespuesta)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))

    elif mensaje == "obj_list":

        string = "\nServer files: "
        for file in currentData:
            string += "\n- " + file

        if string == "\nServer files: ":
            string += "\nEmpty Server!"

        print(string)
        conexionSocket.send(bytes(string, "utf-8"))

    else:
        mensajeRespuesta = "Invalid command :("
        print(mensajeRespuesta)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))

    conexionSocket.close()
    
