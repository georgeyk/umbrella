package basic

// import "fmt"

func BinSearch(arr []int, elem int) int {
	left := 0
	right := len(arr) - 1
	for left <= right {
		mid := (left + right) / 2
		if arr[mid] < elem {
			left = mid + 1
		} else if arr[mid] > elem {
			right = mid - 1
		} else {
			return mid
		}
	}
	return -1
}
