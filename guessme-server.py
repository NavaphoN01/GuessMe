import random

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