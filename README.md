# Sarif Tool Orchestrator

The sarif tool orchestrator is a docker orchestrator that following a toml file with certain tools to run, will spawn docker containers for those tools and manage the directory structure to get the output to a file within the host.

## Documentation

Documentation can be found inside the [Docs Folder]([../Docs](https://github.com/Barroqueiro/sarif-orchestrator/tree/main/docs))


## List of (Possible) Tools and Notes

- [x] GitLeaks [Docker](https://github.com/zricethezav/gitleaks#installing)
- [x] Hadolint [Docker](https://github.com/hadolint/hadolint#install)
  - Does not have a way to output to a file, don't know how to circumvent this problems without major refactor, [they are working on a feature to do just that](https://github.com/hadolint/hadolint/issues/863) - Solved by using a bash call to the script and redirecting the output inside the container, if the feature for files comes this should be refactored as the current solution is not that pretty
- [x] Dockle [Docker](https://github.com/goodwithtech/dockle#use-docker)
- [x] Grype and Syft [Both have Docker](https://github.com/anchore/grype#getting-started)
- [x] Trivy [Docker](https://github.com/aquasecurity/trivy#get-trivy)
- [x] ESLint [Docker](https://hub.docker.com/r/cytopia/eslint)
  - Problems with SARIF reporting, [submitted a issue](https://github.com/cytopia/docker-eslint/issues), submitted pull request, waiting on response
- [x] Flake8 [Docker](https://hub.docker.com/r/alpine/flake8)
  - SARIF is supported by a custom formatter [installed by pip](https://pypi.org/project/flake8-sarif/), already got a pull request accepted, still missing on offical docker hub
- [x] Bandit [Docker](https://github.com/cytopia/docker-bandit)
  - SARIF is supported by a custom formatter [installed by pip](https://pypi.org/project/flake8-sarif/), already got a pull request accepted, still missing on offical docker hub
- [x] Semgrep [Docker](https://github.com/returntocorp/semgrep#getting-started)
  - Platform only available fr linux/amd64, added option to make it possible to configure a tool platform by hand on the run configuration
- [x] Horusec [Docker](https://docs.horusec.io/docs/cli/installation/#installation-via-docker-image)
- [x] OWASP Depedency Check [Docker](https://github.com/jeremylong/DependencyCheck#docker)
  - Platform only available for linux/amd64 
- [x] Zap [Docker](https://www.zaproxy.org/docs/docker/about/)


