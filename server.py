from email import message
from socket import *
from dataReader import update_csv_file

s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("+\nIP Address: {}\n".format(s.getsockname()[0]))
s.close()

servidorPuerto = 12001
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
currentData = update_csv_file()
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    lm = mensaje.lower()
    print("Mensaje recibido de ", clienteDireccion)
    if lm == 'quithipersecreto':
        conexionSocket.close()
        break
    if 'get' in lm:
        m = lm.split(' ')
        if m[1] in currentData:
            mensajeRespuesta = "File found!"
            print(mensajeRespuesta)
            conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
        else:
            mensajeRespuesta = "File not found!" + "\ncurrent files: \n" + str(currentData)
            print(mensajeRespuesta)
            conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    elif 'help' == lm:
        mensajeRespuesta = """
        Commands:
            get [filename] : Retrieve file
            help           : Show help menu
        """
        print(mensajeRespuesta)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    else:
        mensajeRespuesta = "Invalid command :("
        print(mensajeRespuesta)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))

    conexionSocket.close()
    