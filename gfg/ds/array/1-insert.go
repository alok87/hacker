package main

import (
    "fmt"
    "math/rand"
    "time"
)

func initArr(arr []int) []int {
    rand.Seed(int64(time.Now().Nanosecond()))

    for i:=0; i<= len(arr) - 1; i++ {
        arr[i] = rand.Int()
    }
    
    return arr
}

func main() {
    arr := make([]int, 10)
    arr = initArr(arr)
    fmt.Println("Slice before insertion ", arr)
    arr = append(arr, 82)
    fmt.Println("Slice after insertion ", arr)
}
