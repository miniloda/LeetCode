package main

import (
	"fmt"
)

func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	max_area := 0

	for left < right {
		length := 0
		if height[left] < height[right] {
			length = height[left]
			left++
		} else {
			length = height[right]
			right--
		}

		area := length * (right - left + 1) // Calculate the area correctly
		if area > max_area {
			max_area = area
		}
	}
	return max_area
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7})) // Pass the slice correctly
}
