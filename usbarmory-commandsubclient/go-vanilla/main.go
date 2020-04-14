package main

import "fmt"

// #cgo CFLAGS: -Ic_include
// #cgo LDFLAGS: c_bin/libiotc.a
// #include <iotc.h>
import "C"

func main() {
	fmt.Println("Hello World!")
	fmt.Printf("Invoking c library...\n")
	C.iotc_initialize()
}