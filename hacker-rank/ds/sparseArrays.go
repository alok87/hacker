package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sparseArrays() {

	reader := bufio.NewReader(os.Stdin)

	// Number of strings
	line, _ := reader.ReadString('\n')
	N, _ := strconv.Atoi(strings.TrimSuffix(line, "\n"))

	// Input strings
	stringList := make([]string, 0)
	for i := 0; i < N; i++ {
		s, _ := reader.ReadString('\n')
		stringList = append(stringList, strings.TrimSuffix(s, "\n"))
	}

	// Number of queries
	line, _ = reader.ReadString('\n')
	Q, _ := strconv.Atoi(strings.TrimSuffix(line, "\n"))

	// Input queries
	queryList := make([]string, 0)
	for i := 0; i < Q; i++ {
		q, _ := reader.ReadString('\n')
		queryList = append(queryList, strings.TrimSuffix(q, "\n"))
	}

	for j := 0; j < Q; j++ {
		count := 0
		for k := 0; k < N; k++ {
			if stringList[k] == queryList[j] {
				count++
			}
		}
		fmt.Println(count)
	}

}
