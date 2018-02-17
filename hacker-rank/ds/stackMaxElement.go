package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Stack implementation
type Stack []int

func (s Stack) push(number int) Stack {
	return append(s, number)
}

func (s Stack) pop() Stack {
	return s[:len(s)-1]

}

func (s Stack) max() int {
	max := s[0]
	for i := 1; i < len(s); i++ {
		if s[i] > max {
			max = s[i]
		}
	}
	return max
}

func stackMaxElement() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSuffix(line, "\n"))

	stack := make(Stack, 0)

	for i := 0; i < n; i++ {
		query, _ := reader.ReadString('\n')
		queryValues := strings.Split(strings.TrimSuffix(query, "\n"), " ")
		q, _ := strconv.Atoi(queryValues[0])
		switch q {
		case 1:
			val, _ := strconv.Atoi(queryValues[1])
			stack = stack.push(val)
		case 2:
			stack = stack.pop()
		case 3:
			fmt.Println(stack.max())
		}
	}
}
