import docker

#Create a Docker client
client = docker.from_env()

IMAGE = 'environment-mysql:latest'

#Define the container configuration
container_config = {
    'image':{IMAGE}
}

#Create the container
container = client.containers.create(**container_config)

#Start the container
container.start()

#Print the container ID
print(f'Container ID: {container.id}')
