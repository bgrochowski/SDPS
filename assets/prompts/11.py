from perception_utils import get_robot_pos_and_angle, is_path_visible, get_path_points
from action_utils import follow_traj, say

# Assuming the robot has a camera or sensor that can detect the path and its points
if is_path_visible('path on the ground'):
    say('Path detected, starting to follow.')
    # Get the current position and orientation of the robot
    robot_pos, robot_angle = get_robot_pos_and_angle()
    
    # Get the points that make up the path on the ground
    path_points = get_path_points('path on the ground')
    
    # Command the robot to follow the trajectory defined by the path points
    follow_traj(path_points, speed=0.5)  # The speed can be adjusted as necessary

    say('Path following complete.')
else:
    say('No visible path detected on the ground.')