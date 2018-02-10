package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func twoD() {

	sizeOfTwoDArray := 6
	widthOfHourGlass := 3
	lengthofHourGlass := 3

	reader := bufio.NewReader(os.Stdin)
	arr := make([][]int, sizeOfTwoDArray)

	for i := 0; i < sizeOfTwoDArray; i++ {
		arr[i] = make([]int, sizeOfTwoDArray)
		line, _ := reader.ReadString('\n')
		lineElements := strings.Split(strings.TrimSuffix(line, "\n"), " ")
		for j := 0; j < len(lineElements); j++ {
			arr[i][j], _ = strconv.Atoi(lineElements[j])
		}
	}

	maxHourGlassSum := -63

	for l := 0; l <= sizeOfTwoDArray-widthOfHourGlass; l++ {
		for e := 0; e <= sizeOfTwoDArray-lengthofHourGlass; e++ {
			hourGlassSum := arr[l][e] + arr[l][e+1] + arr[l][e+2] + arr[l+1][e+1] + arr[l+2][e] + arr[l+2][e+1] + arr[l+2][e+2]
			if hourGlassSum > maxHourGlassSum {
				maxHourGlassSum = hourGlassSum
			}
		}
	}

	fmt.Println(maxHourGlassSum)
}
