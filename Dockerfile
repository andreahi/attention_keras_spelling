FROM tensorflow/tensorflow:latest-gpu

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements-gpu.txt
