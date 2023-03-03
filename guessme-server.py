import random
import socket
import selectors
import types

HOST = "127.0.0.1"
PORT = 65432

class Game:
    def __init__(self):
        self.max_guess = 10
        self.guesses_left = self.max_guess
        self.answer = random.randint(1, 100)

    def handle_guess(self, guess):
        self.guesses_left -= 1
        if guess == self.answer:
            return "Correct! You win!\n"
        elif guess < self.answer:
            return "Too low.\n"
        else:
            return "Too high.\n"

sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {(HOST, PORT)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

socks = []

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    game = Game()
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"", game=game)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    socks.append(conn)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                 accept_wrapper(key.fileobj)
            else:
                pass
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()