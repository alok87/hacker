package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getSequenceIndex(x int, lastAnswer int, N int) int {
	seq := (x ^ lastAnswer) % N
	// fmt.Printf("\n(%d^%d)%s%d=%d\n", x, lastAnswer, "%", N, seq)
	return seq
}

func dynamicArray() {

	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	lineSplitted := strings.Split(strings.TrimSuffix(line, "\n"), " ")

	N, _ := strconv.Atoi(lineSplitted[0])
	Q, _ := strconv.Atoi(lineSplitted[1])

	lastAnswer := 0
	seqList := make([][]int, N)
	queryList := make([][]string, 0)

	for i := 0; i < N; i++ {
		seqList[i] = make([]int, 0)
	}

	for j := 1; j <= Q; j++ {
		query, _ := reader.ReadString('\n')
		queryValues := strings.Split(strings.TrimSuffix(query, "\n"), " ")
		queryList = append(queryList, queryValues)
	}

	for j := 0; j < Q; j++ {
		queryType, _ := strconv.Atoi(queryList[j][0])
		x, _ := strconv.Atoi(queryList[j][1])
		y, _ := strconv.Atoi(queryList[j][2])

		seq := getSequenceIndex(x, lastAnswer, N)

		switch queryType {
		case 1:
			seqList[seq] = append(seqList[seq], y)
		case 2:
			id := y % len(seqList[seq])
			lastAnswer = seqList[seq][id]
			fmt.Println(lastAnswer)
		}
	}
}
