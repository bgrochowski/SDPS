from env_utils import draw
from plan_utils import parse_shape_pts, transform_shape_pts

# Define points for a star shape around the center
star_points = parse_shape_pts('a star with 5 points around the middle')

# Assuming we have the whiteboard coordinates system set up,
# we can draw the star pattern directly if the function supports complex shapes.
draw(star_points)

# If the draw function requires one point at a time, we may need to loop through the points
for point in star_points:
    draw([point])  # Draw each point of the star