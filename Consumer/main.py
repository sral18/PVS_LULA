import pika
import pymongo
import os
import json
import statistics

# Hilfsfunktion zur Fehlerbehandlung
def fail_on_error(error, message):
    if error:
        raise Exception(f"{message}: {error}")

# Lade die Verbindungsdetails aus Umgebungsvariablen oder nutze Standardwerte
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://lulateko:lulateko@rabbitmq:5672/")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "default")
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://mongo:27017/")
MONGODB_DB = os.getenv("MONGODB_DB", "stockmarket")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "stocks")

# Stelle eine Verbindung zu RabbitMQ her
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

# Verbinde dich mit MongoDB
mongo_client = pymongo.MongoClient(MONGODB_URI)
db = mongo_client[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

# Verarbeite die Nachrichten, die aus RabbitMQ kommen
def process_messages(ch, method, properties, body):
    messages = json.loads(body)
    prices = [msg["price"] for msg in messages]
    avg_price = statistics.mean(prices)

    # Speichere das Ergebnis in der MongoDB
    result = {
        "company": messages[0]["company"],
        "avgPrice": avg_price
    }
    collection.insert_one(result)
    print(f" [x] Processed {len(messages)} messages. Avg Price: {avg_price}")

    # Bestätige, dass die Nachricht verarbeitet wurde
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Richte den Consumer ein, um Nachrichten aus der Warteschlange zu lesen
channel.queue_declare(queue=RABBITMQ_QUEUE)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=process_messages)

print(f" [*] Waiting for messages in {RABBITMQ_QUEUE}. To exit press CTRL+C")
channel.start_consuming()
