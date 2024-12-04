from kafka import KafkaProducer
import json

def produce_to_kafka(data, topic, bootstrap_servers):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    producer.send(topic, data)
    producer.close()

# Example usage: Consume from MQTT and send to Kafka
if __name__ == "__main__":
    from mqtt_broker.mqtt_publish import publish_to_mqtt

    # Fetch and publish weather data
    data = {"temperature": 22.5, "humidity": 60}  # Example MQTT input
    publish_to_mqtt(data, "localhost", "weather/data")

    # Send to Kafka
    produce_to_kafka(data, "weather_topic", ["localhost:9092"])
