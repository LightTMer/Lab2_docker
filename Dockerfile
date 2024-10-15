FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    ffmpeg libsm6 libxext6 \
  

    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY file.py .
COPY image.png .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "file.py"]

# Устанавливаем ENTRYPOINT для запуска VNC-сервера и Python приложения
# ENTRYPOINT ["sh", "-c", "xvfb-run -n 0 -s '-screen 800x600x24' x11vnc -display :0 -forever -nopw & python file.py"]
# ENTRYPOINT ["xvfb-run", "-n", "0", "-s", "'-screen 800x600x24'", "python", "file.py"]
# ENTRYPOINT ["xvfb-run", "-n", "0", "-s", "-screen 800x600x24", "python", "file.py"]
# ENTRYPOINT ["sh", "-c", "xvfb-run -n 0 -s '-screen 800x600x24' python file.py"]

# ENTRYPOINT ["sh", "-c", "xvfb-run -n 0 -s -screen 800x600x24 python file.py"]

# ENTRYPOINT ["sh", "-c", "xvfb-run -n 0 -s '-screen 800x600x24' python file.py"]