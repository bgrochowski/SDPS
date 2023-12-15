say('ok - going in a 1.5m square around the stool as many times as needed, checking each step if there is a coca cola can, only stopping when I see it')
traj = parse_position('a 1.5m square around the stool with 4 points')
while True:
    for pos in traj:
        goto_pos(pos)
        if is_obj_visible('coca cola can', loc='stool'):
            break
    if is_obj_visible('coca cola can', loc='stool'):
        break
say('I see the coca cola can')