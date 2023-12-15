from env_utils import put_first_on_second, get_obj_names, say, parse_position

# First, get the names of all the boxes.
boxes = get_obj_names()  # This should return a list of box names, in this case, based on colors.

# Determine the vertical positions where the boxes should be placed.
vertical_positions = parse_position('vertical line in the center')

# Move each box to its new vertical position.
for box_name, position in zip(boxes, vertical_positions):
    say(f'Moving {box_name} to {position}.')
    put_first_on_second(box_name, position)