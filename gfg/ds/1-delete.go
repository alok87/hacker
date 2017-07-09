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


func deleteElem(arr []int, elemToDel int) []int {
    var pos int
    for i:=0; i<= len(arr) - 1; i++ {
        if arr[i] == elemToDel {
            pos = i
            break
        }
    }
    arr = append(arr[:pos], arr[pos+1:]...)
    return arr
}

func main() {
    arr := make([]int, 10)
    arr = initArr(arr)
    arr = append(arr, 82)
    arr = append(arr, 85)
    fmt.Println("Slice before deletion", arr)
    arr = deleteElem(arr, 82)
    fmt.Println("Slice after deletion", arr)
}
