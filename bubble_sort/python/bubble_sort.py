import time, random

LIST_SIZE = 1000
ITERATIONS = 10

def main():
    print("This is a Bubble Sort")

    unsorted_list = [random.randint(0, 10000) for _ in range(LIST_SIZE)]

    print(f"The size of the list is {LIST_SIZE}")
    print(f"Before Sorting: {unsorted_list[0:10]} ... {unsorted_list[-10:]}")

    start = time.time()
    sorted_list = bubble_sort(unsorted_list)
    end = time.time()

    elapsed_time = end - start

    print(f"After Sorting: {sorted_list[0:10]} ... {unsorted_list[-10:]}")
    print(f"Average elapsed time: {elapsed_time / ITERATIONS:.7f} seconds")

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