ARG ROS2_WS=/opt/ros/ros2_ws
ARG ROS2_PKG=py_serial

FROM ros:foxy

ARG ROS2_WS

# SERIAL env

WORKDIR $ROS2_WS/src/$ROS2_PKG
COPY . .

WORKDIR $ROS2_WS
RUN apt-get update && \
    rosdep install -y \
        --from-paths src \
        --ignore-src &&\
    apt-get install -y python3-pip && \
    python3 -m pip install pyserial

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build --symlink-install

ENV ROS2_WS $ROS2_WS

ENV SERIAL_TOPIC='/serial/get'
ENV SERIAL_PORT='/dev/pts/3'
ENV SERIAL_BAUDRATE='115200'

SHELL ["/bin/bash", "-c", "source install/setup.bash"]