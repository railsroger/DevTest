# DevTest
### Задание 1: Docker image
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
