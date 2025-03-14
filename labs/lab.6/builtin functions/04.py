import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # таймер
    return math.sqrt(number)

num, delay = map(int, input("Введите число и таймер задержки: ").split())

result = delayed_sqrt(num, delay)
print(f"Квадратный корень из {num} после {delay} миллисекунд: {result}")
