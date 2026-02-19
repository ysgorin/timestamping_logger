# timestamping_logger.py

# Dependencies
from datetime import datetime
from time import sleep

def timestamping_logger(own_function):
    def wrapper(a, b):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '-', own_function.__name__)
        own_function(a, b)
    return wrapper

@timestamping_logger
def add_nums(a, b):
    print(a, "+", b, '=', a+b)

@timestamping_logger
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
