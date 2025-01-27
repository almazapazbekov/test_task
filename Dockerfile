FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/gdal/libgdal.so

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
