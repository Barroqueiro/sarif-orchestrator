# Usage

## Docker compose

The `docker-compose.yml` file found inside the docker folder provides a simple way to run the project, this file presents 3 services available:

- orchestrator
  - Which allows the user to leverage the different available tools and produce reports based on the input parameters
- report
  - Which allows the user to transform the SARIF logs into more readable options (At the moment only Markdown is available)
- upload
  - Which allows for the upload of the scan information into a DefectDojo instance

The command to run each of the services is then: `docker-compose up orchestrator`, `docker-compose up report` or `docker-compose up upload`

The services can however be used simultaneously or chained together by using docker-compose's depends-on condition syntax

```
depends_on:
        orchestrator:
            condition: service_completed_successfully
```

The configuration for this file is provided by the `.env` file inside the same folder, this file has 9 possible variables to be configured, divided by service these are the objectives of each:

### Global setting

- `CONFIG_HOST_DIR` - A folder to be shared with the containers for sharing configuration information through files.

### Orchestrator service

This service takes a configuration file along with shared directories between the host and containers and executes the configured tools to produce SARIF results.

- `ORCHESTRATOR_INPUT_HOST_DIR` - A folder to be shared with the containers for the purposes of sharing input information, this folder should take files that will be analyzed by the project
- `ORCHESTRATOR_OUTPUT_HOST_DIR` - A folder to be shared with the containers for the purposes of retreiving information from the containers, this folder will have 2 folders automatically created (`Reporting` and `Logs`) where the first will receive the SARIF files produced by analysis and the later will receive Logs for all tools executed as well as a Log File for the orchetsrator to make troubleshooting easier
- `ORCHESTRATOR_CONFIG_FILE` - The file that configures the current analysis, the specification is addressed later

### Report service

This service takes a input folder, collects the SARIF files found inside and outputs a markdown file for each of the identified files to an output directory

- `REPORT_INPUT_HOST_DIR` - Input folder containing the sarif files
- `REPORT_OUTPUT_HOST_DIR` - Output folder to take the Markdown files produced
- `REPORT TYPE` - The type of report to be produced. There exists 3 different formats (MarkDown, HTML and PDF). Multiple formats can be selected by making use of a comma.

### Upload Service

- `UPLOAD_CONFIG_FILE` - Configuration file for the upload containing information on the DefectDojo instance we are targetting.
- `UPLOAD_INPUT_HOST_DIR` - Input folder to take the information for upload

## Configuration file

This is the specification for the file to configure a run

The file uses [toml](https://toml.io/en/) and its composed of a list of runs where each one corresponds to **ONLY ONE** tool and can have the following arguments:

- **tool**: Name of the tool to be executed, the name must match the names within the tools folder
- **option**: Name of the option to be executed by the selected tool, the options must be defined within the tool's configuration file
- **args**: The arguments to be passed that are considered essential for a run of a option of a tool
- **custom_args**: Custom arguments that can be used to configure tools in the command line (Possibly interesting to define levels of sensitivity and things alike, using the config folder and custom arguments it can be possible to use configuration files within the tools)
  - The usage of configuration files per tools is made by passing the custom argument to the tool indicating the path of the configuration file (Remember to relate this path to the shared docker directory) and by placing a configuration file adapted towards the user's needs inside the config folder
- **depends_on**: Creates a dependency graph between tools, each tool within this list must have finished for the tool being considered to be allowed to run
- **platform**: Specifies the platform for the docker create command

### Example

```
[[runs]]

tool = "dockle"
option = "scan"
args = ["<image-name-placeholder>"]
custom_args = "--timeout 600s"
depends_on= ["gitleaks"]
platform = "linux/amd64"
```

## Ignoring vulnerabilities

Vulnerabilities reported can be false positives or simply accepted as a risk, this can be achieved in different ways, one of which works outside this orchestrator as most tools provide a way to do this either by a configuration file or by command line, a unifying solution was created to keep the track of ignored vulnerabilities in a more sustainable way.

In our solutions both the `.hashignore` and `.idignore` files can be placed under the global configuration directory. These are explained bellow.

### Hash

When finishing up the reporting process the orchestrator will iterate over all vulnerabilities found and produce a hash which will be appended to the SARIF file inside each of the vulnerabilities present. This hash can later be used inside a file called `.hashignore` to make sure that this result does not show up inside the SARIF reports.

## Id

All results take into consideration `ruleId` and as such these Ids can be used to ignore vulnerabilities as well, every Id included inside the `.idignore` file will be discarded from the results.

Note: Both files follow the `.gitignore` comment syntax for simplification, this means that they can be commented using the `#` symbol and all lines with that symbol as the first characters will be ignored, **this does not allow for inline commenting**.

## Tools available

### Bandit

Bandit looks for common security issues in python code.

Arguments:

- Path of the code to be analysed

### Dependency Check

Detects publicly disclosed vulnerabilities in the dependencies of a project.

Arguments:

- Path to scan

Note: Dependency Check is only built on docker using the linux/amd64 architecture, this means that when running this image on an host with a different OS, the image can have unexpected bahviour even when casting the platform to linux/amd64.

### Dockle

Scans Docker images for bad practices.

Arguments:

- Image to be scanned

### EsLint

Scans JavaScript files for problems.

Arguments:

- File(s) to be scanned (Glob patterns can be passed as arguments (p.e 'lib/**'))

Note: EsLint will not work without a configuration file by default, one is present within the `config` folder and can be altered for necessities

### Flake8

Checks style conventions and code complexity in python files.

Arguments:

- Path to be scanned

### GitLeaks

Detects hardcoded secrets in git repositories.

Arguments:

- Path to be scanned

### Grype

Vulnerability scanner for containers and filesystems.

Arguments:

- Image to be scanned

### Hadolint

Scans docker images for bad practices and performs shell linting.

Arguments:

- Dockerfile to be analysed

### Horusec

Collection of tools for SAST and SCA analysis for different languages.

Arguments:

- Path to be scanned

### Semgrep

Code scanning for different linguages.

Arguments:

- Path to be scanned

Note: Semgrep is only built on docker using the linux/amd64 architecture, no such problems as Dependency Check were found when forcing the platform but unexpected bahviour can happen.

### Trivy

Multi-purpose scanner (Images, filesystems, git repositories).

Arguments:

- Image to be scanned (or path to be scanned depending on the option selected)

### Zap

Dynamic scanner for web applications.

Arguments:

- Target to be scanned

Note: Zap offers a great deal of costumization and complexity when testing, this tool only functions with a configuration file already present within the `config` folder. The one present is configured for a normal active scan but can be adapted for the user needs without altering the reporting section as the SARIF reporting depends on that section

## Example

The following configuration file provides the steps for a 3 tool scan (`Dockle`, `Hadolint` and `Trivy`), here `Hadolint` is configured with the scan option and takes as arguments the Dockerfile to be analysed (This Dockerfile is present within the root of the input folder), `Dockle` is configured much of the same way but this time taking as argument the image it is going to scan and a custom argument to ensure the tool times out after 600 seconds, finally `Trivy` is configured to run a scan on the same image and this execution depends on `Dockle`, meaning once `Dockle` is finished `Trivy` is launched.

```
[[runs]]

tool = "hadolint"
option = "scan"
args = ["Dockerfile"]

[[runs]]

tool = "dockle"
option = "scan"
args = ["test-image:Test"]
custom_args = "--timeout 600s"

[[runs]]

tool = "trivy"
option = "image"
args = ["test-image:Test"]
depends_on= ["dockle"]
```

## TL;DR

This orchestrator needs 3 directories to be shared with, a config, a input and output directories, the configuration is based upon a toml file present within the `config` folder and execution is made using docker-compose. Ignoring vulnerabilities is possible by hash and by Id.

### Quick start

```
# Clone repository
git clone git@github.com:Barroqueiro/sarif-orchestrator.git
cd sarif-orchestrator

# Make directories for input and output
mkdir input
mkdir output

# Get inside docker directory
cd docker

# Make and edit .env file
cp .env.example .env
nano .env

# Build sarif-orchestrator image (Optional)
docker-compose build

# Scan (Edit the run file to be used in the scan)
docker-compose up orchestrator

# Make a reporting directory
mkdir ../output/Markdown

# Report 
docker-compose up report
```