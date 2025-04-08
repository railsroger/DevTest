------------------------------------------------------------------------------------------------------------------------------------------
Задание 2: Docker compose
Создайте docker-compose.yaml, который поднимет 2 контейнера:
• Собирает Flask приложение из первой части.
• Redis из образа redis:alpine как кеш.
Необходимо обновить app.py, чтобы он использовал Redis.
При запросе к /count увеличивал счетчик посещений и возвращал его.
Запустите docker-compose и убедитесь, что сервисы работают корректно.
------------------------------------------------------------------------------------------------------------------------------------------
### Устанавливаем Docker-Compose:
```
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
docker compose version
```

### Исправляем файл app.py и добавляем Redis:
```
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
```

### Создаем файл requirements.txt и добавляем зависимости, добавляя Redis:
```
Flask==2.0.3
Werkzeug==2.0.3
redis==4.1.0
```

### Оставляем Dockerfile с содержимым, таким же как в первом задании:
```
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Запуск:
```
docker build -t flask-ping-app .
docker run -p 5000:5000 flask-ping-app
```

### Результат:
![Result](https://github.com/railsroger/DevTest/blob/main/images/start.png)
![Result](https://github.com/railsroger/DevTest/blob/main/images/result.png)
