package basic

import "fmt"

func FooVars() {
	var i int = 20
	fmt.Printf("%T, %[1]v\n", i)

	j := 10.2
	fmt.Printf("%T, %[1]v\n", j)

	arr := [3]int{1, 2, 3}
	fmt.Printf("%T, %[1]v\n", arr)

	sl := []rune{'a', 'b', 'ç', 'd'}
	fmt.Printf("%T, %[1]v\n", sl)

	m := map[string]int{"foo": 1}
	fmt.Printf("%T, %[1]v\n", m)

	s := "hello"
	fmt.Printf("%T, %[1]v\n", s)

	b := false
	fmt.Printf("%T, %[1]v\n", b)
}
