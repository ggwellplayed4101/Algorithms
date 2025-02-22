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
	fmt.Println("This is a Bubble Sort")

	fmt.Println("The size of the list is", size)
	fmt.Println("Before Sorting:", unsorted_list[0:10], "...", unsorted_list[size-10:])

	start := time.Now()
	var sorted_list []int = bubble_sort(unsorted_list)
	elapsed := time.Since(start).Seconds()

	fmt.Println("After Sorting:", sorted_list[0:10], "...", sorted_list[size-10:])
	fmt.Println("Execution time:", elapsed, "seconds")

}

func bubble_sort(numbers []int) []int {
	length := len(numbers)
	for i := 0; i < length-1; i++ {
		for j := 0; j < length-1-i; j++ {
			if numbers[j] > numbers[j+1] {
				var temp int = numbers[j+1]
				numbers[j+1] = numbers[j]
				numbers[j] = temp
			}
		}
	}
	return numbers

}

func random_arr(size int) []int {
	random_list := make([]int, size)
	for i := 0; i < size; i++ {
		random_list[i] = rand.Intn(10001)
	}
	return random_list
}
