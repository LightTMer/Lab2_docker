FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY /app/file.py .
COPY image.png .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "file.py"]