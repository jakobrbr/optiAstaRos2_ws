// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_H_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'rigid_body_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RobotCmd in the package rigidbody_msgs.
typedef struct rigidbody_msgs__msg__RobotCmd
{
  rosidl_runtime_c__String rigid_body_name;
  double angular;
  double linear;
} rigidbody_msgs__msg__RobotCmd;

// Struct for a sequence of rigidbody_msgs__msg__RobotCmd.
typedef struct rigidbody_msgs__msg__RobotCmd__Sequence
{
  rigidbody_msgs__msg__RobotCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rigidbody_msgs__msg__RobotCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__STRUCT_H_
