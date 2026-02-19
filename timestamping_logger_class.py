# timestamping_logger.py

# Dependencies
from datetime import datetime
from time import sleep

class TimestampingLogger:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, a, b):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '-', self.func.__name__)
        self.func(a, b)

@TimestampingLogger
def add_nums(a, b):
    print(a, "+", b, '=', a+b)

@TimestampingLogger
def mul_nums(a, b):
    print(a, "x", b, '=', a*b)

add_nums(1, 3)
sleep(2)
mul_nums(4, 5)
sleep(2)
add_nums(10, 30)
sleep(2)
add_nums(6, 10)
sleep(1)
