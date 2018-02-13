package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/*

1) Init Arr: 0 0 0 0 0

2) Query1(1,2,100) results in the array: 100 100 0 0 0
   Graph1:
		300
		200
		100  X  X
		000        X  X  X
		     |  |  |  |  |
		     1  2  3  4  5

3) Query2(2,5,100) results in the array: 100 200 100 100 100
   Graph2:
		300
		200     X
		100  X     X  X  X
		000
		     |  |  |  |  |
		     1  2  3  4  5


3) Query3(3,4,100) results in the array: 100 200 200 200 100 (<-This is our resulted array and maximum value is 200, which is the maximum height)
   Graph3:
		300
		200     X  X  X
		100  X           X
		000
		     |  |  |  |  |
		     1  2  3  4  5
    OurResult=MaxHeight: 200

OUR RESULT = MAX VALUE IN UPDATED LIST(0  100  200  200  200  100    0) = 200

------------------------------------------
	     ARR
------------------------------------------
INDEX----0----1----2----3----4----5----6-
------------------------------------------
-------  0    0    0    0    0    0    0
Q1(1,2)  0  100  100    0    0    0    0
Q2(2,5)  0    0  100  100  100  100    0
Q3(3,4)  0    0    0  100  100    0    0
-----------------------------------------
SUM      0  100  200  200  200  100    0
FINAL ARR = 0  100  200  200  200  100    0
OUR RESULT = MAX(FINAL ARR) = MAX(0  100  200  200  200  100    0) = 200

Now lets try to reduce the time complexity of the above problem by using diff array and prefix sum.
Basically we need to understand is how we can create a Graph3 using Data structures. If you read about diff array a slope can be respresented by a
diff array as it only stores the starting and ending of the slope. This is useful in this problem as we do not need to iterate all the elements and find the max.
Diff array basically stores the diff that is happening and the index and Prefix Sum is used to generate back the original array from the Diff Array
-------------------------------------
DIFF ARR
--------------------------------------
INDEX----1----2----3----4----5----6---
--------------------------------------
-------  0    0    0    0    0    0
Q1(1,2)  100  0   -100  0    0    0
Q2(2,5)  0    100  0    0    0  -100
Q3(3,4)  0    0  100    0   -100  0
--------------------------------------
SUM     100  100   0    0   -100 -100

ARR2 = SUM(Columns in DIFF ARR) // its the sum of columns of the diff array
     = 100 100 0 0 -100 -100
PRESUM of ARR2 = 100, 200, 200, 200, 100, 0
IF you see the ARR2 is same as our Final array result above
Finding the MAX of ARR2 is our answer :)
OUR RESULT = MAX(ARR2) = 200
*/
func crush() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	lineValues := strings.Split(strings.TrimSuffix(line, "\n"), " ")
	n, _ := strconv.Atoi(lineValues[0])
	m, _ := strconv.Atoi(lineValues[1])

	// Init the array with 0s
	arr := make([]int, n+1)

	for i := 0; i < m; i++ {
		line, _ = reader.ReadString('\n')
		lineValues = strings.Split(strings.TrimSuffix(line, "\n"), " ")
		a, _ := strconv.Atoi(lineValues[0])
		b, _ := strconv.Atoi(lineValues[1])
		k, _ := strconv.Atoi(lineValues[2])

		// Fill the Diff Array and keep summming columns
		arr[a-1] = arr[a-1] + k
		if b <= n+1 {
			arr[b] = arr[b] - k
		}
	}

	preSumMax := 0
	result := 0
	for j := 0; j < n+1; j++ {
		result = result + arr[j]
		if result > preSumMax {
			preSumMax = result
		}
	}
	fmt.Println(preSumMax)
}
