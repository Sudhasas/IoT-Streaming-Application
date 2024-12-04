# IoT-Streaming-Application
A Python-based project to publish and consume weather data using Kafka for real-time data streaming and processing.

Process Flow
1. Weather API:
The Weather API provides weather data in JSON format. It acts as the data source for the application.

2. MQTT Broker:
The JSON data from the Weather API is sent to an MQTT broker.
MQTT is a lightweight messaging protocol used for efficient communication in IoT systems.
The MQTT broker publishes the data to subscribers.

3. Kafka:
Kafka, a distributed messaging system, is used to ingest the data published by the MQTT broker.
Zookeeper is utilized to manage Kafka's configurations and distributed nature.
Kafka ensures reliable and scalable streaming of data.

4. Apache Spark Structured Streaming:
Apache Spark processes the streaming data from Kafka in real time.
It performs the required computations such as averages, minimum/maximum calculations, and formatting of the data for analysis.

5. MongoDB:
Processed data is stored in MongoDB, a NoSQL database, for long-term storage and querying.

6. Live Dashboard:
A live dashboard visualizes the processed data.
Data is sent to the dashboard via WebSocket, enabling real-time updates to the graphs and metrics.

Goals of the Project:

The project processes weather data to compute and display the following metrics:
1. Live Graph: Display real-time weather data on a graph.
2. Hourly Average: Calculate and show the average weather readings for each hour.
3. Maximum and Minimum in a Day: Identify the hours with the highest and lowest readings in a day.
4. Daily Average: Compute the average weather readings for each day.
5. Maximum and Minimum in a Week: Find the days with the highest and lowest averages in a week.

Technologies Involved:

Weather API: Data provider.
MQTT: Messaging protocol for data transfer.
Kafka: Distributed data ingestion platform.
Apache Spark: Real-time data processing and analytics.
MongoDB: Database for storing processed data.
WebSocket: For real-time communication with the dashboard.
Live Dashboard: Frontend for visualizing data.
