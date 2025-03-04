package main

import (
	"fmt"
	"time"

	utils "github.com/ggwellplayed4101/Algorithms/list_generator"
)

const size int = 100000

func main() {
	unsorted_list := utils.Random_Arr(size)

	start := time.Now()
	insertion_sort(unsorted_list)
	elapsed := time.Since(start).Seconds()

	fmt.Println("Time taken by Shell Sort:", elapsed, "seconds")
}

func insertion_sort(list []int) []int {
	length := len(list)
	gap := length / 2
	for gap > 0 {
		for i := gap; i < length; i++ {
			temp := list[i]
			j := i - gap
			for j >= gap && list[j] > temp {
				list[j+gap] = list[j]
				j = j - gap
			}
			list[j+gap] = temp
		}
		gap = gap / 2
	}
	return list
}
