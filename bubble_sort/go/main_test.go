package main

import (
	"testing"
)

func benchmark_bubble_sort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		unsorted_list := random_arr(size)
		b.ResetTimer()
		bubble_sort(unsorted_list)
	}
}
