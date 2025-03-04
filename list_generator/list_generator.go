package list_generator

import (
	"math/rand"
)

func Random_Arr(size int) []int {
	random_list := make([]int, size)
	for i := 0; i < size; i++ {
		random_list[i] = rand.Intn(10001)
	}
	return random_list
}
