objects = ['red block', 'green block', 'blue block', 'red bowl', 'green bowl', 'blue bowl']
# place the blocks in bowls with non matching colors.
say('Ok - placing the blocks in bowls with non matching colors')
matches = {'red block': 'red bowl', 'green block': 'green bowl', 'blue block': 'blue bowl'}
for first, second in matches.items():
    put_first_on_second(first, get_obj_pos(second))