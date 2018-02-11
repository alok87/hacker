package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func leftRotation() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	lineValues := strings.Split(strings.TrimSuffix(line, "\n"), " ")

	// Fill the n an d
	n, _ := strconv.Atoi(lineValues[0])
	d, _ := strconv.Atoi(lineValues[1])

	// Fill the array/slice
	line, _ = reader.ReadString('\n')
	lineValues = strings.Split(strings.TrimSuffix(line, "\n"), " ")
	arr := make([]int, 0)
	for i := 0; i < n; i++ {
		value, _ := strconv.Atoi(lineValues[i])
		arr = append(arr, value)
	}

	newArr := arr[d:]
	newArr = append(newArr, arr[:d]...)
	for i := 0; i < n; i++ {
		fmt.Printf("%d ", newArr[i])
	}
}
