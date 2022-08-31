from socket import *
from random import randint  # for later use (easter egg)
from time import sleep

servidorNombre = "127.0.0.1"
servidorPuerto = 12001


print("""
 __          __  _        _____           _                  
 \ \        / / | |      / ____|         | |                 
  \ \  /\  / /__| |__   | |     __ _  ___| |__   ___         
   \ \/  \/ / _ \ '_ \  | |    / _` |/ __| '_ \ / _ \        
    \  /\  /  __/ |_) | | |___| (_| | (__| | | |  __/        
     \/  \/ \___|_.__/   \_____\__,_|\___|_| |_|\___|                                                                                                             
   _____ _                 _       _                         
  / ____(_)               | |     | |                        
 | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __             
  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|            
  ____) | | | | | | | |_| | | (_| | || (_) | |     _   _   _ 
 |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|    (_) (_) (_)                                                   
                                                             """)


print("By: \n- Juan Nicolas Sepulveda Arias\n- Juan Esteban Velandia\n -Juan David Martinez\n\nGROUP NÂ° 2\n")


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
            print("""
               _____                 _   ____               _   _   _ 
              / ____|               | | |  _ \             | | | | | |
             | |  __  ___   ___   __| | | |_) |_   _  ___  | | | | | |
             | | |_ |/ _ \ / _ \ / _` | |  _ <| | | |/ _ \ | | | | | |
             | |__| | (_) | (_) | (_| | | |_) | |_| |  __/ |_| |_| |_|
              \_____|\___/ \___/ \__,_| |____/ \__, |\___| (_) (_) (_)
                                                __/ |                 
                                               |___/                  """)
            accepted = True
            break

        elif command[0] == "brew_coffee":
            print("Brewing coffee", end="")
            for i in range(20):
                print(".", end="")
                r = randint(1, 8)
                sleep(1 * r / 20)

            c = input("\nFeeling lucky? (Y/N): \n")
            if c and c.lower() == "y":
                server_response = """
            
                  _    _                                                 _ 
                 | |  | |                                               | |
                 | |__| | ___ _ __ ___   _   _  ___  _   _    __ _  ___ | |
                 |  __  |/ _ \ '__/ _ \ | | | |/ _ \| | | |  / _` |/ _ \| |
                 | |  | |  __/ | |  __/ | |_| | (_) | |_| | | (_| | (_) |_|
                 |_|  |_|\___|_|  \___|  \__, |\___/ \__,_|  \__, |\___/(_)
                                          __/ |               __/ |        
                                         |___/               |___/         
                            
                
                                        (
                                        )     (
                                 ___...(-------)-....___
                             .-""       )    (          ""-.
                       .-'``'|-._             )         _.-|
                      /  .--.|   `""---...........---""`   |
                     /  /    |                             |
                     |  |    |                             |
                      \  \   |                             |
                       `\ `\ |                             |
                         `\ `|                             |
                         _/ /\                             /
                        (__/  \                           /
                     _..---""` \                         /`""---.._
                  .-'           \                       /          '-.
                 :               `-.__             __.-'              :
                 :                  ) ""---...---"" (                 :
                  '._               `"--...___...--"`              _.'
                    \""--..__                              __..--""/
                     '._     ""-----.....______.....----""'     _.'
                        `""--..,,_____            _____,,..--""`
                                      `""------""`"""


            elif c.lower() == "n":
                server_response = """
                
                  _  _  __  ___         _____ _                      _                         _     _ 
                 | || |/_ |/ _ \   _   |_   _( )                    | |                       | |   | |
                 | || |_| | (_) | (_)    | | |/ _ __ ___     __ _   | |_ ___  __ _ _ __   ___ | |_  | |
                 |__   _| |> _ <         | |   | '_ ` _ \   / _` |  | __/ _ \/ _` | '_ \ / _ \| __| | |
                    | | | | (_) |  _    _| |_  | | | | | | | (_| |  | ||  __/ (_| | |_) | (_) | |_  |_|
                    |_| |_|\___/  (_)  |_____| |_| |_| |_|  \__,_|   \__\___|\__,_| .__/ \___/ \__| (_)
                                                                                  | |                  
                                                                                  |_|              
                    
                                                                     ;,'
                                                             _o_    ;:;'
                                                         ,-.'---`.__ ;
                                                        ((j`=====',-'
                                                         `-\     /
                                                            `-=-'     """
            else:
                server_response = """
                
                  _____ _   _                     _                                       _ _                          
                 |_   _| | ( )                   | |                                     ( ) |                         
                   | | | |_|/ ___   ___  __ _  __| |  _   _  ___  _   _    ___ __ _ _ __ |/| |_    _____   _____ _ __  
                   | | | __| / __| / __|/ _` |/ _` | | | | |/ _ \| | | |  / __/ _` | '_ \  | __|  / _ \ \ / / _ \ '_ \ 
                  _| |_| |_  \__ \ \__ \ (_| | (_| | | |_| | (_) | |_| | | (_| (_| | | | | | |_  |  __/\ V /  __/ | | |
                 |_____|\__| |___/ |___/\__,_|\__,_|  \__, |\___/ \__,_|  \___\__,_|_| |_|  \__|  \___| \_/ \___|_| |_|
                   __      _ _                 _       __/ |                   _   _                                   
                  / _|    | | |               (_)     |___/ |                 | | (_)                                  
                 | |_ ___ | | | _____      __  _ _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___                   
                 |  _/ _ \| | |/ _ \ \ /\ / / | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|                  
                 | || (_) | | | (_) \ V  V /  | | | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \                  
                 |_| \___/|_|_|\___/ \_/\_/   |_|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/                  
                                                                                                       
                                                                                                       """

        elif command[0] == "help":
            print("""help:\n
                     \n"""
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
                "help", "You're already here..."))

            server_response = ""

        else:
            print("Invalid command!")
            continue

        print(server_response)

        if accepted:
            clienteSocket.close()
