from socket import *
from time import sleep

# ConexiÃ³n con el cliente
servidorPuerto = 12001
servidorSocket = socket(AF_INET, SOCK_STREAM)
servidorSocket.bind(('', servidorPuerto))
servidorSocket.listen(1)
print("Web Cache Ready")

while 1:
    conexionSocket, webDireccion = servidorSocket.accept()
    print("Conection established: ", webDireccion)
    mensaje = str(conexionSocket.recv(1024), "utf-8")
    print("Recieved message from: ", webDireccion)
    mensaje_server = mensaje
    mensaje = mensaje.split(" ")

    if mensaje[0] == "GET":

        with open("dir_cache.txt", "r") as cache:
            files = cache.readlines()
        cache.close()

        files = [file.replace("\n", "") for file in files]

        if mensaje[1] in files:
            mensajeRespuesta = f"STATUS CODE:\n304: NOT MODIFIED\n- {mensaje[1]}"
            print(mensajeRespuesta)
            sleep(0.05)
            conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
            conexionSocket.close()

        else:
            # Conectarse al servidor
            servidorNombre = "127.0.0.1"
            servidorPuerto = 12000
            webSocket = socket(AF_INET, SOCK_STREAM)
            webSocket.connect((servidorNombre, servidorPuerto))
            webSocket.send(bytes(mensaje_server, "utf-8"))
            mensajeRespuesta = webSocket.recv(1024)
            mensajeRespuesta2 = str(mensajeRespuesta, "utf-8")
            webSocket.close()

            if str(mensajeRespuesta, "utf-8") == "404: Not Found":
                print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
            else:
                mensajeRespuesta2 = "File found!\n200: OK\n- " + str(mensajeRespuesta, "utf-8")
                print(mensajeRespuesta2)

                with open('dir_cache.txt', 'a') as files:
                    print(str(mensajeRespuesta, "utf-8"), file=files)
                files.close()

            sleep(0.25)
            conexionSocket.send(bytes(mensajeRespuesta2, "utf-8"))
            conexionSocket.close()
            webSocket.close()

    elif mensaje[0] == "delete_cache":
        f = open("dir_cache.txt", "w")
        f.truncate()
        f.close()
        conexionSocket.send(bytes("Cache deleted!", "utf-8"))
        conexionSocket.close()

    elif mensaje[0] == "cache_list":

        with open("dir_cache.txt", "r") as cache:
            files = cache.readlines()
        cache.close()

        string = "\nCached files:\n"
        for i in range(len(files)):
            string += "- " + files[i]

        if string == "\nCached files:\n":
            string += "\nEmpty cache!"

        conexionSocket.send(bytes(string, "utf-8"))
        conexionSocket.close()


    if mensaje[0] == "obj_list":
        # Conectarse al servidor
        servidorNombre = "127.0.0.1"
        servidorPuerto = 12000
        webSocket = socket(AF_INET, SOCK_STREAM)
        webSocket.connect((servidorNombre, servidorPuerto))
        webSocket.send(bytes(mensaje_server, "utf-8"))
        mensajeRespuesta = webSocket.recv(1024)
        mensajeRespuesta2 = str(mensajeRespuesta, "utf-8")
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
        webSocket.close()

        conexionSocket.send(bytes(mensajeRespuesta2, "utf-8"))
        conexionSocket.close()
        webSocket.close()



    else:
        conexionSocket.close()
