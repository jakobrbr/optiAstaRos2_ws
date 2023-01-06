// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rigidbody_msgs:msg/RobotCmd.idl
// generated code does not contain a copyright notice
#include "rigidbody_msgs/msg/detail/robot_cmd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"

bool
rigidbody_msgs__msg__RobotCmd__init(rigidbody_msgs__msg__RobotCmd * msg)
{
  if (!msg) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__init(&msg->rigid_body_name)) {
    rigidbody_msgs__msg__RobotCmd__fini(msg);
    return false;
  }
  // angular
  // linear
  return true;
}

void
rigidbody_msgs__msg__RobotCmd__fini(rigidbody_msgs__msg__RobotCmd * msg)
{
  if (!msg) {
    return;
  }
  // rigid_body_name
  rosidl_runtime_c__String__fini(&msg->rigid_body_name);
  // angular
  // linear
}

bool
rigidbody_msgs__msg__RobotCmd__are_equal(const rigidbody_msgs__msg__RobotCmd * lhs, const rigidbody_msgs__msg__RobotCmd * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->rigid_body_name), &(rhs->rigid_body_name)))
  {
    return false;
  }
  // angular
  if (lhs->angular != rhs->angular) {
    return false;
  }
  // linear
  if (lhs->linear != rhs->linear) {
    return false;
  }
  return true;
}

bool
rigidbody_msgs__msg__RobotCmd__copy(
  const rigidbody_msgs__msg__RobotCmd * input,
  rigidbody_msgs__msg__RobotCmd * output)
{
  if (!input || !output) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__copy(
      &(input->rigid_body_name), &(output->rigid_body_name)))
  {
    return false;
  }
  // angular
  output->angular = input->angular;
  // linear
  output->linear = input->linear;
  return true;
}

rigidbody_msgs__msg__RobotCmd *
rigidbody_msgs__msg__RobotCmd__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RobotCmd * msg = (rigidbody_msgs__msg__RobotCmd *)allocator.allocate(sizeof(rigidbody_msgs__msg__RobotCmd), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rigidbody_msgs__msg__RobotCmd));
  bool success = rigidbody_msgs__msg__RobotCmd__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rigidbody_msgs__msg__RobotCmd__destroy(rigidbody_msgs__msg__RobotCmd * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rigidbody_msgs__msg__RobotCmd__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rigidbody_msgs__msg__RobotCmd__Sequence__init(rigidbody_msgs__msg__RobotCmd__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RobotCmd * data = NULL;

  if (size) {
    data = (rigidbody_msgs__msg__RobotCmd *)allocator.zero_allocate(size, sizeof(rigidbody_msgs__msg__RobotCmd), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rigidbody_msgs__msg__RobotCmd__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rigidbody_msgs__msg__RobotCmd__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rigidbody_msgs__msg__RobotCmd__Sequence__fini(rigidbody_msgs__msg__RobotCmd__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rigidbody_msgs__msg__RobotCmd__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rigidbody_msgs__msg__RobotCmd__Sequence *
rigidbody_msgs__msg__RobotCmd__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RobotCmd__Sequence * array = (rigidbody_msgs__msg__RobotCmd__Sequence *)allocator.allocate(sizeof(rigidbody_msgs__msg__RobotCmd__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rigidbody_msgs__msg__RobotCmd__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rigidbody_msgs__msg__RobotCmd__Sequence__destroy(rigidbody_msgs__msg__RobotCmd__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rigidbody_msgs__msg__RobotCmd__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rigidbody_msgs__msg__RobotCmd__Sequence__are_equal(const rigidbody_msgs__msg__RobotCmd__Sequence * lhs, const rigidbody_msgs__msg__RobotCmd__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rigidbody_msgs__msg__RobotCmd__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rigidbody_msgs__msg__RobotCmd__Sequence__copy(
  const rigidbody_msgs__msg__RobotCmd__Sequence * input,
  rigidbody_msgs__msg__RobotCmd__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rigidbody_msgs__msg__RobotCmd);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rigidbody_msgs__msg__RobotCmd * data =
      (rigidbody_msgs__msg__RobotCmd *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rigidbody_msgs__msg__RobotCmd__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rigidbody_msgs__msg__RobotCmd__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rigidbody_msgs__msg__RobotCmd__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
