from robot_control_utils import identify_object, plan_path, execute_movement, grasp_object, release_object

# Step 1: Identify the red book's position
red_book_position = identify_object('red book')

# Step 2: Plan the path to the red book
path_to_book = plan_path(current_position, red_book_position)

# Step 3: Move to the red book and grasp it
execute_movement(path_to_book)
grasp_object(red_book_position)

# Step 4: Plan the path to the right shelf
path_to_right_shelf = plan_path(red_book_position, right_shelf_position)

# Step 5: Move to the right shelf and release the book
execute_movement(path_to_right_shelf)
release_object(right_shelf_position)