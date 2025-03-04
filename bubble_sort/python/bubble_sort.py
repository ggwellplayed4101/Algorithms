import time, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from list_generator import list_generator

def main():
    unsorted_list = list_generator()

    start = time.perf_counter()
    sorted_list = bubble_sort(unsorted_list)
    end = time.perf_counter()

    elapsed_time = end - start

    print(f"Time taken by bubble_sort: {elapsed_time:.7f} seconds")

def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

if __name__ == "__main__":
    main()