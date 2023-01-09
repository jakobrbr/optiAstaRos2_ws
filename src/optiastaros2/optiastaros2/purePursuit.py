import numpy as np
import time 

def proportional_velocity_controller(current_position, path, system_start_time, path_total_time, kp=1):
    current_time = np.floor(time.time())
    
    diff = np.subtract(path, current_position)
    distance_diff = np.linalg.norm(diff, axis=1)
    closest_target_index = np.argmin(distance_diff)

    # Calculate the remaining time to the target
    point_time = len(path) / (path_total_time - system_start_time)
    target_desired_index = int((current_time - system_start_time) * point_time)
    
    # print(system_start_time)
    
    error = target_desired_index - closest_target_index
    # Calculate the error as a weighted sum of the distance and remaining time
    velocity = error * kp
    if velocity < 0:
        velocity = 0
    return velocity


# ------------------------------------------------------------------

# takes a position the robot is currently and a path as input (a touple and a list of touples)
# and outputs the angle for pointing the robot at the next waypoint
def pure_pursuit(current_pos, path,lookahead_distance=5):

    # finds the index of the closest point
    diff = np.subtract(path, current_pos)
    distance_diff = np.linalg.norm(diff, axis=1)

    # finds the all the angles between the points
    angle_diff = find_angles(current_pos,path)
    target_index = np.argmin(np.multiply(distance_diff,angle_diff))
    # Apply the window to the path
    # start_index = max(0, target_index - window_size)
    # end_index = min(len(path) - 1, target_index + window_size)
    # path = path[start_index:end_index + 1]

    # Find the lookahead point on the path
    lookahead_index = target_index
    lookahead_distance_remaining = lookahead_distance

    while lookahead_distance_remaining > 0 and lookahead_index < len(path) - 1:
        diff = np.subtract(path[lookahead_index], path[lookahead_index + 1])
        lookahead_distance_remaining -= np.linalg.norm(diff)
        lookahead_index += 1

    # Make sure the lookahead index is within the bounds of the path array
    lookahead_index = min(lookahead_index, len(path) - 1)

    # Calculate the desired heading based on the position of the lookahead point
    lookahead_pos = path[lookahead_index]
    desired_heading = np.arctan2(lookahead_pos[1] - current_pos[1], lookahead_pos[0] - current_pos[0])

    return desired_heading

def pure_pursuit_turn_speed(current_angle,previous_angle):
    # To do: calculate the speed from the path point distance and the time vector for the point.

    # Calculate the change in angle
    delta_angle = np.arctan2(np.sin(previous_angle - current_angle), np.cos(previous_angle - current_angle))
    
    # Calculate a scalar to multiply with the velocity based on the change in angle and orientation. 
    # The function slows down the robot, according to the change in direction, making it take slower turns
    if np.abs(delta_angle) > np.pi/2:
        # Return a negative speed for angles above pi/2 or below 4/3pi
        velocity_scalar = mapFromTo(np.abs(delta_angle),np.pi,np.pi/2,-1,0)
        #print("velocity scalar %f" % velocity_scalar)
        return velocity_scalar
    elif np.abs(delta_angle) < np.pi/2:
        # Return the speed calculated
        velocity_scalar = mapFromTo(np.abs(delta_angle),np.pi/2,0,0,1)
        #print("velocity scalar %f" % velocity_scalar)
        return velocity_scalar
    else:
        # Return a positive speed for all other angles
        return 0

# Mapping helper function
# x = input , y = output
# [a,b] = input range
# [c,d] = output range
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def find_angles(tuple1, tuple_list):
    array1 = np.array(tuple1)
    array_list = [np.array(t) for t in tuple_list]
    angles = []
    for array2 in array_list:
        dot_product = np.dot(array1, array2)
        length1 = np.linalg.norm(array1)
        length2 = np.linalg.norm(array2)
        angle = np.arccos(dot_product / (length1 * length2))
        angles.append(angle + 1)
    return angles