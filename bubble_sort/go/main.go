package main

import (
	"fmt"
)

func main() {
	fmt.Println("This is a Bubble Sort")
	bubble_sort()
}

func bubble_sort() {
	var numbers []uint8 = []uint8{5, 4, 3, 1, 8, 6, 9, 7, 2}
	fmt.Printf("Before sorting: %v\n", numbers)

	for i := 0; i < 8; i++ {
		for j := 0; j < 8-i; j++ {
			if numbers[j] > numbers[j+1] {
				var temp uint8 = numbers[j+1]
				numbers[j+1] = numbers[j]
				numbers[j] = temp
			}
		}

	}

	fmt.Printf("After sorting: %v", numbers)

}
