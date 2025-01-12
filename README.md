# PVS-LULA-01: Parallele und Verteilte Systeme

## Projektbeschreibung
Dieses Projekt implementiert ein verteiltes Finanzsystem, das fiktive Finanzdaten verarbeitet und speichert. Es umfasst mehrere miteinander verbundene Komponenten, die in Docker-Containern bereitgestellt werden. Ziel ist es, ein ausfallsicheres System zu erstellen, das Finanzdaten verarbeitet, aggregiert und über ein Frontend visualisiert.


## Setup und Installation
1. Klonen Sie dieses Repository:
   ```bash
   git clone <repository-url>
   ```
2. Starten Sie die Docker-Compose-Umgebung:
   ```bash
   docker-compose up
   ```
3. Überprüfen Sie die RabbitMQ-Admin-Oberfläche unter [http://localhost:15672/](http://localhost:15672/).
4. Zugriff auf das Frontend unter [http://localhost:3000/](http://localhost:3000/).


## Komponenten

### 1. **Producer (Stock-Publisher)**
- **Funktion:** Generiert zufällige "Buy"- und "Sell"-Datenpakete für fiktive Finanztransaktionen.
- **Aufgaben:**
  - In ein Docker-Container-Image verpacken.
  - Image auf Docker Hub veröffentlichen.
  - Code-Repository: [Stock-Publisher](https://github.com/SwitzerChees/stock-publisher).

### 2. **RabbitMQ (Message Broker)**
- **Funktion:** Zwischenspeicherung der vom Producer generierten Daten in Queues.
- **Aufgaben:**
  - Integration in eine Docker-Compose-Umgebung.
  - Verbindung mit Producer und Consumer zur Datenweiterleitung.

### 3. **Consumer**
- **Funktion:** Liest Datenpakete aus RabbitMQ-Queues, aggregiert sie und speichert Ergebnisse in MongoDB.
- **Aufgaben:**
  - Nachrichten (jeweils 1000 Pakete) aus RabbitMQ-Queues lesen.
  - Durchschnitt berechnen und Ergebnisse speichern.
  - Steuerung der Verbindungen über Umgebungsvariablen.
  - In ein Docker-Container-Image verpacken und auf Docker Hub veröffentlichen.

### 4. **MongoDB Cluster**
- **Funktion:** Speicherung der aggregierten Ergebnisse in einem ausfallsicheren Cluster.
- **Aufgaben:**
  - Aufbau als Replica-Set in Docker-Compose.
  - Sicherstellung der Kommunikation mit Consumer und Frontend.
  - Persistente Speicherung der Daten.

### 5. **Frontend (Stock-Liveview)**
- **Funktion:** Visualisierung der in MongoDB gespeicherten Ergebnisse.
- **Aufgaben:**
  - In ein Docker-Container-Image verpacken.
  - Sicherstellung der Ausfallsicherheit durch mindestens zwei Instanzen mit Load Balancer.
  - Image auf Docker Hub veröffentlichen.
  - Code-Repository: [Stock-Liveview](https://github.com/SwitzerChees/stock-liveview).

### 6. **NGINX (Load Balancer)**
- **Funktion:** Lastverteilung und Failover für das Frontend.
- **Aufgaben:**
  - Verteilung der Anfragen auf mindestens zwei Frontend-Instanzen.
  - Automatisches Failover bei Ausfall einer Instanz.