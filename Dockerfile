FROM tensorflow/tensorflow:1.14.0-gpu-py3

WORKDIR /app
COPY . /app

RUN apt-get update
RUN pip3 install -r requirements_gpu.txt
