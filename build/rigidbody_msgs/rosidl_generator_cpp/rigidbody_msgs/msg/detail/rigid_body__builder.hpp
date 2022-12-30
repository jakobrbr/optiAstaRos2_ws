// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rigidbody_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rigidbody_msgs/msg/detail/rigid_body__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rigidbody_msgs
{

namespace msg
{

namespace builder
{

class Init_RigidBody_rot
{
public:
  explicit Init_RigidBody_rot(::rigidbody_msgs::msg::RigidBody & msg)
  : msg_(msg)
  {}
  ::rigidbody_msgs::msg::RigidBody rot(::rigidbody_msgs::msg::RigidBody::_rot_type arg)
  {
    msg_.rot = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rigidbody_msgs::msg::RigidBody msg_;
};

class Init_RigidBody_pose
{
public:
  explicit Init_RigidBody_pose(::rigidbody_msgs::msg::RigidBody & msg)
  : msg_(msg)
  {}
  Init_RigidBody_rot pose(::rigidbody_msgs::msg::RigidBody::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_RigidBody_rot(msg_);
  }

private:
  ::rigidbody_msgs::msg::RigidBody msg_;
};

class Init_RigidBody_rigid_body_name
{
public:
  Init_RigidBody_rigid_body_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RigidBody_pose rigid_body_name(::rigidbody_msgs::msg::RigidBody::_rigid_body_name_type arg)
  {
    msg_.rigid_body_name = std::move(arg);
    return Init_RigidBody_pose(msg_);
  }

private:
  ::rigidbody_msgs::msg::RigidBody msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rigidbody_msgs::msg::RigidBody>()
{
  return rigidbody_msgs::msg::builder::Init_RigidBody_rigid_body_name();
}

}  // namespace rigidbody_msgs

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_
