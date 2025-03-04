import time
from list_generator import list_generator


def main():
    unsorted_list = list_generator()

    start = time.time()
    sorted_list = bubble_sort(unsorted_list)
    end = time.time()

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