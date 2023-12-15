import numpy as np
from env_utils import put_first_on_second, get_obj_pos, get_obj_names, say
from plan_utils import parse_obj_name, parse_position

# Assuming 'objects' contains the names of all objects on the table
objects = get_obj_names()

# Identify the apple and the target bowl. We assume the apple is the only red object.
apple_name = parse_obj_name('red object', f'objects = {objects}')
target_bowl_name = parse_obj_name('empty bowl', f'objects = {objects}')

# Get the position of the target bowl to place the apple in
target_bowl_pos = get_obj_pos(target_bowl_name)

# Move the apple to the target bowl
say(f'Moving the {apple_name} to the {target_bowl_name}.')
put_first_on_second(apple_name, target_bowl_pos)