# Usage

## Docker compose

The `docker-compose.yml` file found inside the docker folder provides a simple way to run the project, this file presents 2 services available:

- orchestrator
  - Which allows the user to leverage the different available tools and produce reports based on the input parameters
- report
  - Which allows the user to transform the SARIF logs into more readable options (At the moment only Markdown is available)

The command to run each of the services is then:

```
docker-compose up orchestrator
```

or

```
docker-compose up report
```

The services can however be used simultaneously or chained together by using docker-compose's depends-on condition syntax

```
depends_on:
        orchestrator:
            condition: service_completed_successfully
```

The configuration for this file is provided by the `.env` file inside the same folder, this file has 6 possible variables to be configured, divided by service these are the objectives of each:

### Orchestrator service

This service takes a configuration file along with shared directories between the host and containers and executes the configured tools to produce SARIF results.

- `INPUT_HOST_DIR` - A folder to be shared with the containers for the purposes of sharing input information, this folder should take files that will be analyzed by the project
- `OUTPUT_HOST_DIR` - A folder to be shared with the containers for the purposes of retreiving information from the containers, this folder will have 2 folders automatically created (`Reporting` and `Logs`) where the first will receive the SARIF files produced by analysis and the later will Logs for all tools executed as well as a Log File for the orchetsrator to make troubleshooting easier
- `CONFIG_HOST_DIR` - A folder to be shared with the containers for the purposed of sharing configuration information, this folder should take files meant to configure the orchestrator or the tools ran by it
- `CONFIG_FILE` - The file that configures the current analysis, the specification is addressed later

### Report service

This service takes a input folder, collects the SARIF files found inside and outputs a markdown file for each of the identified files to an output directory

- `INPUT_DIR` - Input folder containing the sarif files
- `OUTPUT_DIR` - Output folder to take the Markdown files produced

## Configuration file

This is the specification for the file to configure a run

The file uses [toml](https://toml.io/en/) and its composed of a list of runs where each one corresponds to **ONLY ONE** tool and can have the following arguments:

- **tool**: Name of the tool to be executed, the name must match the names within the tools folder
- **option**: Name of the option to be executed by the selected tool, the options must be defined within the tool's configuration file
- **args**: The arguments to be passed that are considered essential for a run of a option of a tool
- **custom_args**: Custom arguments that can be used to configure tools in the command line (Possibly interesting to defined levels of sensitivy and things alike, using the config folder and custom arguments it can be possible to use configuration files within the tools)
- **depends_on**: Creates a dependency graph between tools, each tool within this list must have finished for the tool being considered to be allowed to run
- **platform**: Specifies the platform for the docker create command

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



