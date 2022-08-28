from socket import *
import csv

dir_cache_ex = []
with open('dir_cache.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        dir_cache_ex.append(', '.join(row))
        #print(', '.join(row))

dir_cache = []
for i in range(1,len(dir_cache_ex)):
    dir_cache.append(dir_cache_ex[i])


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
    mensaje_server = mensaje
    mensaje = mensaje.split(" ")
    mensajeRespuesta1 = mensaje[1].upper()
    print(mensajeRespuesta1)

    if mensaje[0] == "GET" and mensaje[1] in dir_cache:
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
        #mensaje = input("Ingrese un mensaje:")
        webSocket.send(bytes(mensaje_server, "utf-8"))
        mensajeRespuesta = webSocket.recv(1024)
        mensajeRespuesta2 = str( mensajeRespuesta, "utf-8" )
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
        webSocket.close()

        conexionSocket.send(bytes(mensajeRespuesta2, "utf-8"))
        conexionSocket.close()
    

    

    

        

    

        


