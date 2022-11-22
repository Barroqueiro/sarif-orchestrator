# Sarif Tool Orchestrator

The sarif tool orchestrator is a docker orchestrator that following a toml file with certain tools to run, will spawn docker containers for those tools and manage the directory structure to get the output to a file within the host.

## Config file

This is the specification for the file to configure a run (Work In Progress)

The file uses [toml](https://toml.io/en/) and its composed of a list of runs where each on corresponds to ONLY ONE tool and can have the following arguments:

- **tool**: The name must match the names within the tools folder
- **option**: The options must be defined withint the tools configuration file
- **args**: The arguments to be passed that are considered essential for a run of a option of a tool
- **custom_args**: Custom arguments that can be used to configure tools in the command line (Possibly interesting to defined levels of sensitivy and things alike, using tyhe input folder and a custom arguments it cna be possible to use configuration files within the tools)
- **depends_on**: Creates a dependency graph between tools, each tool within this list must have finished for the tool being considered to be allowed to run

### Example

```
[[runs]]

tool = "horusec"
option = "scan"
args = ["<repo-name_placeholder>"]

[[runs]]

depends_on= ["horusec"]
tool = "gitleaks"
option = "detect"
args = ["<repo-name_placeholder>"]

[[runs]]

depends_on= ["gitleaks"]
tool = "dockle"
option = "scan"
args = ["<image-name-placeholder>"]
custom_args = "--timeout 600s"

[[runs]]

depends_on= ["gitleaks"]
tool = "trivy"
option = "image"
args = ["<image-name-placeholder>"]
```

## How to run

The python script takes as arguments:

- input-dir - Directory to be shared with docker to get access to files for analysis
- output-dir - Directory within docker where output results must be places
- output-dir-host - Directory to be shared with docker to allow for writting within the user system to get reports, this folder can be expected to gain 2 folders (Reporting and Logging)
- keep-images - When cleaning up, the script will remove the images for the containers ran, with-out this flag the images will be erased

Note: `output-dir` and `output-host-dir` are the same when running locally (`./runLocal.sh`) because the reporting and logging directories will be created within the host, however when running with docker (`./runDocker.sh`) the output folder where the directories will be created is within docker and we shall pass the host output directory to allow for the new dockers to communicate with it.

## List of (Possible) Tools

- [x] GitLeaks [Has docker]
- [ ] Hadolint
- [x] Dockle [Has docker]
- [ ] Grype and Syft
- [x] Trivy [Has Docker]
- [ ] ESLint
- [ ] Bandit
- [ ] Semgrep
- [x] Horusec [Has docker](https://docs.horusec.io/docs/cli/installation/#installation-via-docker-image)
- [ ] OWASP Depedency Check

## Todo

- Verfication of inputs
- Possibly add some command line goodies along with tool information (Which are there and their options)
- Logging in a better way and keep command outputs to the respective files

## Notes

- Docker does not seem to allow for multiple accesses to the same image at the same time, this can cause timeout problem within tools that are going to analyse the same image