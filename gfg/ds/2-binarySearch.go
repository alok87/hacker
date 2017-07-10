package main

import (
    "fmt"
    "github.com/alok87/goutils/pkg/random"
)

func main() {
    arr := random.RangeInt(1, 100, 10)
    fmt.Println(arr)
}
