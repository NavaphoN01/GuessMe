import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Welcome to the Guess Number Game!")
    print("You have 10 guesses to guess a number between 1 and 100.")

    for i in range(10):
        guess = input("Enter your guess: ")
        s.sendall(guess.encode())
        data = s.recv(1024)
        print(data.decode())
        if b"win" in data:
            break

print("Game over.")