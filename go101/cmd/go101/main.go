package main

import (
	"fmt"
	"go101/basic"
)

func main() {
	fmt.Println("FooVars")
	basic.FooVars()

	fmt.Println("BinSearch")
	ret := basic.BinSearch([]int{1, 2, 3, 4, 5, 6, 7}, 0)
	fmt.Println(ret, ret != -1)
	ret = basic.BinSearch([]int{1, 2, 3, 4, 5, 6, 7}, 7)
	fmt.Println(ret, ret != -1)
}
