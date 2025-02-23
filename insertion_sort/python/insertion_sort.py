import random, timeit

LIST_SIZE = 1000
ITERATIONS = 10

def main():
    print("This is a Insertion Sort")

    unsorted_list = [random.randint(0, 10000) for _ in range(LIST_SIZE)]

    print(f"The size of the list is {LIST_SIZE}")
    print(f"Before Sorting: {unsorted_list[0:10]} ... {unsorted_list[-10:]}")
    sorted_list = insertion_sort(unsorted_list)
    print(f"After Sorting: {sorted_list[0:10]} ... {unsorted_list[-10:]}")

    elapsed_time = timeit.timeit(lambda: insertion_sort(unsorted_list.copy()), number = ITERATIONS)
    print(f"Average elapsed time: {elapsed_time / ITERATIONS:.7f} seconds")

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i -1
        temp = list[i]

        if temp < list[j] and j>=0:
            list[j+1] = list[j]
            j -= 1
        
        list[j+1] = temp
    
    return list

if __name__ == "__main__":
    main()