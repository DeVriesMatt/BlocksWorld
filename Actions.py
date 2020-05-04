# A file of functions which describe what the agent can do
def move_up(state):
    new_state = state[:]
    position = new_state.index(0)
    upper = [0, 1, 2, 3]
    # Check if possible to move up
    if position not in upper:
        # move agent up
        # do this by swapping the tiles
        tmp = new_state[position - 4]
        new_state[position - 4] = new_state[position]
        new_state[position] = tmp
        return new_state
    else:
        return None


def move_down(state):
    new_state = state[:]
    position = new_state.index(0)
    lower = [12, 13, 14, 15]
    # Check if possible to move down
    if position not in lower:
        # Move agent down
        # Do this by swapping the tiles
        tmp = new_state[position + 4]
        new_state[position + 4] = new_state[position]
        new_state[position] = tmp
        return new_state
    else:
        return None


def move_left(state):
    new_state = state[:]
    position = new_state.index(0)
    lefter = [0, 4, 8, 12]
    # Check if possible to move left
    if position not in lefter:
        # Move agent left
        # Do this by swapping tiles
        tmp = new_state[position - 1]
        new_state[position - 1] = new_state[position]
        new_state[position] = tmp
        return new_state
    else:
        return None


def move_right(state):
    new_state = state[:]
    position = new_state.index(0)
    righter = [3, 7, 11, 15]
    # Check if possible to move left
    if position not in righter:
        # Move agent right
        # Do this by swapping tiles
        tmp = new_state[position + 1]
        new_state[position + 1] = new_state[position]
        new_state[position] = tmp
        return new_state
    else:
        return None
