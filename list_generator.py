import random

def list_generator (size=1000, min=0, max=10000):
    return [random.randint(min, max) for _ in range(size)]
