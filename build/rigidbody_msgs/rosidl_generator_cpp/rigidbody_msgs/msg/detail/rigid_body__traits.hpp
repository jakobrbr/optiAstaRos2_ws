// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rigidbody_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__TRAITS_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "rigidbody_msgs/msg/detail/rigid_body__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
// Member 'rot'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace rigidbody_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RigidBody & msg,
  std::ostream & out)
{
  out << "{";
  // member: rigid_body_name
  {
    out << "rigid_body_name: ";
    rosidl_generator_traits::value_to_yaml(msg.rigid_body_name, out);
    out << ", ";
  }

  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
    out << ", ";
  }

  // member: rot
  {
    out << "rot: ";
    to_flow_style_yaml(msg.rot, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RigidBody & msg,
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

  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }

  // member: rot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rot:\n";
    to_block_style_yaml(msg.rot, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RigidBody & msg, bool use_flow_style = false)
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
  const rigidbody_msgs::msg::RigidBody & msg,
  std::ostream & out, size_t indentation = 0)
{
  rigidbody_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use rigidbody_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const rigidbody_msgs::msg::RigidBody & msg)
{
  return rigidbody_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<rigidbody_msgs::msg::RigidBody>()
{
  return "rigidbody_msgs::msg::RigidBody";
}

template<>
inline const char * name<rigidbody_msgs::msg::RigidBody>()
{
  return "rigidbody_msgs/msg/RigidBody";
}

template<>
struct has_fixed_size<rigidbody_msgs::msg::RigidBody>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<rigidbody_msgs::msg::RigidBody>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<rigidbody_msgs::msg::RigidBody>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__RIGID_BODY__TRAITS_HPP_
