// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "rigidbody_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "rigidbody_msgs/msg/detail/robot_cmd__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace rigidbody_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rigidbody_msgs
cdr_serialize(
  const rigidbody_msgs::msg::RobotCmd & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rigidbody_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  rigidbody_msgs::msg::RobotCmd & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rigidbody_msgs
get_serialized_size(
  const rigidbody_msgs::msg::RobotCmd & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rigidbody_msgs
max_serialized_size_RobotCmd(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace rigidbody_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rigidbody_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, rigidbody_msgs, msg, RobotCmd)();

#ifdef __cplusplus
}
#endif

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
