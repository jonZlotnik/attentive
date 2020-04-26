package main

// #cgo CFLAGS: -I${SRCDIR}/include
// #cgo LDFLAGS: -L${SRCDIR}/libs -liotc
// #include <iotc.h>
// #include <iotc_error.h>
// #include <iotc_jwt.h>
import "C"
import (
	"fmt"
	"github.com/davecgh/go-spew/spew"
)

const (
	DEFAULT_PRIVATE_KEY_FIILENAME = "ec_private.pem"
)

func main() {
	iotcConnectPrivateKeyData := C.iotc_crypto_key_data_t{}
	ecPrivateKeyPem := ""
	var iotcContext C.iotc_context_handle_t = C.IOTC_INVALID_CONTEXT_HANDLE

	fmt.Println("Printing the application variables")
	spew.Dump(iotcConnectPrivateKeyData)
	fmt.Println(ecPrivateKeyPem)
	spew.Dump(iotcContext)
}
