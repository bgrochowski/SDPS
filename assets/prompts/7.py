import numpy as np
from env_utils import put_first_on_second, get_obj_pos, get_obj_names, say, parse_position

# First, get the names of all the blocks on the table.
objects = get_obj_names()  # This should return a list of object names, including the blocks.

# Now we need to place the blocks in diagonal positions. We can define these manually or calculate them.
# Assuming we have a function that can calculate equidistant points in a diagonal in our environment:
diagonal_positions = parse_position('diagonal line from top left to bottom right')

# Next, we assign each block to a position on the diagonal.
for block_name, position in zip(objects, diagonal_positions):
    say(f'Moving {block_name} to position {position}.')
    put_first_on_second(block_name, position)