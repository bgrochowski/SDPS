import numpy as np
from env_utils import draw
from plan_utils import parse_shape_pts, transform_shape_pts

# Function to draw a letter by parsing shape points and drawing them
def draw_letter(letter, offset):
    # Parse the shape points for the letter
    letter_shape_pts = parse_shape_pts(f'a letter {letter} with size suitable for whiteboard')
    # Transform the shape points by offsetting to position the letter correctly
    letter_shape_pts_transformed = transform_shape_pts(f'translate it by {offset[0]}x and {offset[1]}y', shape_pts=letter_shape_pts)
    # Draw the transformed letter on the whiteboard
    draw(letter_shape_pts_transformed)

# Define offsets for each letter in "robot"
# These would be calculated based on the size of each letter and desired spacing
offsets = [
    (0, 0),   # Offset for 'R'
    (1, 0),   # Offset for 'o'
    (2, 0),   # Offset for 'b'
    (3, 0),   # Offset for 'o'
    (4, 0)    # Offset for 't'
]

# Draw each letter on the whiteboard
letters = ['R', 'o', 'b', 'o', 't']
for i, letter in enumerate(letters):
    draw_letter(letter, offsets[i])