FROM ros:noetic-robot

RUN apt update &&\
    apt install -y \
    ros-noetic-joint-state-publisher-gui \
    python3-catkin-tools \
    python3-rosdep \
    python3-rosinstall-generator \
    python3-vcstool \
    python3-pip \
    ros-noetic-rviz

RUN pip3 install catkin_tools

RUN rosdep update

RUN mkdir -p /catkin_ws/src
WORKDIR /catkin_ws/src/
COPY . /catkin_ws/src/micro_resector_description

WORKDIR /catkin_ws/
RUN ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && \
    catkin build"]
