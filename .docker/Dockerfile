FROM ros:foxy

RUN apt update &&\
    apt install -y \
    software-properties-common \
    ssh \
    git \
    udev \
    usbutils \
    libboost-dev \
    python3-pip \
    python3-vcstool \
    build-essential \
    cmake \
    python3-colcon-common-extensions \
    python3-flake8 \
    python3-pytest-cov \
    python3-rosdep \
    python3-setuptools \
    python3-vcstool \
    ros-foxy-xacro \
    wget \
    ros-foxy-joint-state-publisher-gui \
    ros-foxy-rviz2 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /dev_ws/src
WORKDIR /dev_ws/src/
COPY . /dev_ws/src/micro_resector_description

WORKDIR /dev_ws/
RUN ["/bin/bash", "-c", "source /opt/ros/foxy/setup.bash && \
    colcon build"]
