package main

import (
    "fmt"
    "math/rand"
    "sort"
    "github.com/alok87/goutils/pkg/random"
    "github.com/alok87/goutils/pkg/unique"
)

func binarySearch(arr []int, noSearch int, low int, high int) (bool){
    if high < low {
        return false
    }
    middle := (high+low)/2
    if arr[middle] == noSearch {
        return true
    } else if arr[middle] < noSearch {
        return binarySearch(arr, noSearch, middle+1, high)
    } else {
        return binarySearch(arr, noSearch, low, middle-1)
    }
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
    found := binarySearch(uniqueArr, noSearch, 0, len(uniqueArr)-1)
    if found {
        fmt.Println(noSearch, "found") 
    } else {
        fmt.Println(noSearch, "not found")
    }
}
