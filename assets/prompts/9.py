from env_utils import put_first_on_second, get_obj_names, say
from plan_utils import parse_obj_name, parse_position

# Assuming 'objects' is a list of all objects the robot can see on the table
objects = get_obj_names()

# Identify the red object and the target bowl. Let's assume there are multiple bowls and the red object is unique.
red_object_name = parse_obj_name('red object', f'objects = {objects}')
# We need to find an empty bowl or another bowl that we can move the object to.
# This might be more complex in reality, where you would check for an empty bowl or select a specific bowl based on additional criteria.
target_bowl_name = parse_obj_name('empty bowl', f'objects = {objects}')

# The position of the target bowl is obtained. We assume the function get_obj_pos returns the position where objects can be placed.
target_bowl_pos = parse_position(f'inside {target_bowl_name}')

# Move the red object to the target bowl
say(f'Moving the {red_object_name} to the {target_bowl_name}.')
put_first_on_second(red_object_name, target_bowl_pos)
