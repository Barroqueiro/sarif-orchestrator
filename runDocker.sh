#!/bin/bash

docker build . -t sarif-orchestrator
docker run  -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output:/output:rw \
            -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/input:/input:ro \
            -v /Users/cruz/Desktop/Bolsa/sarif-orchestrator/config:/config:ro \
            -v /var/run/docker.sock:/var/run/docker.sock:rw \
            sarif-orchestrator orchestrator \
            --keep-images \
            --input-dir-host /Users/cruz/Desktop/Bolsa/sarif-orchestrator/input \
            --output-dir-host /Users/cruz/Desktop/Bolsa/sarif-orchestrator/output \
            --config-dir-host /Users/cruz/Desktop/Bolsa/sarif-orchestrator/config \
            --config /config/run.toml 