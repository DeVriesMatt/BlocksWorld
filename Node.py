from TreeSearchAlgorithms import calculate_manhattan, calculate_hamming


class Node:
    def __init__(self, state, parent, node_action, depth):
        # the state in the state space to which the node corresponds
        self.state = state
        # the node in the search tree that generated this node
        self.parent = parent
        # the action that was applied to the parent to generate the node
        self.node_action = node_action
        # the depth of this node
        self.depth = depth
        # the cost, traditionally denoted by f(n), of the path from the initial state
        # to the node, as indicated by the parent pointers
        self.cost = hn(self.state, "Manhattan")

        self.evaluation = hn(self.state, "Manhattan") + self.depth


def hn(state, heuristic_function):
    if heuristic_function == "Manhattan":
        return calculate_manhattan(state)
    if heuristic_function == "Hamming":
        return calculate_hamming(state)
    else:
        print("Please choose an appropriate heuristic from: \n"
              " - Manhattan, \n"
              "- Hamming,\n")
