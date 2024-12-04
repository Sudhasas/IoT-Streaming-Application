from pymongo import MongoClient

def save_to_mongo(data, db_name, collection_name, mongo_uri="mongodb://localhost:27017/"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(data)

# Example usage: Store processed data in MongoDB
if __name__ == "__main__":
    data = {"temperature": 22.5, "humidity": 60, "timestamp": "2024-12-02T10:00:00Z"}
    save_to_mongo(data, "weatherDB", "weatherData")
