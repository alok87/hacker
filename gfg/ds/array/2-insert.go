package main

import (
    "fmt"
    "math/rand"
    "sort"
    "github.com/alok87/goutils/pkg/random"
    "github.com/alok87/goutils/pkg/unique"
)

func insert(arr []int, elem int) ([]int, bool) {
    

}

func main() {
    min := 1
    max := 20
    n := 10
    arr := random.RangeInt(min, max, n)
    uniqueArr := unique.Ints(arr)
    sort.Ints(uniqueArr)
    n := rand.Intn(max) + min
    fmt.Println("Inserting:", n)
    fmt.Println("Array=", uniqueArr)
    newArr, isInserted := insert(uniqueArr, noSearch)
    fmt.Println("Array=", newArr, isInserted) 
}
