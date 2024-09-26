FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Instalación de dependencias necesarias: Chrome, Selenium, y demás
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    unzip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm google-chrome-stable_current_amd64.deb

# Instalar dependencias de Python
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

# Comando para iniciar Gunicorn con la aplicación Flask
CMD ["gunicorn", "-c", "gunicorn_config.py", "main:app"]
