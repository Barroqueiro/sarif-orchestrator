# Sarif Tool Orquestrator

## List of Tools

- GitLeaks [Has docker]
- Hadolint
- Dockle [Has docker]
- Grype and Syft
- Trivy [Has Docker]
- ESLint
- Bandit
- Semgrep
- Horusec [Has docker](https://docs.horusec.io/docs/cli/installation/#installation-via-docker-image)
- OWASP Depedency Check

## Todo

- Verfication of inputs
- Possibly add some command line goodies along with tool information (Which are there and their options)
- Logging in a better way and keep command outputs to the respective files

## Notes

- Docker does not ssem to allow for multiple accesses to the same image at the same time, this can cause timeout problem within tools that are going to analyse the same image