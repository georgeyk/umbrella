package hello

import "fmt"

const EnPrefix = "Hello, "

func main() {
	fmt.Println(Hello("world"))
}

func Hello(name string) string {
	if name == "" {
		name = "world"
	}
	return EnPrefix + name
}
