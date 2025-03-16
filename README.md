# `rol_fby_kisbeadando` package
ROS 2 C++ package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
A package két node-ból áll. A /gen_node tangens jelet és korlátozottan véletlen számokat generál, amiket két std_msgs/float32 topicban hirdet. A /sum_node a összegzi az előállított topicokat és egy újabb std_msgs/float32 topicban hirdeti. Megvalósítás ROS 2 Humble alatt.
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` 
cd ~/ros2_ws/src
```
``` 
git clone https://github.com/peterbela/rol_fby_kisbeadando
```

### Build ROS 2 packages
``` 
cd ~/ros2_ws
```
``` 
colcon build --packages-select rol_fby_kisbeadando --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

```
ros2 launch rol_fby_kisbeadando launch_example1.launch.cpp
```
```
ros2 run rol_fby_kisbeadando gen_node
```
```
ros2 run rol_fby_kisbeadando sum_node 
```
###Graph
```


``` 
