for i in range(1, 10000):
    print("FizzBuzz" if not i % 15 else "Fizz" if not i % 3 else "Buzz" if not
          i % 5 else i, end=" ")
