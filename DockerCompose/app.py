from flask import Flask, jsonify
import redis
import os

app = Flask(name)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    try:
        visits = redis_client.incr('counter')
        return jsonify({"count": visits})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if name == 'main':
    app.run(host='0.0.0.0', port=5000)

