from Blocksworld import *


def breadth_first_graph(starting_state):
    print("Beginning Breadth-First Graph Search")
    # We now need to keep a list of the states which have been visited
    visited = []
    # We continue similarly as before in tree search
    total_nodes_expanded = 0
    # Initialising the fringe
    fringe = [generate_child_node(starting_state, None, None, 0)]
    # We perform the search until the fringe is empty or the goal state is found
    while len(fringe) != 0:
        # We expand the first node in the fringe
        node_to_expand = fringe.pop(0)

        # We append the list of visited states with this expanded nodes state
        visited.append(node_to_expand.state)

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

        fringe.extend(expand_graph(node_to_expand, visited))
        total_nodes_expanded += 1


def depth_first_graph(starting_state):
    print("Beginning Depth-First Graph Search")
    # We now need to keep a list of the states which have been visited
    visited = []
    total_nodes_expanded = 0
    # Initialising the fringe
    fringe = [generate_child_node(starting_state, None, None, 0)]
    # We perform the search until the fringe is empty or the goal state is found
    while len(fringe) != 0:
        node_to_expand = fringe.pop(0)
        visited.append(node_to_expand.state)
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

        expanded_nodes = expand_node_randomly_graph(node_to_expand, visited)
        expanded_nodes.extend(fringe)
        fringe = expanded_nodes
        total_nodes_expanded += 1


def depth_limited_graph(starting_state, limit):
    visited = []
    total_nodes_expanded = 0
    fringe = [generate_child_node(starting_state, None, None, 0)]

    while len(fringe) != 0:
        node_to_expand = fringe.pop(0)
        visited.append(node_to_expand.state)
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
            expanded_nodes = expand_graph(node_to_expand, visited)
            expanded_nodes.extend(fringe)
            fringe = expanded_nodes
            total_nodes_expanded += 1


def iterative_deepening_graph(starting_state):
    print("Beginning Iterative Deepening Graph Search")
    for j in range(100):
        print("Depth = {0}".format(j))
        result = depth_limited_graph(starting_state, j)
        print(result)
        if result is not None:
            return result


def a_star_graph(starting_state):
    print("Beginning A* Heuristic Graph Search")
    visited = []
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
        visited.append(node_to_expand.state)
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

        fringe.extend(expand_graph(node_to_expand, visited))
        total_nodes_expanded += 1


def recursive_best_first_graph(starting_state, f_limit):
    visited = []
    total_nodes_expanded = 0
    # Initialise the fringe with the start state
    state_copy = starting_state
    fringe = [generate_child_node(starting_state, None, None, 0)]
    while len(fringe) != 0:
        # Continue by expanding next node in the sorted fringe
        node_to_expand = fringe.pop(0)
        visited.append(node_to_expand.state)
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

        successors = [generate_child_node(move_up(node_to_expand.state), node_to_expand, "Move Up", node_to_expand.depth + 1),
                           generate_child_node(move_down(node_to_expand.state), node_to_expand, "Move Down", node_to_expand.depth + 1),
                           generate_child_node(move_left(node_to_expand.state), node_to_expand, "Move Left", node_to_expand.depth + 1),
                           generate_child_node(move_right(node_to_expand.state), node_to_expand, "Move Right", node_to_expand.depth + 1)
                           ]
        # We need to find out which successor nodes are possible
        successors = [node for node in successors if node.state is not None]
        # Check if successors is empty and if so return failure
        if not successors:
            return None
        for s in successors:
            s.evaluation = max(s.depth + s.cost, node_to_expand.evaluation)
        while True:
            if successors.sort(key=lambda x: x.evaluation) is None:
                return None
            else:
                best = successors.sort(key=lambda x: x.evaluation).pop(0)
                if best.evaluaion > f_limit:
                    return False
                alternative = successors.pop(1).evaluation
                result, best.evaluation = recursive_best_first_graph(best.state, alternative)
                if result is not None:
                    return result


if __name__ == "__main__":
    starting = [1, 1, 1, 1,
                1, 1, 1, 1,
                1, 1, 1, 1,
                2, 3, 4, 0]
    breadth_first_graph(starting)
    depth_first_graph(starting)
    iterative_deepening_graph(starting)
    a_star_graph(starting)
