// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__rigidbody_msgs__msg__RobotCmd __attribute__((deprecated))
#else
# define DEPRECATED__rigidbody_msgs__msg__RobotCmd __declspec(deprecated)
#endif

namespace rigidbody_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotCmd_
{
  using Type = RobotCmd_<ContainerAllocator>;

  explicit RobotCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rigid_body_name = "";
      this->angular = 0.0;
      this->linear = 0.0;
    }
  }

  explicit RobotCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rigid_body_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rigid_body_name = "";
      this->angular = 0.0;
      this->linear = 0.0;
    }
  }

  // field types and members
  using _rigid_body_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _rigid_body_name_type rigid_body_name;
  using _angular_type =
    double;
  _angular_type angular;
  using _linear_type =
    double;
  _linear_type linear;

  // setters for named parameter idiom
  Type & set__rigid_body_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->rigid_body_name = _arg;
    return *this;
  }
  Type & set__angular(
    const double & _arg)
  {
    this->angular = _arg;
    return *this;
  }
  Type & set__linear(
    const double & _arg)
  {
    this->linear = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__rigidbody_msgs__msg__RobotCmd
    std::shared_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__rigidbody_msgs__msg__RobotCmd
    std::shared_ptr<rigidbody_msgs::msg::RobotCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotCmd_ & other) const
  {
    if (this->rigid_body_name != other.rigid_body_name) {
      return false;
    }
    if (this->angular != other.angular) {
      return false;
    }
    if (this->linear != other.linear) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotCmd_

// alias to use template instance with default allocator
using RobotCmd =
  rigidbody_msgs::msg::RobotCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace rigidbody_msgs

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_HPP_
