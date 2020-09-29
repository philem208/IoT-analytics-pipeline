FROM golang:1.15.2-alpine3.12
RUN apk update && apk add git && go get github.com/Shopify/sarama && mkdir /app
ADD . /app
WORKDIR /app
RUN go build -o main .
CMD ["/app/main"]
