package main

import (
    "fmt"
    "math/rand"
    "sort"
    "github.com/alok87/goutils/pkg/random"
    "github.com/alok87/goutils/pkg/unique"
)

func binarySearch(low int,high int, arr []int, no int) (bool, int){
    if high < low {
        return false, -1
    }
    middle := (low+high)/2
    if arr[middle] == no {
        return true, middle
    } else if arr[middle] < no {
        return binarySearch(middle+1, high, arr, no)
    } else {
        return binarySearch(low, middle-1, arr, no)
    }
}

func deleteElem(arr []int, pos int) []int {
    var newArr []int
    newArr = append(newArr, arr[0:pos]...)
    if pos != len(arr) - 1 {
        newArr = append(newArr, arr[pos+1:]...)
    }
    return newArr
}

func main() {
    min := 1
    max := 20
    n := 10
    arr := random.RangeInt(min, max, n)
    uniqueArr := unique.Ints(arr)
    sort.Ints(uniqueArr)
    noDel := rand.Intn(max) + min
    noDel = 20
    fmt.Println("Deleting:", noDel)
    fmt.Println("Array=", uniqueArr)
    found, pos := binarySearch(0, len(uniqueArr)-1, uniqueArr, noDel)
    if found {
        fmt.Println(noDel, "to be deleted at pos:", pos, uniqueArr)
        uniqueArr = deleteElem(uniqueArr, pos)
        fmt.Println(noDel, "deleted at pos:", pos, uniqueArr)
    } else {
        fmt.Println(noDel, "not found", uniqueArr)
    }
}
