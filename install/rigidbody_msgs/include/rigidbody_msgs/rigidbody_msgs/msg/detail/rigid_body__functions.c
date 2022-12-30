// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rigidbody_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice
#include "rigidbody_msgs/msg/detail/rigid_body__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
// Member `rot`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
rigidbody_msgs__msg__RigidBody__init(rigidbody_msgs__msg__RigidBody * msg)
{
  if (!msg) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__init(&msg->rigid_body_name)) {
    rigidbody_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Point__init(&msg->pose)) {
    rigidbody_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  // rot
  if (!geometry_msgs__msg__Point__init(&msg->rot)) {
    rigidbody_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  return true;
}

void
rigidbody_msgs__msg__RigidBody__fini(rigidbody_msgs__msg__RigidBody * msg)
{
  if (!msg) {
    return;
  }
  // rigid_body_name
  rosidl_runtime_c__String__fini(&msg->rigid_body_name);
  // pose
  geometry_msgs__msg__Point__fini(&msg->pose);
  // rot
  geometry_msgs__msg__Point__fini(&msg->rot);
}

bool
rigidbody_msgs__msg__RigidBody__are_equal(const rigidbody_msgs__msg__RigidBody * lhs, const rigidbody_msgs__msg__RigidBody * rhs)
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
  // pose
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  // rot
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->rot), &(rhs->rot)))
  {
    return false;
  }
  return true;
}

bool
rigidbody_msgs__msg__RigidBody__copy(
  const rigidbody_msgs__msg__RigidBody * input,
  rigidbody_msgs__msg__RigidBody * output)
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
  // pose
  if (!geometry_msgs__msg__Point__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  // rot
  if (!geometry_msgs__msg__Point__copy(
      &(input->rot), &(output->rot)))
  {
    return false;
  }
  return true;
}

rigidbody_msgs__msg__RigidBody *
rigidbody_msgs__msg__RigidBody__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RigidBody * msg = (rigidbody_msgs__msg__RigidBody *)allocator.allocate(sizeof(rigidbody_msgs__msg__RigidBody), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rigidbody_msgs__msg__RigidBody));
  bool success = rigidbody_msgs__msg__RigidBody__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rigidbody_msgs__msg__RigidBody__destroy(rigidbody_msgs__msg__RigidBody * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rigidbody_msgs__msg__RigidBody__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rigidbody_msgs__msg__RigidBody__Sequence__init(rigidbody_msgs__msg__RigidBody__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RigidBody * data = NULL;

  if (size) {
    data = (rigidbody_msgs__msg__RigidBody *)allocator.zero_allocate(size, sizeof(rigidbody_msgs__msg__RigidBody), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rigidbody_msgs__msg__RigidBody__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rigidbody_msgs__msg__RigidBody__fini(&data[i - 1]);
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
rigidbody_msgs__msg__RigidBody__Sequence__fini(rigidbody_msgs__msg__RigidBody__Sequence * array)
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
      rigidbody_msgs__msg__RigidBody__fini(&array->data[i]);
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

rigidbody_msgs__msg__RigidBody__Sequence *
rigidbody_msgs__msg__RigidBody__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rigidbody_msgs__msg__RigidBody__Sequence * array = (rigidbody_msgs__msg__RigidBody__Sequence *)allocator.allocate(sizeof(rigidbody_msgs__msg__RigidBody__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rigidbody_msgs__msg__RigidBody__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rigidbody_msgs__msg__RigidBody__Sequence__destroy(rigidbody_msgs__msg__RigidBody__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rigidbody_msgs__msg__RigidBody__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rigidbody_msgs__msg__RigidBody__Sequence__are_equal(const rigidbody_msgs__msg__RigidBody__Sequence * lhs, const rigidbody_msgs__msg__RigidBody__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rigidbody_msgs__msg__RigidBody__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rigidbody_msgs__msg__RigidBody__Sequence__copy(
  const rigidbody_msgs__msg__RigidBody__Sequence * input,
  rigidbody_msgs__msg__RigidBody__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rigidbody_msgs__msg__RigidBody);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rigidbody_msgs__msg__RigidBody * data =
      (rigidbody_msgs__msg__RigidBody *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rigidbody_msgs__msg__RigidBody__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rigidbody_msgs__msg__RigidBody__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rigidbody_msgs__msg__RigidBody__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
