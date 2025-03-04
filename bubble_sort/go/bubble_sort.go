package main

import (
	"fmt"
	"time"

	utils "github.com/ggwellplayed4101/Algorithms/list_generator"
)

const size int = 1000

func main() {
	unsorted_list := utils.Random_Arr(size)

	start := time.Now()
	bubble_sort(unsorted_list)
	elapsed := time.Since(start).Seconds()

	fmt.Println("Execution time:", elapsed, "seconds")

}

func bubble_sort(list []int) []int {
	length := len(list)
	for i := 0; i < length-1; i++ {
		for j := 0; j < length-1-i; j++ {
			if list[j] > list[j+1] {
				var temp int = list[j+1]
				list[j+1] = list[j]
				list[j] = temp
			}
		}
	}
	return list

}
