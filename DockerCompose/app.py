from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/count')
def count():
    try:
        visits = cache.incr('visits')
        return f'This page has been visited {visits} times.'
    except redis.exceptions.ConnectionError as e:
        return f'Redis error: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)