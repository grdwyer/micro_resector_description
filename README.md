# Micro-Resector Description

# URDFs
## Stages
  * ECSx5050
  * ECR5050

## Tools
  * Scalpel (Swan Morton SM65A)


# Docker
## Build
`docker build --pull --rm -f ./.docker/Dockerfile  -t micro_resector_description:tool_update .`

## Run
```
docker run -it \
    --user=$(id -u $USER):$(id -g $USER) \
    --group-add sudo \
    --env="DISPLAY" \
    --workdir="/catkin_ws/src" \
    --volume="/home/$USER:/home/$USER" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    micro_resector_description:tool_update
```

docker run -it \
    --env="DISPLAY" \
    --workdir="/catkin_ws/src" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    micro_resector_description:tool_update

xhost + local: