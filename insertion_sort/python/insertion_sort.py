import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from list_generator import list_generator

def main():
    unsorted_list = list_generator()

    start = time.time()
    sorted_list = insertion_sort(unsorted_list)
    end = time.time()

    elapsed_time = end - start

    print(f"Time taken by insertion sort: {elapsed_time:.7f} seconds")

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i -1
        temp = list[i]

        while temp < list[j] and j>=0:
            list[j+1] = list[j]
            j -= 1
        
        list[j+1] = temp
    
    return list

if __name__ == "__main__":
    main()