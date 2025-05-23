# DEVTEST
------------------------------------------------------------------------------------------------------------------------------------------
Задание 1: Docker image
Создайте Dockerfile, который:
• Используется python3.9 как базовый образ.
• Копирует локальный файл app.py в контейнер.
• Устанавливает зависимости из requirements.txt.
• Запускает Flask-приложение при старте контейнера.
Необходимо создать app.py - простое Flask api с 1 эндпоинтом /ping, который возвращает {"status": "ok"}.
Контейнер должен запуститься на порту 5000. Проверка работы контейнера производится путем отправки curl запроса http://localhost:5000/ping
------------------------------------------------------------------------------------------------------------------------------------------
### Устанавливаем Docker:
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Создаем файл app.py с содержимым:
```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Создаем файл requirements.txt и добавляем зависимости (поправка, что может ругаться на невозможность импорта модуля, тогда добавляем еще Werkzeug). Ошибка может быть вида:
```
Traceback (most recent call last):
  File "/app/app.py", line 1, in <module>
    from flask import Flask, jsonify
  File "/usr/local/lib/python3.9/site-packages/flask/__init__.py", line 7, in <module>
    from .app import Flask as Flask
  File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 28, in <module>
    from . import cli
  File "/usr/local/lib/python3.9/site-packages/flask/cli.py", line 18, in <module>
    from .helpers import get_debug_flag
  File "/usr/local/lib/python3.9/site-packages/flask/helpers.py", line 16, in <module>
    from werkzeug.urls import url_quote
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/usr/local/lib/python3.9/site-packages/werkzeug/urls.py)
```
Исправляем добавлением Werkzeug:
```
Flask==2.0.3
Werkzeug==2.0.3
```

### Создаем Dockerfile с содержимым:
```
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask

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
