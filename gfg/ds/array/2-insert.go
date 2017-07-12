package main

import (
    "fmt"
    "math/rand"
)

func insert(arr [5]int, elem int) ([5]int, bool) {
    i := len(arr) - 2
    for ;(i>=0 && arr[i] > elem); i-- {
        arr[i+1] = arr[i] 
    }
    arr[i+1] = elem
    return arr, true
}

func main() {
    min := 1
    max := 20
    newArr := [5]int{1, 2, 3, 5}
    number := rand.Intn(max) + min
    number = 0 
    fmt.Println("Inserting:", number)
    fmt.Println("Array=", newArr)
    arr2, isInserted := insert(newArr, number)
    fmt.Println("Array=", arr2, isInserted) 
}
