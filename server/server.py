from socket import *
from dataReader import update_csv_file

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
            print(mensajeRespuesta)
            conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
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
    
