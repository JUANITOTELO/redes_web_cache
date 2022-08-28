from socket import *
import csv

archivos_ex = []
with open('Archivos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        archivos_ex.append(', '.join(row))
        #print(', '.join(row))

archivos = []
for i in range(1,len(archivos_ex)):
    archivos.append(archivos_ex[i])


#Conexión con el cliente
servidorPuerto = 12001
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, webDireccion = servidorSocket.accept()
    print("Conexión establecida con ", webDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", webDireccion)
    print(mensaje)
    mensajeRespuesta1 = mensaje.upper()
    print(mensajeRespuesta1)

    if mensaje in archivos:
        mensajeRespuesta = "El archivo se encontró..."
        print(mensajeRespuesta)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
        conexionSocket.close()
    else:
    
    
    #Conectarse al servidor
        servidorNombre = "127.0.0.1" 
        servidorPuerto = 12000
        webSocket = socket(AF_INET, SOCK_STREAM)
        webSocket.connect((servidorNombre,servidorPuerto))
        mensaje = input("Ingrese un mensaje:")
        webSocket.send(bytes(mensaje, "utf-8"))
        mensajeRespuesta = webSocket.recv(1024)
        mensajeRespuesta2 = str( mensajeRespuesta, "utf-8" )
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
        webSocket.close()

        conexionSocket.send(bytes(mensajeRespuesta2, "utf-8"))
        conexionSocket.close()
    
