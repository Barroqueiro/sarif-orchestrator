#!/bin/bash

docker build . -t sarif-orchestrator
docker run -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output:/output:rw \
            -v /var/run/docker.sock:/var/run/docker.sock:rw \
            sarif-orchestrator report \
            --input-dir /output/Reporting \
            --output-dir /output/Markdown \
