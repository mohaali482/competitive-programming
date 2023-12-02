package trebuchet

import (
	"strconv"
)

func Solution(line string) string {
	i := 0
	j := len(line) - 1
	output := ""
	var err error
	for ; i < len(line); i++ {
		_, err = strconv.Atoi(string(line[i]))
		if err == nil {
			output += string(line[i])
			break
		}
	}
	for ; j >= 0; j-- {
		_, err = strconv.Atoi(string(line[j]))
		if err == nil {
			output += string(line[j])
			break
		}
	}

	return output
}
