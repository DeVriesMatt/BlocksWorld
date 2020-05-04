from Blocksworld import *


def breadth_first_search(starting_state):
    print("Beginning Breadth-First Tree Search")
    total_nodes_expanded = 0
    # Initialising the fringe
    fringe = [generate_child_node(starting_state, None, None, 0)]
    # We perform the search until the fringe is empty or the goal state is found
    while len(fringe) != 0:
        # We expand the first node in the fringe
        node_to_expand = fringe.pop(0)
        # Check if this node is in the goal state before expanding
        if goal_check(node_to_expand.state) is True:
            # Solution variables
            path = []
            action = []
            tmp = node_to_expand
            # We go from the goal to the beginning while keeping track of the path and actions and the state
            while True:
                action.insert(0, tmp.node_action)
                path.insert(0, tmp.state)
                if tmp.depth == 1:
                    break
                # Go up a level
                tmp = tmp.parent

            return path, total_nodes_expanded

        fringe.extend(expand(node_to_expand))
        total_nodes_expanded += 1


def depth_first_search(starting_state):
    print("Beginning Depth-First Search")
    total_nodes_expanded = 0
    # Initialising the fringe
    fringe = [generate_child_node(starting_state, None, None, 0)]
    # We perform the search until the fringe is empty or the goal state is found
    while len(fringe) != 0:
        node_to_expand = fringe.pop(0)
        # Check if this node is in the goal state before expanding
        if goal_check(node_to_expand.state) is True:
            # Solution variables
            path = []
            action = []
            tmp = node_to_expand
            # We go from the goal to the beginning while keeping track of the path and actions and the state
            while True:
                action.insert(0, tmp.node_action)
                path.insert(0, tmp.state)
                if tmp.depth <= 1:
                    break
                # Go up a level
                tmp = tmp.parent

            return path, total_nodes_expanded

        expanded_nodes = expand_node_randomly(node_to_expand)
        expanded_nodes.extend(fringe)
        # Change from BFS to DFS
        fringe = expanded_nodes
        total_nodes_expanded += 1


def depth_limited_search(starting_state, limit):
    total_nodes_expanded = 0
    fringe = [generate_child_node(starting_state, None, None, 0)]

    while len(fringe) != 0:
        node_to_expand = fringe.pop(0)
        if goal_check(node_to_expand.state) is True:
            path = []
            action = []
            tmp = node_to_expand
            while True:
                action.insert(0, tmp.node_action)
                path.insert(0, tmp.state)
                if tmp.depth <= 1:
                    break
                # Go up a level
                tmp = tmp.parent

            return path, total_nodes_expanded

        # Depth limited part to check if the depth limit is reached
        if node_to_expand.depth <= limit:
            # Continue same as depth first search
            expanded_nodes = expand_node_randomly(node_to_expand)
            expanded_nodes.extend(fringe)
            fringe = expanded_nodes
            total_nodes_expanded += 1


def iterative_deepening_search(starting_state):
    print("Beginning Iterative Deepening Search")
    for j in range(100):
        print("Depth = {0}".format(j))
        result = depth_limited_search(starting_state, j)
        if result is not None:
            return result

    print("End")


def calculate_hamming(initial_state):  # The number of blocks in the wrong position
    distance = 0

    if initial_state is None:
        return 10000

    if initial_state[5] != 2:
        distance += 1
    if initial_state[9] != 3:
        distance += 1
    if initial_state[13] != 4:
        distance += 1

    return distance


def calculate_manhattan(initial_state):
    # We need to account for a None state
    if initial_state is None:
        return 10000
    # Initialise distance
    distance = 0
    # For our problem, this is 16 but we may change the grid-size for testing
    length = len(initial_state)
    # The problem set up is such that the state is in 1 dimension
    # for this reason, calculating the distance can be done through a series of
    # if statements
    # We are only concerned with the positions of the letter blocks,
    # not the agent.
    for i in range(length):
        if initial_state[i] is 2:
            if i in range(0, 4):
                distance = distance + abs(i-1) + 1
            if i in range(4, 8):
                distance = distance + abs(i-5)
            if i in range(8, 12):
                distance = distance + abs(i-9) + 1
            if i in range(12, 16):
                distance = distance + abs(i-13) + 2

        if initial_state[i] is 3:
            if i in range(0, 4):
                distance = distance + abs(i-1) + 2
            if i in range(4, 8):
                distance = distance + abs(i-5) + 1
            if i in range(8, 12):
                distance = distance + abs(i-9)
            if i in range(12, 16):
                distance = distance + abs(i-13) + 1

        if initial_state[i] is 4:
            if i in range(0, 4):
                distance = distance + abs(i-1) + 3
            if i in range(4, 8):
                distance = distance + abs(i-5) + 2
            if i in range(8, 12):
                distance = distance + abs(i-9) + 1
            if i in range(12, 16):
                distance = distance + abs(i-13)

    return distance


def a_star(starting_state):
    print("Beginning A* Heuristic Search Using Manhattan Distance")
    total_nodes_expanded = 0
    # Initialise the fringe with the start state
    fringe = [generate_child_node(starting_state, None, None, 0)]
    while len(fringe) != 0:
        # After the first node is expanded, we need to sort the nodes to expand
        # in order of their evaluation values
        if total_nodes_expanded > 1:
            fringe.sort(key=lambda x: x.evaluation)
        # Continue by expanding next node in the sorted fringe
        node_to_expand = fringe.pop(0)
        # Perform the goal test
        if goal_check(node_to_expand.state) is True:
            path = []
            action = []
            tmp = node_to_expand
            while True:
                action.insert(0, tmp.node_action)
                path.insert(0, tmp.state)
                if tmp.depth <= 1:
                    break
                # Go up a level
                tmp = tmp.parent

            return path, total_nodes_expanded

        fringe.extend(expand(node_to_expand))
        total_nodes_expanded += 1


if __name__ == "__main__":
    starting = [1, 1, 1, 1,
                1, 1, 1, 1,
                1, 1, 1, 1,
                2, 3, 4, 0]
    breadth_first_search(starting)
    depth_first_search(starting)
    iterative_deepening_search(starting)
    a_star(starting)