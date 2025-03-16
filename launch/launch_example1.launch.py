#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <cmath>  

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"

using namespace std::chrono_literals;

class GenTanAndRand : public rclcpp::Node
{
public:
    GenTanAndRand(): Node("gen_node"), count_(0)
    {
        RCLCPP_INFO(this->get_logger(), "Generating tangent and random numbers");
        pub_tan_ = this->create_publisher<std_msgs::msg::Float32>("tangent", 10);
        pub_rand_ = this->create_publisher<std_msgs::msg::Float32>("rand", 10);
        timer_ = this->create_wall_timer(50ms, std::bind(&GenTanAndRand::timer_callback, this));
    }

private:
    void timer_callback()
    {
        auto message_tan = std_msgs::msg::Float32();
        auto message_rand = std_msgs::msg::Float32();
        
        message_tan.data = tan(count_++ / 50.0) * 100;  // A tangens értéket 100-zal szorozzuk
        
        message_rand.data = rand() % 5; 
        
        pub_tan_->publish(message_tan);
        pub_rand_->publish(message_rand);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr pub_tan_, pub_rand_;
    size_t count_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<GenTanAndRand>());
    rclcpp::shutdown();
    return 0;
}
