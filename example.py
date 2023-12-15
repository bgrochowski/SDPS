move_block_to_target(color, start_position, end_position):    # Detect block with the specified color
    block = detect_block_with_color(color)

    # Check if the block is not already at the target location
    if block.position != end_position:
        # Pick up the block using color as reference
        robot.pick(block)

        # Move the block to the target location
        # (The curve path is simplified to a direct move command for the sake of example)
        robot.move_to(end_position)

        # Drop the block at the target location
        robot.drop()
    else:
        print("Block is already at the target position.")

# Invoke the function with the color 'red' and the specified start and end positions
move_block_to_target('red', start_position, end_position)