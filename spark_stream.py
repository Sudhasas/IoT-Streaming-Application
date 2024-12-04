from pyspark.sql import SparkSession

def process_stream(input_topic, bootstrap_servers):
    spark = SparkSession.builder         .appName("WeatherStreamProcessor")         .getOrCreate()

    # Read from Kafka
    df = spark         .readStream         .format("kafka")         .option("kafka.bootstrap.servers", bootstrap_servers)         .option("subscribe", input_topic)         .load()

    # Select weather data
    weather_data = df.selectExpr("CAST(value AS STRING)")

    # Display processed data to console (can be saved to MongoDB later)
    query = weather_data         .writeStream         .outputMode("append")         .format("console")         .start()

    query.awaitTermination()

# Example usage: Process weather stream
if __name__ == "__main__":
    process_stream("weather_topic", "localhost:9092")
