# AIRAK Mobility

## Installation

### Prerequisites
- Ubuntu 18.04 x86_64
- ROS Melodic / Noetic 
  
  (http://wiki.ros.org/noetic/Installation/Ubuntu)

- Intel RealSense SDK 2.0 
  
  (https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages)

- imu_tools ROS package

  (http://wiki.ros.org/imu_tools)

  ``` bash
  sudo apt-get install ros-$ROS_DISTRO-imu-tools
  ```

- rtabmap_ros

  (https://github.com/introlab/rtabmap_ros)

  ```bash
  sudo apt-get install ros-$ROS_DISTRO-rtabmap-ros
  ```

- move_base

  (http://wiki.ros.org/move_base)

  ```bash
  sudo apt-get install ros-$ROS_DISTRO-navigation
  ```

*change $ROS_DISTRO to match you ROS distribution

### Download and Build

  ```bash
  git clone https://github.com/p-amonpitakpun/airak-mobility.git
  cd airak-mobility
  git submodule init
  git submodule update --recursive
  ```
  ```bash
  source /opt/ros/$ROS_DISTRO/setup.bash
  catkin build -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
  ```

  ```bash
  source devel/setup.bash
  ```

## Usage Instructions
  ### Launch Nodes
  For the first terminal, launch tf camera and imu nodes.
  ```bash
  source devel/setup.bash
  roslaunch airak-bringup bringup.launch
  ```

  For the second terminal, launch mapping nodes.
  ```bash
  source devel/setup.bash
  roslaunch airak-mapping mapping_only.launch
  ```

  For the third terminal, start rviz visualization node.
  ```bash
  rviz -d src/airak-mapping/launch/config/mapping.rviz
  ```

  ### Parameters

  - airak-bringup/launch/bringup.launch
    - camera_offset_x
    - camera_offset_y
    - camera_offset_z
    - camera_orient_roll
    - camera_orient_pitch
    - camera_orient_yaw

      ...

    - realsense-ros parameters

  - airak-mapping/launch/mapping_only.launch
    - rtabmap-ros parameters