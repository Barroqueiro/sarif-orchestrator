#!/bin/bash

docker build . -t sarif-orchestrator
docker run -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output:/output:rw \
            -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/input:/input:ro \
            -v /var/run/docker.sock:/var/run/docker.sock:rw \
            sarif-orchestrator \
            --keep-images \
            --input-dir-host /Users/cruz/Desktop/Bolsa/sarif-orchestrator/input \
            --output-dir-host /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output \
            --config /input/run.toml 