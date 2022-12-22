FROM --platform=amd64 ubuntu:22.04

WORKDIR /app

# Setup user
RUN groupadd -r orchestrator && useradd -r -g orchestrator orchestrator
RUN groupadd docker
RUN usermod -aG docker orchestrator

# Install Python
RUN apt update
RUN apt install software-properties-common python3-pip curl -y

# Install Docker
RUN apt install apt-transport-https ca-certificates -y 
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
RUN apt install docker-ce-cli:amd64 -y

# Setup Orchestrator
ADD tools /app/tools
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY orchestrator.py .

ENTRYPOINT ["python3", "orchestrator.py"]