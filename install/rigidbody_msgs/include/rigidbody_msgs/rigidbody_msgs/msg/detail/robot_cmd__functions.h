// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice

#ifndef RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__FUNCTIONS_H_
#define RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "rigidbody_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "rigidbody_msgs/msg/detail/robot_cmd__struct.h"

/// Initialize msg/RobotCmd message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * rigidbody_msgs__msg__RobotCmd
 * )) before or use
 * rigidbody_msgs__msg__RobotCmd__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__init(rigidbody_msgs__msg__RobotCmd * msg);

/// Finalize msg/RobotCmd message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
void
rigidbody_msgs__msg__RobotCmd__fini(rigidbody_msgs__msg__RobotCmd * msg);

/// Create msg/RobotCmd message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * rigidbody_msgs__msg__RobotCmd__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
rigidbody_msgs__msg__RobotCmd *
rigidbody_msgs__msg__RobotCmd__create();

/// Destroy msg/RobotCmd message.
/**
 * It calls
 * rigidbody_msgs__msg__RobotCmd__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
void
rigidbody_msgs__msg__RobotCmd__destroy(rigidbody_msgs__msg__RobotCmd * msg);

/// Check for msg/RobotCmd message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__are_equal(const rigidbody_msgs__msg__RobotCmd * lhs, const rigidbody_msgs__msg__RobotCmd * rhs);

/// Copy a msg/RobotCmd message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__copy(
  const rigidbody_msgs__msg__RobotCmd * input,
  rigidbody_msgs__msg__RobotCmd * output);

/// Initialize array of msg/RobotCmd messages.
/**
 * It allocates the memory for the number of elements and calls
 * rigidbody_msgs__msg__RobotCmd__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__Sequence__init(rigidbody_msgs__msg__RobotCmd__Sequence * array, size_t size);

/// Finalize array of msg/RobotCmd messages.
/**
 * It calls
 * rigidbody_msgs__msg__RobotCmd__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
void
rigidbody_msgs__msg__RobotCmd__Sequence__fini(rigidbody_msgs__msg__RobotCmd__Sequence * array);

/// Create array of msg/RobotCmd messages.
/**
 * It allocates the memory for the array and calls
 * rigidbody_msgs__msg__RobotCmd__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
rigidbody_msgs__msg__RobotCmd__Sequence *
rigidbody_msgs__msg__RobotCmd__Sequence__create(size_t size);

/// Destroy array of msg/RobotCmd messages.
/**
 * It calls
 * rigidbody_msgs__msg__RobotCmd__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
void
rigidbody_msgs__msg__RobotCmd__Sequence__destroy(rigidbody_msgs__msg__RobotCmd__Sequence * array);

/// Check for msg/RobotCmd message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__Sequence__are_equal(const rigidbody_msgs__msg__RobotCmd__Sequence * lhs, const rigidbody_msgs__msg__RobotCmd__Sequence * rhs);

/// Copy an array of msg/RobotCmd messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_rigidbody_msgs
bool
rigidbody_msgs__msg__RobotCmd__Sequence__copy(
  const rigidbody_msgs__msg__RobotCmd__Sequence * input,
  rigidbody_msgs__msg__RobotCmd__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // RIGIDBODY_MSGS__MSG__DETAIL__ROBOT_CMD__FUNCTIONS_H_
