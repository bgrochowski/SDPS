import numpy as np
from env_utils import put_first_on_second, get_obj_pos, get_obj_names, say, parse_position

# Assuming 'objects' is a list of all the objects on the table
objects = get_obj_names()  # This should include the orange block
orange_block_name = parse_obj_name('orange block', f'objects = {objects}')
lower_right_corner_pos = parse_position('lower right corner')

# Move the orange block to the lower right corner
say(f'Moving the {orange_block_name} to the lower right corner')
put_first_on_second(orange_block_name, lower_right_corner_pos)