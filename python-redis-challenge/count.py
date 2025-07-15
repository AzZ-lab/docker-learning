import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def welcome():
    return 'Welcome to the challenge!'

@app.route('/count')
def count():
    # Increment the count in Redis
    count = r.incr('vists')
    return f'this page has been visted {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
