FROM python:3.11-slim-bullseye
WORKDIR /app

ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080

# Run run.py when the container launches
ENTRYPOINT ["python", "run.py"]