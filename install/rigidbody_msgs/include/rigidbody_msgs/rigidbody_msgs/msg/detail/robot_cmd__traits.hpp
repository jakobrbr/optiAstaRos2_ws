// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__TRAITS_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "rigidbody_msgs/msg/detail/robot_cmd__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace rigidbody_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RobotCmd & msg,
  std::ostream & out)
{
  out << "{";
  // member: rigid_body_name
  {
    out << "rigid_body_name: ";
    rosidl_generator_traits::value_to_yaml(msg.rigid_body_name, out);
    out << ", ";
  }

  // member: angular
  {
    out << "angular: ";
    rosidl_generator_traits::value_to_yaml(msg.angular, out);
    out << ", ";
  }

  // member: linear
  {
    out << "linear: ";
    rosidl_generator_traits::value_to_yaml(msg.linear, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: rigid_body_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rigid_body_name: ";
    rosidl_generator_traits::value_to_yaml(msg.rigid_body_name, out);
    out << "\n";
  }

  // member: angular
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angular: ";
    rosidl_generator_traits::value_to_yaml(msg.angular, out);
    out << "\n";
  }

  // member: linear
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear: ";
    rosidl_generator_traits::value_to_yaml(msg.linear, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotCmd & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace rigidbody_msgs

namespace rosidl_generator_traits
{

[[deprecated("use rigidbody_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const rigidbody_msgs::msg::RobotCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  rigidbody_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use rigidbody_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const rigidbody_msgs::msg::RobotCmd & msg)
{
  return rigidbody_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<rigidbody_msgs::msg::RobotCmd>()
{
  return "rigidbody_msgs::msg::RobotCmd";
}

template<>
inline const char * name<rigidbody_msgs::msg::RobotCmd>()
{
  return "rigidbody_msgs/msg/RobotCmd";
}

template<>
struct has_fixed_size<rigidbody_msgs::msg::RobotCmd>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<rigidbody_msgs::msg::RobotCmd>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<rigidbody_msgs::msg::RobotCmd>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__TRAITS_HPP_
