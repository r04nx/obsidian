# Lab Report: Docker and Container Management

## Student Information
- **Name:** Rohan Prakash Pawar
- **UID:** 2023201020
- **Branch:** EXTC
- **Date:** February 25, 2024

## Aim
To implement Docker containerization technology and gain practical experience in container management, focusing on single and multi-container applications using Docker and Docker Compose.
## Theory
## Theory
Docker is a platform for developing and running applications in isolated environments called containers. Containers package application code and dependencies into standardized units that run consistently across different environments. Unlike virtual machines, containers share the host OS kernel, making them lightweight and efficient.

## Lab Outcomes
Through this practical session, I learned to:
1. Set up Docker environment and verify installation
2. Create and manage Docker containers
3. Work with Docker images and container lifecycle
4. Implement multi-container setups using Docker Compose

## Software/Hardware Requirements
- Operating System: Ubuntu Linux 20.04 LTS
- Docker Engine v24.0.6  
- Docker Compose v2.21.0
- Internet connectivity for pulling images
- System with minimum 4GB RAM and 20GB storage

## Practical Implementation

## Requirements
- Operating System: Ubuntu Linux 20.04 LTS
- Docker Engine v24.0.6
- Docker Compose v2.21.0
- Minimum 4GB RAM and 20GB storage
- Internet connectivity
# Test with hello-world container
## Procedure and Results

### 1. Docker Setup and Verification
```bash
# Verify Docker installation
$ docker --version
Docker version 24.0.6, build ed223bc

# Test with hello-world container
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
$ docker ps
### 2. Container Management Implementation
```bash
# Pull and run nginx container
$ docker pull nginx
$ docker run -d -p 8080:80 nginx
7d14f0ddeb2b...

# List running containers
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
7d14f0ddeb2b   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 8 seconds    0.0.0.0:8080->80/tcp   romantic_edison

# Container lifecycle commands
$ docker stop 7d14f0ddeb2b
$ docker start 7d14f0ddeb2b
$ docker rm 7d14f0ddeb2b
```
    image: nginx
    ### 3. Multi-container Application Deployment
    Created and deployed a web application stack with nginx and postgres services:

    ```yaml
    # docker-compose.yml
    version: "3.7"
    services:
    web:
        image: nginx
        ports:
        - "8080:80"
    db:
        image: postgres
        environment:
        - POSTGRES_DB=myapp
        - POSTGRES_USER=user
        - POSTGRES_PASSWORD=password
    ```

    Deployment and verification:
    ```bash
    # Start services
    $ docker-compose up -d
    Creating network "myapp_default" with the default driver
    Creating myapp_db_1  ... done
    Creating myapp_web_1 ... done

    # Verify running services
    $ docker-compose ps
    Name                Command               State           Ports
    --------------------------------------------------------------------------
    myapp_db_1    docker-entrypoint.sh postgres    Up      5432/tcp
    myapp_web_1   nginx -g daemon off;             Up      0.0.0.0:8080->80/tcp
    ```
- Run first container

### Implementation Steps

1. **Docker Installation Verification**
```bash
docker --version
```
Output:
```
Docker version 24.0.6, build ed223bc
```

2. **First Container Test**
```bash
docker run hello-world
```
Output:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
## Part 2: Working with Docker Images and Containers

### Objective
- Learn basic Docker commands
- Manage containers and images
- Understand container lifecycle

### Implementation Steps

1. **Basic Container Management Commands**
```bash
# List running containers
docker ps
```
Output:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

```bash
# Pull and run nginx container
docker pull nginx
docker run -d -p 8080:80 nginx
```
Output:
```
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
2f44b7a888fa: Pull complete
Digest: sha256:a935d4ee...
Status: Downloaded newer image for nginx:latest
7d14f0ddeb2b...
```

2. **Container Lifecycle Management**
```bash
# Start container
docker start 7d14f0ddeb2b

# Stop container
docker stop 7d14f0ddeb2b

# Remove container
docker rm 7d14f0ddeb2b
```

## Practical Implementation

### 1. Docker Installation & Verification
```bash
# Check Docker version
docker --version
```
```
Docker version 24.0.6, build ed223bc
```

### 2. Basic Container Operations
```bash
# Run test container
docker run hello-world

# List running containers
docker ps

# Pull and run nginx container
docker pull nginx
docker run -d -p 8080:80 nginx
```

### 3. Container Management
```bash
# Container lifecycle commands
docker start 7d14f0ddeb2b
docker stop 7d14f0ddeb2b
docker rm 7d14f0ddeb2b
```

Here is a popular diagram illustrating the workflow between the different core components of Docker.


Here’s a step-by-step explanation:

## 1. Docker Client to Docker Host:

- `docker build`: The user (through the Docker client) can build a new image from a Dockerfile present in the local system. This command sends a build context to the Docker daemon.
- `docker pull`: The user can also pull an image from a registry to their local system. This is commonly used to download pre-built images.
- `docker run`: This command is used to run a container from an image. When the user wants to start an application or service, they issue this command.

## 2. Docker Host to Registry:

- The Docker daemon communicates with a registry to pull images (as requested by the `docker pull` command) or to push new images that have been built locally and need to be shared or stored remotely.

## 3. Images on Docker Host:

- This represents the local storage of images on the Docker host. Once an image is pulled from the registry or built locally, it’s stored here.

## 4. Running Containers:

- This shows multiple containers running on the Docker host. These are the active instances of the images, each running in isolation with its own environment, resources, etc.

The Docker client is where commands are issued. The Docker host does the work of building, running, and managing containers. The registry is where images are stored and shared.

Docker images are static templates containing the application code, libraries, and dependencies, whereas containers are running instances of these images, executed in isolation with their own CPU, memory, block I/O, and network resources, essentially acting as lightweight, portable virtual environments.

# Section 2: Installing Docker

To install Docker on Windows, follow these steps:

## 1. Install Windows Subsystem for Linux 2 (WSL 2) backend.

WSL 2 (Windows Subsystem for Linux version 2) is an enhanced Windows feature that enables users to run a GNU/Linux environment directly on Windows, without the overhead of a traditional virtual machine or dual-boot setup. It offers improved file system performance and full system call compatibility, allowing for a more authentic Linux experience on a Windows platform.


## 2. Download Docker Desktop for Windows:

Downloaded Docker Desktop installer for Windows from the official Docker website.

## 3. Run the Installer:

- Execute the Docker Desktop Installer.exe file you downloaded.
- Follow the install wizard to accept the license, authorize the installer, and proceed with the install.
- You may be asked to enable Hyper-V Windows Features or WSL during the installation process if they are not already enabled.

## 4. Reboot:

- Restart your computer to ensure the changes can take effect.

## 5. Start Docker Desktop:

- After rebooting, start Docker Desktop from the Windows Start menu.

## 6. Verify the Installation:

- Open a terminal window (like PowerShell or Command Prompt).
- Run the command `docker --version` to ensure Docker CLI can be called.
- Run `docker run hello-world` to verify that Docker can pull images and run

You should see this result:

Unable to find image 'hello-world:latest' locally                                         
latest: Pulling from library/hello-world                                                  
c1ec31eb5944: Pull complete                                                               
Digest: sha256:4bd78111b6914a99dbc560e6a20eab57ff6655aea4a80c50b0c5491968cbc2e6           
Status: Downloaded newer image for hello-world:latest                                     
                                                                                          
Hello from Docker!                                                                        
This message shows that your installation appears to be working correctly.                
                                                                                          
To generate this message, Docker took the following steps:                                
 1. The Docker client contacted the Docker daemon.                                        
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.                 
    (amd64)                                                                               
 3. The Docker daemon created a new container from that image which runs the              
    executable that produces the output you are currently reading.                        
 4. The Docker daemon streamed that output to the Docker client, which sent it            
    to your terminal.                                                                     
                                                                                          
To try something more ambitious, you can run an Ubuntu container with:                    
 $ docker run -it ubuntu bash                                                             
                                                                                          
Share images, automate workflows, and more with a free Docker ID:                         
 https://hub.docker.com/                                                                  
                                                                                          
For more examples and ideas, visit:                                                       
 https://docs.docker.com/get-started/                                                   

This shows that the docker image wasn’t found locally so the Docker run command automatically pulled the image from the Docker registry and ran it afterwards showing the message “Hello from Docker!”

## Basic Docker commands

Docker is managed primarily through a command-line interface (CLI), with commands that control Docker’s behavior and the lifecycles of containers and images. Here’s an introduction to some of the basic Docker commands:

`docker run`: This command is used to create and start a container from a specified image. For example, `docker run hello-world` will run a test container to ensure Docker is installed correctly.

`docker pull`: It fetches an image from a registry (like Docker Hub) without starting a container. For instance, `docker pull ubuntu` will download the Ubuntu image.

`docker push`: This uploads an image you've created to a registry. You must be logged in and have the right to push to the repository.

`docker build`: Used to create a new image from a Dockerfile. You run it in the directory where the Dockerfile is located, like `docker build -t my-image .`.

`docker images`: Lists all the images that are locally stored with the Docker engine.

`docker rmi`: Removes one or more images. Any containers using the image must be stopped and removed before the image can be removed.

`docker ps`: Lists running containers. Using `docker ps -a` will show all containers, including stopped ones.

`docker stop`: Stops a running container.

`docker start`: Starts a container that has been stopped.

`docker restart`: Restarts a container that's running or stopped.

`docker rm`: Deletes one or more containers. The container must be stopped before it can be removed.

`docker exec`: Runs a command in a running container. For example, `docker exec -it container_name bash` opens a bash shell in the container.

`docker logs`: Fetches the logs of a container. This is useful for debugging.

# Section 3: Your First Steps with Docker Containers

If you want to run a Node.js application inside a Docker container, you can follow these steps:

1. **Pull the Node.js Image:** Open a terminal and download the official Node.js image from Docker Hub using the `docker pull` command:

docker pull node

**2. Run a Container with the Node.js Image:** Use the `docker run` command to start a container from the Node.js image. You can execute a simple Node.js command directly for testing purposes. For example, to print "Hello World" with Node.js, you can run:

docker run -it --rm node

This command does the following:

- `docker run`: Tells Docker to run a container.
- `-it`: Allocates a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container.
- `--rm`: Automatically removes the container when it exits.
- `node`: The name of the image to use.

You should now see the following:

Welcome to Node.js v21.6.0.  
Type ".help" for more information.  
>

Open another terminal tab and type the following:

docker ps -a

You should clearly see that the container named “inspiring_williams” is running:

CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES  
277c4b7881ea   node          "docker-entrypoint.s…"   10 seconds ago   Up 9 seconds                          inspiring_williams

To stop the container, now type:

docker stop inspiring_williams

The container is now stopped and was automatically removed since we ran it using the `--rm` parameter.

## Lifecycle of a container

The lifecycle of a Docker container begins with its creation from an image using the `docker run` command. It then enters a running state, where it's actively executing. Containers can be stopped with `docker stop`, paused with `docker pause`, and restarted with `docker start`. Changes within a running container can be committed to create a new image. Finally, containers can be removed from the system using `docker rm`, cleaning up any resources they consumed.

# Section 4: Understanding Docker Images

Docker images are pre-configured snapshots of software environments, including the application and its dependencies. They work as immutable templates for creating Docker containers. You can pull existing images from Docker Hub, which is an online repository service where users and companies share images. By executing `docker pull <image-name>`, you can download any available image to your local environment, which you can then use to run containers with the exact setup specified in the image.

## Building a basic Docker image using a Dockerfile

Building a basic Docker image involves creating a Dockerfile, a text document containing all the commands a user could call on the command line to assemble the image. Here’s a step-by-step process:

## Create a Dockerfile:

- Start by creating an empty file named `Dockerfile` (no file extension) in your project directory.
- Define your base image using the `FROM` instruction. For instance, `FROM node:14` to use version 14 of the node image as your starting point.
- Use the `WORKDIR` instruction to set the working directory inside your container.
- Copy your application’s source code into the container using the `COPY` command, e.g., `COPY . /app`.
- If your application has dependencies, use the `RUN` command to install them. For a Node.js application, you might have `RUN npm install`.
- Specify the command to run your application using the `CMD` instruction, such as `CMD ["node", "app.js"]`.

**Dockerfile**

# Use an official Node.js runtime as the base image  
FROM node:14  
  
# Set the working directory inside the container  
WORKDIR /app  
  
# Copy package.json and package-lock.json to the container  
COPY package*.json ./  
  
# Install Node.js dependencies  
RUN npm install  
  
# Copy the rest of the application code to the container  
COPY . .  
  
# Expose a port that the application will listen on  
EXPOSE 3000  
  
# Define the command to run your Node.js application  
CMD ["node", "app.js"]

You can customize this Dockerfile according to the specific requirements of your Node.js application. Don’t forget to create the `app.js` file as it’s the actual entry point file of your application. This means that when the application is executed, Node.js starts by running the `app.js` file. It acts as the central control point, initializing and orchestrating various components, making it the first file executed when your Node.js application is launched.

**app.js**

console.log("Hello World!");

## Build the Docker Image:

- In your terminal, navigate to the directory containing your Dockerfile.
- Run the command `docker build -t your-image-name .` to build your Docker image. The `-t` flag tags your image with a name, and the `.` tells Docker to use the current directory for the Dockerfile and build context.

## Verify the Image:

- After the build completes, use `docker images` to see your new image listed.

REPOSITORY                              TAG              IMAGE ID       CREATED              SIZE  
node-js-image                           latest           91e368e7222d   About a minute ago   912MB

## Run a Container from Your Image:

- You can now start a container from your image using `docker run -p 4000:80 your-image-name`, where `-p` maps a port on your local machine to a port in the container.

Hello World!

# Section 5: Beginner Tips and Resources

Getting started with Docker can be a rewarding experience, but it might seem a bit overwhelming at first. Here are some beginner tips and resources to help you on your learning path.

- **Understand the Basics:** Start by grasping the fundamental concepts of Docker. Understand what containers are, how they differ from virtual machines, and why Docker is so popular for containerization.
- **Docker Hub:** Docker Hub is a repository for Docker images. You can find thousands of pre-built Docker images for various software applications and operating systems here. It’s a great resource to get you started without having to build everything from scratch.
- **Docker CLI:** Familiarize yourself with the Docker command-line interface (CLI). Learn essential commands like `docker run`, `docker build`, `docker pull`, and `docker ps`. The CLI is your primary tool for interacting with Docker.
- **Dockerfile:** Understand Dockerfiles, which are used to define how a Docker image is built. Learn to create and customize Dockerfiles to package your applications into containers.
- **Container Lifecycle:** Learn about the lifecycle of a Docker container. This includes creating, running, stopping, and removing containers. Understand the difference between running containers in the foreground and the background.

In Docker, advanced concepts like networking, volumes, bind mounts, and Docker Compose extend the platform’s functionality beyond basic containerization. Networking allows precise control over container communication, while volumes and bind mounts enable data persistence and sharing between containers and the host. Docker Compose simplifies managing multi-container applications, enhancing orchestration and scalability. These advanced features empower users to tackle complex scenarios, from building distributed applications to securely managing secrets and configurations, making Docker a versatile tool for various development and deployment needs.


## Key Learnings
## Results and Discussion
The following objectives were successfully achieved:

1. **Docker Environment Setup**
- Successfully installed and configured Docker environment
- Verified functionality with test containers
- Mastered basic Docker CLI commands

## Results and Analysis
The laboratory work successfully achieved the following objectives:

1. **Docker Environment Setup**
- Installed and configured Docker environment
- Verified functionality with hello-world container
- Demonstrated proficiency in basic Docker commands

2. **Container Management**
- Created and managed nginx container
- Implemented container lifecycle operations
- Successfully managed container states

3. **Multi-container Implementation**
- Created web application stack with nginx and postgres
- Implemented service orchestration using Docker Compose
- Verified multi-container networking and communication
- Troubleshooting and managing container states
## Conclusion
This laboratory provided practical experience with Docker containerization technology. The hands-on implementation helped develop essential skills in container management, from basic Docker operations to multi-container orchestration with Docker Compose. Key accomplishments include:

- Successfully deployed single and multi-container applications
- Demonstrated container lifecycle management
- Implemented service orchestration using Docker Compose
- Applied container networking and environment configuration
- Gained practical experience with container deployment workflows
## References
1. Docker Command Line Interface Documentation
2. Docker Compose Documentation
3. Docker Container Best Practices Guide
4. Docker Image Management Documentation
5. Docker Networking Guide
- Implemented multi-container applications with Docker Compose
- Applied networking and volume management concepts

2. **Technical Proficiency Gained:**
- Understanding of container architecture and management
- Experience with image building and customization
- Practical knowledge of Docker Compose for orchestration
- Troubleshooting and debugging container issues
- Implementation of Docker best practices

3. **Real-world Applications:**
- Deployment of web applications using containers
- Database containerization and management
- Multi-container application orchestration
- Environment consistency across development stages
- Containerized development workflows

4. **Challenges Overcome:**
- Container networking configuration
- Volume management for data persistence
- Multi-container orchestration setup
- Environment variable management
- Container resource optimization

5. **Future Learning Paths:**
- Advanced Docker security practices
- Container orchestration with Kubernetes
- Microservices architecture implementation
- CI/CD pipeline integration
- Container monitoring and logging

This laboratory has equipped me with essential containerization skills crucial for modern DevOps practices and cloud-native application development. The hands-on experience has provided a strong foundation for implementing containerized solutions in production environments.

## References
1. Docker Command Line Interface Documentation
2. Docker Compose User Guide
3. Docker Container Best Practices
4. Docker Image Management Guide
5. Container Orchestration Documentation


## Part 3: Docker Compose Implementation

Docker Compose enables managing multi-container applications using a single YAML configuration file. This section demonstrates the practical implementation of Docker Compose for container orchestration.

### Objective
- Set up multi-container application using Docker Compose
- Manage container dependencies and networking
- Implement volume management for data persistence

### Docker Compose Implementation Steps

1. **Creating docker-compose.yml**
```yaml
version: "3.7"
services:
web:
    image: nginx
    ports:
    - "8080:80"
db:
    image: postgres
    environment:
    - POSTGRES_DB=myapp
    - POSTGRES_USER=user
    - POSTGRES_PASSWORD=password
```

2. **Running Multi-Container Setup**
```bash
# Start containers
docker-compose up -d
```
Output:
```
Creating network "myapp_default" with the default driver
Creating myapp_db_1  ... done
Creating myapp_web_1 ... done
```

Let’s see what these elements actually are.

3. **Managing Containers**
```bash
# List running containers
docker-compose ps
```
Output:
```
Name                Command               State           Ports
--------------------------------------------------------------------------
myapp_db_1    docker-entrypoint.sh postgres    Up      5432/tcp
myapp_web_1   nginx -g daemon off;             Up      0.0.0.0:8080->80/tcp
```

4. **Service Operations**
```bash
# Stop services
docker-compose stop

# Start services
docker-compose start

# Remove containers and networks
docker-compose down
```

There are multiple settings that we can apply to services.

- **Pulling an Image :**

Sometimes, the image we need for our service has already been published (by us or by others) in [Docker Hub](https://hub.docker.com/), or another Docker Registry. If that’s the case, then we refer to it with the image attribute, by specifying the image name and tag:

services:  my-service:    image: ubuntu:latest    ...

- **Building an Image :**

Instead, we might need to [build](https://docs.docker.com/compose/compose-file/#build) an image from the source code by reading its _Dockerfile_. This time, we’ll use the _build_ keyword, passing the path to the Dockerfile as the value:

services:  my-custom-app:    build: /path/to/dockerfile/    ...

- **Configuring the Networking :**

Docker containers communicate between themselves in networks created, implicitly or through configuration, by Docker Compose. A service can communicate with another service on the same network by simply referencing it by container name and port (for example _network-example-service:80_), provided that we’ve made the port accessible through the _expose_ keyword:

services:  network-example-service:    image: karthequian/helloworld:latest    expose:      - "80"

- **Setting Up the Volumes :**

There are three types of volumes: [_anonymous_, _named_, and _host_](https://success.docker.com/article/different-types-of-volumes) ones. Docker manages both anonymous and named volumes, automatically mounting them in self-generated directories in the host. While anonymous volumes were useful with older versions of Docker, named ones are the suggested way to go nowadays. Host volumes also allow us to specify an existing folder in the host. We can configure host volumes at the service level and named volumes in the outer level of the configuration, in order to make the latter visible to other containers and not only to the one they belong:

services:  volumes-example-service:    image: alpine:latest    volumes:      - my-named-global-volume:/my-volumes/named-global-volume      - /tmp:/my-volumes/host-volume      - /home:/my-volumes/readonly-host-volume:ro    ...  another-volumes-example-service:    image: alpine:latest    volumes:      - my-named-global-volume:/another-path/the-same-named-volume    ...volumes:  my-named-global-volume:

Here, both containers will have read/write access to the _my-named-global-volume_ shared folder, no matter the different paths they’ve mapped it to. The two host volumes, instead, will be available only to _volumes-example-service_. The _/tmp_ folder of the host’s file system is mapped to the _/my-volumes/host-volume_ folder of the container. This portion of the file system is writeable, which means that the container can not only read but also write (and delete) files in the host machine.

- **Declaring the Dependencies :**

Often, we need to create a dependency chain between our services, so that some services get loaded before (and unloaded after) other ones. We can achieve this result through the _depends_on_ keyword:

services:  kafka:    image: wurstmeister/kafka:2.11-0.11.0.3    depends_on:      - zookeeper    ...  zookeeper:    image: wurstmeister/zookeeper    ...

We should be aware, however, that Compose will not wait for the _zookeeper_ service to finish loading before starting the _kafka_ service: it will simply wait for it to start. If we need a service to be fully loaded before starting another service, we need to get deeper control of startup and shutdown order in Compose.



## **2. Volumes & Networks**

_Volumes_, on the other hand, are physical areas of disk space shared between the host and a container, or even between containers. In other words, a volume is a shared directory in the host, visible from some or all containers. Similarly, _networks_ define the communication rules between containers, and between a container and the host. Common network zones will make containers’ services discoverable by each other, while private zones will segregate them in virtual sandboxes.

## 3. **Managing Environment Variables :**

Working with environment variables is easy in Compose. We can define static environment variables, and also define dynamic variables with the _${}_ notation:

services:  database:    image: "postgres:${POSTGRES_VERSION}"    environment:      DB: mydb      USER: "${USER}"

There are different methods to provide those values to Compose. For example, one is setting them in a _.env_ file in the same directory, structured like a _.properties_ file, _key=value_:

POSTGRES_VERSION=alpineUSER=foo

Otherwise, we can set them in the OS before calling the command:

export POSTGRES_VERSION=alpineexport USER=foodocker-compose up

Finally, we might find handy using a simple one-liner in the shell:

POSTGRES_VERSION=alpine USER=foo docker-compose up

We can mix the approaches, but let’s keep in mind that Compose uses the following priority order, overwriting the less important with the higher ones:

1. Compose file
2. Shell environment variables
3. Environment file
4. Dockerfile
5. Variable not defined

## **3. Scaling and Replicas :**

In older Compose versions, we were allowed to scale the instances of a container through the [_docker-compose scale_](https://docs.docker.com/compose/reference/scale/) command. Newer versions deprecated it and replaced it with the _— –scale_ option. On the other side, we can exploit [Docker Swarm](https://docs.docker.com/engine/swarm/) — a cluster of Docker Engines — and autoscale our containers declaratively through the _replicas_ attribute of the _deploy_ section:

services:  worker:    image: dockersamples/examplevotingapp_worker  networks:    - frontend    - backend  deploy:    mode: replicated    replicas: 6    resources:      limits:        cpus: '0.50'        memory: 50M      reservations:        cpus: '0.25'        memory: 20M      ...

Under _deploy,_ we can also specify many other options, like the resources thresholds. Compose, however, considers the whole _deploy_ section only when deploying to Swarm, and ignores it otherwise.

## **Lifecycle Management**

Let’s finally take a closer look at the syntax of Docker Compose:

docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]

While there are [many options and commands available](https://docs.docker.com/compose/reference/overview/), we need at least to know the ones to activate and deactivate the whole system correctly.

To start Docker Compose :

docker-compose up

After the first time, however, we can simply use _start_ to start the services:

docker-compose start

In case our file has a different name than the default one (_docker-compose.yml_), we can exploit the _-f_ and _— file_ flags to specify an alternate file name:

docker-compose -f custom-compose-file.yml start

Compose can also run in the background as a daemon when launched with the _-d_ option:

docker-compose up -d

To safely stop the active services, we can use _stop_, which will preserve containers, volumes, and networks, along with every modification made to them:

docker-compose stop

To reset the status of our project, instead, we simply run _down_, which will destroy everything with only the exception of external volumes:

docker-compose down