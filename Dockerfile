FROM python:3.11-slim-bullseye
WORKDIR /app

ADD . /app

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytesseract

EXPOSE 8080

# Run run.py when the container launches
ENTRYPOINT ["python","run.py"]
