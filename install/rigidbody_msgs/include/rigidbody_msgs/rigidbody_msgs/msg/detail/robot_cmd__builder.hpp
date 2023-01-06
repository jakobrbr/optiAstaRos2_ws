// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__BUILDER_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rigidbody_msgs/msg/detail/robot_cmd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rigidbody_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotCmd_linear
{
public:
  explicit Init_RobotCmd_linear(::rigidbody_msgs::msg::RobotCmd & msg)
  : msg_(msg)
  {}
  ::rigidbody_msgs::msg::RobotCmd linear(::rigidbody_msgs::msg::RobotCmd::_linear_type arg)
  {
    msg_.linear = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rigidbody_msgs::msg::RobotCmd msg_;
};

class Init_RobotCmd_angular
{
public:
  explicit Init_RobotCmd_angular(::rigidbody_msgs::msg::RobotCmd & msg)
  : msg_(msg)
  {}
  Init_RobotCmd_linear angular(::rigidbody_msgs::msg::RobotCmd::_angular_type arg)
  {
    msg_.angular = std::move(arg);
    return Init_RobotCmd_linear(msg_);
  }

private:
  ::rigidbody_msgs::msg::RobotCmd msg_;
};

class Init_RobotCmd_rigid_body_name
{
public:
  Init_RobotCmd_rigid_body_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotCmd_angular rigid_body_name(::rigidbody_msgs::msg::RobotCmd::_rigid_body_name_type arg)
  {
    msg_.rigid_body_name = std::move(arg);
    return Init_RobotCmd_angular(msg_);
  }

private:
  ::rigidbody_msgs::msg::RobotCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rigidbody_msgs::msg::RobotCmd>()
{
  return rigidbody_msgs::msg::builder::Init_RobotCmd_rigid_body_name();
}

}  // namespace rigidbody_msgs

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__BUILDER_HPP_
