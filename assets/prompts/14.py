from env_utils import put_first_on_second, get_obj_pos, get_obj_names, say
from plan_utils import parse_obj_name, parse_position

# Assume 'objects' is the list of all objects the robot can recognize on the table
objects = get_obj_names()

# Identify objects by size using a sorting function - this is hypothetical and assumes that
# the robot has a way to determine the size of an object, perhaps through a vision system or predefined knowledge
objects_sorted_by_size = sorted(objects, key=lambda x: parse_obj_name(f'size of {x}', f'objects = {objects}'))

# Positions will be determined based on sorted object sizes, assuming parse_position can find suitable places on the table
sorted_positions = [parse_position(f'position {i} in sorted area') for i, _ in enumerate(objects_sorted_by_size)]

# Move each object to its new position based on size
for obj_name, new_pos in zip(objects_sorted_by_size, sorted_positions):
    say(f'Moving {obj_name} to position {new_pos}.')
    put_first_on_second(obj_name, new_pos)

say('Sorting complete.')