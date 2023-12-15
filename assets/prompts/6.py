from env_utils import stack_objects_in_order, get_obj_names, say
from plan_utils import parse_obj_name, parse_position

# Get the current object names, which should include our boxes
objects = get_obj_names()

# Parse the object names to identify the boxes specifically
box_names = parse_obj_name('box', f'objects = {objects}')

# Assuming parse_position can generate the correct positions for a vertical pyramid stack
pyramid_base_pos = parse_position('center of the table')
pyramid_positions = transform_shape_pts('pyramid', base_pos=pyramid_base_pos, num_levels=len(box_names))

# We will stack the boxes in order with the largest base at the bottom and the smallest at the top
order_bottom_to_top = sorted(box_names, key=lambda x: get_obj_pos(x)[0])  # This assumes sorting by size or some other criteria

stack_objects_in_order(object_names=order_bottom_to_top, positions=pyramid_positions)