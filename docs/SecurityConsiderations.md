# Security Considerations

## Docker Socket

Instead of using network interfaces to transport data, Unix sockets act as a network within the kernel to directly send information between processes, allowing programs to connect directly to one another. The sockets are formed as a disk file, but no data is actually written to the file because doing so would be counterproductive. Instead, data is kept in kernel memory, and the file ensures that an object can be referred to and that an access control configuration is available.

The Docker socket conforms to the Unix socket protocol, and in this case, the `docker.sock` file gives the Docker client a method to communicate with the Docker daemon (Server) and issue commands (create, remove, delete...)

## Sharing the docker sock with a container

Docker supports [volumes](https://docs.docker.com/storage/volumes/), which enable transparent sharing of a specific directory from the host to the container. The container mounts the host's referenced directory, displaying the contents of the folder or file, and any information created inside the container is delivered back to the host.

The docker socket being a file (`/var/run/docker.sock`) is then able to be mounted within the container, this means that the container can communicate with the docker daemon process running on the host. This allows for the orchestration of containers on a certain host from inside a container. The Docker process, as a process that needs access to namespaces and cgroups requires root permissions (UID = 0).

## Integrity problems

Processes have a parenthood type of relationship between them, the processes for the PIDs 0 and 1 are created by the kernel and as such the process 1 is the ancestor of all other processes. A running process can fork itself and create a new process, this will be a child process, if the program forks again a new child will be created, and each child is then a sibling of each other as they have the same parent. This hierarchy allows for the access control of child processes, as a parent by forking itself, will make his child have the same or less permissions as him, not more.

However taking containers as the child processes of the docker daemon, when the docker socket is mounted and a container creates another, the container process is not making a standard action that would be more or equally limited as him. It is making a call to create a sibling container breaking the hierarchy completly, the process doesn't fork itself and then executes a new program, it asks for his parent to make a new child.

The isolation is broken, and while process isolation is important, here, the container isolation to the host is also broken, the container, having access to a process on the host that runs as root, allows for root access to the host.
