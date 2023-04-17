FROM alpine:3.14

WORKDIR /app

# Install Python
RUN apk add --no-cache python3 py3-pip

# Install Docker
RUN apk add --update docker openrc
# Pillow
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN apk add --update --no-cache g++ gcc libxml2 libxslt-dev py3-lxml
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# Setup Orchestrator
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD tools /app/tools
ADD src /app/src
ADD templates /app/templates
COPY main.py .

ENTRYPOINT ["python3", "main.py"]
CMD ["--help"]