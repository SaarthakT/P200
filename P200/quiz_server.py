import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

questions = [
    "What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n_c.Patty\nd.Pizza",
    "Water boils at 212 Units at which scale? \n a.Fahrenheit\n b Celsius.\n c.Rankine \n d.Kelvin",
    "Which sea creature has three hearts? \n a.Dolphin\n b.Octopus \n c.Walrus\nd.Seal",
    "Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh",
    "How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
    "How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4", "What element does not exist? \n a.Xf\n b.Re\n c.Si\n d. Pa", "How many states are there in India? \n a.24\n b.29\n c.30\n d.31", "Who invented the telephone? \n a.A.G Bell\n b.John Wick\n c. Thomas Edison\n d.G Marconi",
    "Who is Loki? \n a.God of Thunder\n b.God of Dwarves \n c.God of Mischief\n d. God of Gods",
    "Who was the first Indian female astronaut ? \n a.Sunita Williams\n b.Kalpana Chawla\n c.None of them\n d.Both of them ",
    "What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\n d.Australia",
    "The beaver is the national embelem of which country? \n a.Zimbabwe\n b.Iceland \n c.Argentina\n d.Canada",
    "How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d.8",
    "Hg stands for? \n a.Mercury\n b.Hulgerium\n £.Argenine\n d.Halfnium"
    "Who gifted the Statue of Libery to the US? \n a.Brazil\n b. France\n c.Wales\n d.Germany",
    "Which planet is closest to the sun? \n a.Mercury\n b. Pluto\n c.Earth\nd.Venus"
]

def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print ("<" + addr[0] + "> " + message)

                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients !=connection :
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()
