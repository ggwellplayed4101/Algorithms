// Bubble Sort

package main

import (
	"fmt"
	"math/rand"
	"time"
)

const size int = 1000

var unsorted_list []int = random_arr(size)

func main() {
	fmt.Println("This is a Insetion Sort")

	fmt.Println("The size of the list is", size)
	fmt.Println("Before Sorting:", unsorted_list[0:10], "...", unsorted_list[size-10:])

	start := time.Now()
	var sorted_list []int = insertion_sort(unsorted_list)
	elapsed := time.Since(start).Seconds()

	fmt.Println("After Sorting:", sorted_list[0:10], "...", sorted_list[size-10:])
	fmt.Println("Execution time:", elapsed, "seconds")

}

func insertion_sort(list []int) []int {
	length := len(list)
	for i := 1; i < length; i++ {
		j := i - 1
		temp := list[i]

		for j >= 0 && temp < list[j] {
			list[j+1] = list[j]
			j -= 1
		}

		list[j+1] = temp
	}
	return list

}

func random_arr(size int) []int {
	random_list := make([]int, size)
	for i := 0; i < size; i++ {
		random_list[i] = rand.Intn(10001)
	}
	return random_list
}
