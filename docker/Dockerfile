FROM alpine:3.14

RUN addgroup -S appgroup && adduser -S orchestrator -G orchestrator
USER orchestrator

WORKDIR /app

# Install Python
RUN apk add --no-cache python3 py3-pip

# Install Docker
RUN apk add --update docker openrc

# Setup Orchestrator
ADD tools /app/tools
ADD templates /app/templates
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY orchestrator.py .

ENTRYPOINT ["python3", "orchestrator.py"]
CMD ["--help"]