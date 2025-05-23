FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
