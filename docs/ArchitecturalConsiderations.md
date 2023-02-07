# Architectural Considerations

## Architecture Explanation

## High level representation of architecture

The orchestrator performs the different execution of tools by spawning sibling containers that report back to the output folder shared and consume information from the input folder and the config folder.

![Architecture](../images/Orchestrator_Resource_Sharing.png?raw=True "Architecture")

## Thread execution

The image bellow shows an example where tool 3 depends on both tool 1 and tool 2

![Thread Execution](../images/Thread_Explanation.png?raw=True "Threads example")

## Volumes

The 3 volumes shared are somewhat self explanatory and while 1 single volume for input was considered, the approach to separate this directory into 2 is based on the simplification of the process to allow for the division of purpose between the 2.

The configuration and input volumes are configured as read only and the output directory is the only configured with write access

```
volumes:
    - ${INPUT_HOST_DIR}:/input:ro
    - ${OUTPUT_HOST_DIR}:/output:rw
    - ${CONFIG_HOST_DIR}:/config:ro
```

## Tool files

Tools are configured in a standard way to provide an interface for the adition of further solutions, the objective is to allow for the possibility of every tool that reports in SARIF to be integrated within this framework.

The files are written in [toml](https://toml.io/en/) and have the following specification:

- **tag**: The tag of the image to be used
- **image**: Image for the tool to be executed
- **output_volume_docker**: Some images already come configured with a volume that they will output the results to and this is configured here
- **input_volume_docker**: Some images already come configured with a volume that they will consume information from and this is configured here
- **default_option**: When no option is configured in the run specification, this argument is taken into consideration as the default
- **options**: Options allowed by the tool, while some tools are only made for one purpose some have different commands that can be configured with different arguments, this allows for the specification of multiple commands
  - This argument will almost always take an `output_place` and a `custom_args` argument to be formatted by python to take into consideration the place where to output the sarif results and custom args passed by the user, respectivly. Arguments that can vary like the files to be scanned, a target, an image, are taking into consideration using numbers and relate to the list of arguments passed in the run file.

