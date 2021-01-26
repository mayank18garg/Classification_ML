# from alpine:latest
FROM python:3.8-slim
# RUN apk add --no-cache python3-dev

# RUN apk add --no-cache py3-pip

# RUN pip3 install --upgrade pip

WORKDIR /app

COPY ./app /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

# ENTRYPOINT ["python3"]
# CMD ["application.py"]
CMD gunicorn --bind 0.0.0.0:$PORT wsgi



