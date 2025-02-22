import timeit
import random

LIST_SIZE = 1000
ITERATIONS = 10

def main():
    print("This is a Bubble Sort")

    unsorted_list = [random.randint(0, 10000) for _ in range(LIST_SIZE)]

    print(f"The soze of the list is {LIST_SIZE}")
    print(f"Before Sorting: {unsorted_list[0:10]} ... {unsorted_list[-10:]}")
    sorted_list = bubble_sort(unsorted_list)
    print(f"After Sorting: {sorted_list[0:10]} ... {unsorted_list[-10:]}")

    elapsed_time = timeit.timeit(lambda: bubble_sort(unsorted_list.copy()), number = ITERATIONS)
    print(f"Average elapsed time: {elapsed_time / ITERATIONS:.6f} seconds")

def bubble_sort(numbers):
    for j in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
    return numbers

if __name__ == "__main__":
    main()