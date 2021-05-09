package main

import (
	"context"
	"errors"
	"fmt"
	"golang.org/x/sync/errgroup"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

func hello(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}


func main() {
	sigs := make(chan os.Signal, 1)

	cancelCtx, cancel := context.WithCancel(context.Background())
	signal.Notify(sigs, syscall.SIGTERM, syscall.SIGQUIT, syscall.SIGINT)

	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)
	server := &http.Server{Addr: ":8080", Handler: nil}

	g, ctx := errgroup.WithContext(cancelCtx)
	g.Go(func() error {
		<-ctx.Done()
		println("context done, stop")
		return server.Shutdown(ctx)
	})

	g.Go(func() error {
		println("start http server")
		return server.ListenAndServe()
	})
	g.Go(func() error {
		for {
			select {
			case <-ctx.Done():
				return ctx.Err()
			case <-sigs:
				println("signal received, cancel context")
				cancel()
				return nil
			}
		}
	})
	if err := g.Wait(); err != nil && !errors.Is(err, context.Canceled)  && !errors.Is(err, http.ErrServerClosed) {
		panic(err)
	}
}
