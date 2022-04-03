ARG ROS_DISTRO=foxy
ARG ROS2_WS=/opt/ros/ros2_ws
ARG ROS2_PKG=nbot_description

FROM ros:foxy as ROS-FOXY-NAV2-BASE
ARG ROS_DISTRO
ENV ROS_DISTRO=$ROS_DISTRO

RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y ros-$ROS_DISTRO-xacro \
                       ros-$ROS_DISTRO-gazebo-ros-pkgs \
                       ros-$ROS_DISTRO-navigation2 \
                       ros-$ROS_DISTRO-nav2-bringup \
                       ros-$ROS_DISTRO-joint-state-publisher &&\
    apt-get install -y python3-pip && \
    python3 -m pip install pyserial

FROM ROS-FOXY-NAV2-BASE as ROS-FOXY-NAV2-BRINGUP
ARG ROS2_WS
ARG ROS2_PKG

WORKDIR $ROS2_WS/src/$ROS2_PKG
COPY . .

WORKDIR $ROS2_WS
RUN rosdep install -y \
        --from-paths src \
        --ignore-src 

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build --symlink-install

SHELL ["/bin/bash", "-c", "source install/setup.bash"]