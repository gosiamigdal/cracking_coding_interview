from __future__ import print_function

def fizz_buzz_logical(n):
    for i in range(n + 1):
        (i % 15 == 0 and (print("FizzBuzz") or True)) or \
        (i % 3 == 0 and (print("Buzz") or True)) or \
        (i % 5 == 0 and (print("Fizz") or True)) or \
        (print(i))


fizz_buzz_logical(100)





