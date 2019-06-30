MAX_GUESSES = 10
START, END = 1, 100


def get_random_number():
    import random
    return random.randint(START, END)


class Game:

    def __init__(self):
        self._guesed = set()
        self.answer = get_random_number()

    def check_number(self):
        target = input("Enter your number: ")
        try:
            target = int(target)
        except ValueError:
            raise ValueError("Should be a number")
            print("Should be a number")
            return self.check_number()
        if target > END or target < START:
            raise ValueError("Should be a number")
            print(f"Number is not in scope {START}-{END}")
            return self.check_number()
        if target in self._guesed:
            raise ValueError("Should be a number")
            print("Already guessed!")
            return self.check_number()
        self._guesed.add(target)
        return target

    def __call__(self, *args, **kwargs):
        print(f"Guess a number between {START} and {END}")
        while len(self._guesed) < MAX_GUESSES:
            guess = self.check_number()
            if guess == self.answer:
                guess_str = 1 == len(self._guesed) and "attempt" or "attempts"
                print(f"It takes you {len(self._guesed)} {guess_str} to "
                      f"guess.")
                break
            low_high = "higher" if guess < self.answer else "lower"
            print(f"My number is {low_high}")
        else:
            print(f"You loose. It was {self.answer}. Try again")


if __name__ == "__main__":
    game = Game()
    game()


