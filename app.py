from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
import logging
import os
import json
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set up logging with a structured logger
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Setup MongoDB connection using environment variable
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client.ping_database
collection = db.pings

# Prometheus metric to count total requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/ping', methods=['GET'])
def ping():
    REQUEST_COUNT.inc()  # Increment the Prometheus counter

    # Record the ping with a timestamp in MongoDB
    result = collection.insert_one({'message': 'ping', 'timestamp': datetime.utcnow()})

    # Log the ping event
    logging.info(json.dumps({
        'event': 'PingReceived',
        'id': str(result.inserted_id),
        'timestamp': datetime.utcnow().isoformat()
    }))

    return jsonify({'message': 'Ping recorded', 'id': str(result.inserted_id)})

@app.route('/metrics')
def metrics():
    # Expose Prometheus metrics
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    # Read environment variables
    flask_env = os.getenv('FLASK_ENV', 'production')
    port = int(os.getenv('PORT', 5000))

    # Configure debug mode based on FLASK_ENV
    debug_mode = True if flask_env == 'development' else False

    # Run the Flask application
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
