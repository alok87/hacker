package main

import (
    "fmt"
    "math/rand"
    "sort"
    "github.com/alok87/goutils/pkg/random"
    "github.com/alok87/goutils/pkg/unique"
)

func binarySearch(arr []int, noSearch int) (bool){
    var middle int
    middle = (len(arr)/2) 
    if middle > len(arr) - 1 {
        return false
    }
    if middle == 1 && noSearch != arr[middle] {
        return false
    }
    if noSearch == arr[middle] {
        return true
    } else if noSearch > arr[middle] {
        return binarySearch(arr[middle:], noSearch)
    } else {
        return binarySearch(arr[:middle], noSearch)
    }
    return false
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
    found := binarySearch(uniqueArr, noSearch)
    if found {
        fmt.Println(noSearch, "found") 
    } else {
        fmt.Println(noSearch, "not found")
    }
}
