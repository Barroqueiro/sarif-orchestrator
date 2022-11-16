#!/bin/bash

docker run -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output:/output:rw -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/input:/input:ro -v /var/run/docker.sock:/var/run/docker.sock:rw sarif-orchestrator