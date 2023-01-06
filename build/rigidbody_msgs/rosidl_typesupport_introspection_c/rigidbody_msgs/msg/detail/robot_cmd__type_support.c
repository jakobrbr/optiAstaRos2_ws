// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rigidbody_msgs/msg/detail/robot_cmd__rosidl_typesupport_introspection_c.h"
#include "rigidbody_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rigidbody_msgs/msg/detail/robot_cmd__functions.h"
#include "rigidbody_msgs/msg/detail/robot_cmd__struct.h"


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rigidbody_msgs__msg__RobotCmd__init(message_memory);
}

void rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_fini_function(void * message_memory)
{
  rigidbody_msgs__msg__RobotCmd__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_member_array[3] = {
  {
    "rigid_body_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RobotCmd, rigid_body_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angular",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RobotCmd, angular),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "linear",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RobotCmd, linear),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_members = {
  "rigidbody_msgs__msg",  // message namespace
  "RobotCmd",  // message name
  3,  // number of fields
  sizeof(rigidbody_msgs__msg__RobotCmd),
  rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_member_array,  // message members
  rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_init_function,  // function to initialize message memory (memory has to be allocated)
  rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_type_support_handle = {
  0,
  &rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rigidbody_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rigidbody_msgs, msg, RobotCmd)() {
  if (!rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_type_support_handle.typesupport_identifier) {
    rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &rigidbody_msgs__msg__RobotCmd__rosidl_typesupport_introspection_c__RobotCmd_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
