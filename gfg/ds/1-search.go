package main

import (
    "fmt"
)

func findElem(arr [5]int, elemToFind int) bool {
    i := 0
    for ;i <= len(arr) - 1; i++ {
        if elemToFind == arr[i] {
            return true
        }
    }
    return false 
}


func main() {
    arr := [5]int{1, 2, 4, 3, 5}
    elemToFind := 3
    if findElem(arr, elemToFind) {
        fmt.Println("Found Element ", elemToFind)
    } else {
        fmt.Println("Not Found Element ", elemToFind)
    }
}
