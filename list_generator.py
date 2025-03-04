import random

def list_generator (size=1000, min=0, max=10000):
    return [random.randint(min, max) for _ in range(size)]

def print_list_details(lst):
    print(f"List length: {len(lst)}")
    print(f"First 10 numbers: {lst[:10]}")
    print(f"Last 10 numbers: {lst[-10:]}")