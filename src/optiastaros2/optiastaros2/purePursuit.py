import numpy as np

class PID_controller:
    def __init__(self,kp,ki,kd, kt):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.kt = kt # Time catch-up gain
        self.previous_error = 0
        self.integral = 0

    def update(self, current_position, target_position, current_time, target_time=1,update_time=0.1,breakforce = 0.1):

            error = np.linalg.norm(np.subtract(target_position,current_position)) # Calculate the error
            elapsed_time = current_time - target_time # Calculate the elapsed time

            p_position = self.kp * error # Proportional term

            self.integral += error * update_time
            i_position = self.ki * self.integral # Integral term

            derivative = (error - self.previous_error) / update_time
            d_position = self.kd * derivative # Derivative term

            t = self.kt * elapsed_time # Time elapsed term

            self.previous_error = error # Save the error for the next iteration
            
            desired_velocity = (p_position + i_position + d_position + t) # sum the gains to obtain the desired velocity
            
            if error < 0:
                desired_velocity *= breakforce
            if error == 0:
                desired_velocity = 0
            return desired_velocity

# Use inside the main loop like like so :
# Generate outout:
#   output = controller.update(current_position, target_position, current_time, target_time, dt)
# Check if target_pos has been reached:
#  if abs(current_position - target_position) < 0.01: Break
        
def pure_pursuit(current_pos, path,lookahead_distance=1):
    # Find the closest point on the path to the current position
    diff = np.subtract(path, current_pos)
    distances = np.linalg.norm(diff, axis=1)
    target_index = np.argmin(distances)

    print("debug, inside pure pursuit")

    # Find the lookahead point on the path
    lookahead_index = target_index
    lookahead_distance_remaining = lookahead_distance
    while lookahead_distance_remaining > 0 and lookahead_index < len(path) - 1:
        diff = np.subtract(path[lookahead_index], path[lookahead_index + 1])
        lookahead_distance_remaining -= np.linalg.norm(diff)
        lookahead_index += 1

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
        print("velocity scalar %f" % velocity_scalar)
        return velocity_scalar
    elif np.abs(delta_angle) < np.pi/2:
        # Return the speed calculated
        velocity_scalar = mapFromTo(np.abs(delta_angle),np.pi/2,0,0,1)
        print("velocity scalar %f" % velocity_scalar)
        return velocity_scalar
    else:
        # Return a positive speed for all other angles
        return 0


# Legacy function, no longer used
def waypoint_change(current_position,target_position, threshold):
    #calculate the distance from the current postition, to the target postition
    direction = target_position - current_position
    distance = np.linalg.norm(direction)
    # If we are close enough to the waypoint, increment the index
    if threshold > distance:
        return 1
    else:
        return 0

# Mapping helper function
# x = input , y = output
# [a,b] = input range
# [c,d] = output range
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y