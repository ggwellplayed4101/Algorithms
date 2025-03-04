import time, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from list_generator import list_generator, print_list_details

def main():
    unsorted_list = list_generator()

    start = time.perf_counter()
    sorted_list = shell_sort(unsorted_list)
    end = time.perf_counter()

    elapsed_time = end - start

    print(f"Time taken by shell_sort: {elapsed_time:.7f} seconds")

def shell_sort(list):
    gap = len(list) // 2

    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i - gap

            while j>=0 and temp < list[j]:
                list[j + gap] = list[j]
                j = j - gap 
            
            list[j + gap] = temp
        gap //= 2
    return list

if __name__ == "__main__":
    main()      