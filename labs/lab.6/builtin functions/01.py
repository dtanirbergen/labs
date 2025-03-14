import math

def multiply(numbers):
    return math.prod(numbers)

nums = list(map(int, input().split()))

print("Произведение чисел:", multiply(nums))
