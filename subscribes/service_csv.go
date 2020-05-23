package main

import (
	"github.com/gomodule/redigo/redis"
	"fmt"
	"encoding/csv"
    "encoding/json"
    "os"
)

type Application struct {
    Brand string
    Price string
}

func main() {	
	c, err := redis.Dial("tcp", ":6379")
	if err != nil {
		// handle error
	}
	
	psc := redis.PubSubConn{Conn: c}
	psc.Subscribe("topic_create_file")

	for {
		switch v := psc.Receive().(type) {
			case redis.Message:
				var jsonData []Application
				err = json.Unmarshal([]byte(v.Data), &jsonData)
				if err != nil {
					fmt.Println(err)
				}

				csvFile, err := os.Create("./files/file_go.csv")
				if err != nil {
					fmt.Println(err)
				}
				defer csvFile.Close()

				writer := csv.NewWriter(csvFile)

				for _, usance := range jsonData {
					var row []string
					row = append(row, usance.Brand)
					row = append(row, usance.Price)
					writer.Write(row)
				}
				writer.Flush()
				fmt.Println("File go CSV")
		}
	}
	defer c.Close()
}
