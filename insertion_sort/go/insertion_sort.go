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
	insertion_sort(unsorted_list)
	elapsed := time.Since(start).Seconds()
	fmt.Println("Time taken by insertion sort:", elapsed, "seconds")
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
