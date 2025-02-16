import time
import random

size = 1000
numbers = [random.randint(0, 10000) for _ in range(size)]

def bubble_sort(numbers):
    for j in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
    
    return numbers

def benchmark(sort_function):
    start = time.time()
    sort_function(numbers)
    end = time.time()
    time_taken = end - start
    print(f"Time elapsed: {time_taken:.6f}")

for i in range(10):
    benchmark(bubble_sort) 