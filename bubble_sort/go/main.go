package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("This is a Bubble Sort")
	bubble_sort()
}

func bubble_sort() {

	var numbers []int = random_arr(10)
	fmt.Printf("Before sorting: %v\n", numbers)

	for i := 0; i < 8; i++ {
		for j := 0; j < 8-i; j++ {
			if numbers[j] > numbers[j+1] {
				var temp int = numbers[j+1]
				numbers[j+1] = numbers[j]
				numbers[j] = temp
			}
		}

	}

	fmt.Printf("After sorting: %v", numbers)

}

func random_arr(size int) []int {
	random_list := make([]int, size)
	for i := 0; i < size; i++ {
		random_list[i] = rand.Intn(10)
	}
	return random_list
}
