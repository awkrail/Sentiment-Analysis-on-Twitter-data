FROM python:3.6.2-slim
WORKDIR /app
RUN mkdir /app/dataset
COPY requirement.txt /app/
COPY train.py /app/
COPY dataset /app/dataset/
RUN pip install -r requirement.txt
