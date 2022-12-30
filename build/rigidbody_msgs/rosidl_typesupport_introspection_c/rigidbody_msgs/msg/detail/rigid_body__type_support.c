// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rigidbody_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rigidbody_msgs/msg/detail/rigid_body__rosidl_typesupport_introspection_c.h"
#include "rigidbody_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rigidbody_msgs/msg/detail/rigid_body__functions.h"
#include "rigidbody_msgs/msg/detail/rigid_body__struct.h"


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
// Member `rot`
#include "geometry_msgs/msg/point.h"
// Member `pose`
// Member `rot`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rigidbody_msgs__msg__RigidBody__init(message_memory);
}

void rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_fini_function(void * message_memory)
{
  rigidbody_msgs__msg__RigidBody__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[3] = {
  {
    "rigid_body_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RigidBody, rigid_body_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RigidBody, pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rot",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rigidbody_msgs__msg__RigidBody, rot),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_members = {
  "rigidbody_msgs__msg",  // message namespace
  "RigidBody",  // message name
  3,  // number of fields
  sizeof(rigidbody_msgs__msg__RigidBody),
  rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array,  // message members
  rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_init_function,  // function to initialize message memory (memory has to be allocated)
  rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle = {
  0,
  &rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rigidbody_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rigidbody_msgs, msg, RigidBody)() {
  rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle.typesupport_identifier) {
    rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &rigidbody_msgs__msg__RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
