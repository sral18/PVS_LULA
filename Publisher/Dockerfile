# Golang Base Image
FROM golang:1.20 AS builder

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Module laden
COPY go.mod go.sum ./
RUN go mod download

# Code kopieren und bauen
COPY . .
RUN go build -o stock-publisher

# Minimalistisches Container-Image
FROM debian:bullseye-slim
WORKDIR /app
COPY --from=builder /app/stock-publisher .
EXPOSE 8080

# Startbefehl
CMD ["./stock-publisher"]
