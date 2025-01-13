# Golang Base Image
FROM golang:1.23 AS builder

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Module laden
COPY go.mod go.sum ./
RUN go mod download

# Code kopieren und bauen
COPY . .
RUN go build -o stock-publisher

# Minimalistisches Container-Image
FROM ubuntu:22.04
WORKDIR /app
COPY --from=builder /app/stock-publisher .
EXPOSE 8080

# Startbefehl
CMD ["./stock-publisher"]
