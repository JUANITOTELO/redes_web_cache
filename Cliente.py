from socket import *
from random import randint  # for later use (easter egg)
from time import sleep

servidorNombre = "127.0.0.1"
servidorPuerto = 12001

command = print("Enter a command: \n type \"help\" to view available commands\n")
accepted = False

while True:
    command = input("(client) $> ")
    if command != "":

        clienteSocket = socket(AF_INET, SOCK_STREAM)
        clienteSocket.connect((servidorNombre, servidorPuerto))
        command = command.split()

        if command[0] in ["delete_cache", "obj_list", "cache_list", "GET"]:

            if command[0] == "GET":

                while len(command) == 1:
                    command += input("Enter object name: ").split()

                if len(command) > 2:
                    print("Invalid \"GET\" input: try replacing blank spaces \" \" with underscores \"_\"")
                    continue

            elif len(command) != 1:
                print(f"invalid {command[0]} input: this command doesn't accept any extra parameter(s)")
                continue

            message = " ".join(command)
            clienteSocket.send(bytes(message, "utf-8"))
            server_response = clienteSocket.recv(1024)
            server_response = str(server_response, "utf_8")
            accepted = True

        elif command[0] == "exit":
            print("Good Bye!")
            accepted = True
            break

        elif command[0] == "upper":
            message = input("Write a message!: ")
            clienteSocket.send(bytes(message, "utf-8"))
            server_response = clienteSocket.recv(1024)
            server_response = str(server_response, "utf_8")
            accepted = True

        elif command[0] == "brew_coffee":
            print("Brewing coffee", end="")
            for i in range(20):
                print(".", end="")
                r = randint(1, 8)
                sleep(1 * r / 20)

            server_response = "\nUnable to brew coffee:\nSTATUS CODE:\n418: I'm a teapot!"

        elif command[0] == "help":
            print("""help:\n
                     \n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n"""
                  """{:<15}: {:>50}\n""".format(
                "GET", "Ask the server to send you an object",
                "delete_cache", "Delete all cached objects",
                "obj_list", "View GET-able objects from server",
                "cache_list", "View cached elements in web cache",
                "brew_coffee", "Feeling tired?",
                "exit", "Exit the client",
                "upper", "Just for testing. hopefully this got deleted :)",
                "help", "You're already here..."))

            server_response = ""

        else:
            print("Invalid command!")
            continue

        print(server_response)

        if accepted:
            clienteSocket.close()

