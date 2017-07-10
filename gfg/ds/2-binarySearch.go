package main

import (
    "fmt"
    "math/rand"
    "sort"
    "github.com/alok87/goutils/pkg/random"
    "github.com/alok87/goutils/pkg/unique"
)

func binarySearch(arr []int, noSearch int) (bool, int){
    var middle int
    for len(arr) > 0 {
        middle = (len(arr) / 2) + 1
        if middle > len(arr) - 1 {
            return false, -1
        }
        if noSearch == arr[middle] {
            return true, middle
        } else if noSearch > arr[middle] {
            arr = arr[middle:]
        } else {
            arr = arr[:middle]
        }
    }
    return false, -1
}

func main() {
    min := 1
    max := 20
    n := 10
    arr := random.RangeInt(min, max, n)
    uniqueArr := unique.Ints(arr)
    sort.Ints(uniqueArr)
    noSearch := rand.Intn(max) + min
    fmt.Println("Searching for:", noSearch)
    fmt.Println("Array=", uniqueArr)
    found, pos := binarySearch(uniqueArr, noSearch)
    if found {
        fmt.Println(noSearch, "found at pos:", pos)
    } else {
        fmt.Println(noSearch, "not found")
    }
}
