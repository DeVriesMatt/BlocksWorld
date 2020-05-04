from Node import Node
from Actions import *
import random


# Checks if the current state is the goal
def goal_check(state):
    if state[5] == 2 and state[9] == 3 and state[13] == 4:
        return True
    else:
        return False


# Generates a new node
def generate_child_node(state, parent, action, depth):
    return Node(state, parent, action, depth)


# Expands a node and returns a list of the possible actions or successor nodes
def expand(node):
    successor_nodes = [generate_child_node(move_up(node.state), node, "Move Up", node.depth + 1),
                       generate_child_node(move_down(node.state), node, "Move Down", node.depth + 1),
                       generate_child_node(move_left(node.state), node, "Move Left", node.depth + 1),
                       generate_child_node(move_right(node.state), node, "Move Right", node.depth + 1)
                       ]
    # We need to find out which successor nodes are possible
    successor_nodes = [node for node in successor_nodes if node.state is not None]
    return successor_nodes


# For depth first search, we need to expand nodes randomly
def expand_node_randomly(node):
    nodes_ex = expand(node)
    random.shuffle(nodes_ex)
    return nodes_ex


def expand_graph(node, visited):
    successor_nodes = [generate_child_node(move_up(node.state), node, "Move Up", node.depth + 1),
                       generate_child_node(move_down(node.state), node, "Move Down", node.depth + 1),
                       generate_child_node(move_left(node.state), node, "Move Left", node.depth + 1),
                       generate_child_node(move_right(node.state), node, "Move Right", node.depth + 1)
                       ]
    # We need to find out which successor nodes are possible
    successor_nodes = [node for node in successor_nodes if node.state is not None]
    # same principle applied to previously visited states for graph search
    successor_nodes = [node for node in successor_nodes if node.state not in visited]
    return successor_nodes


# For depth first search, we need to expand nodes randomly
def expand_node_randomly_graph(node, visited):
    nodes_ex = expand_graph(node, visited)
    random.shuffle(nodes_ex)
    return nodes_ex


def display(state):
    print("-----------------")
    print("| {0} | {1} | {2} | {3} |".format(state[0], state[1], state[2], state[3]))
    print("-----------------")
    print("| {0} | {1} | {2} | {3} |".format(state[4], state[5], state[6], state[7]))
    print("-----------------")
    print("| {0} | {1} | {2} | {3} |".format(state[8], state[9], state[10], state[11]))
    print("-----------------")
    print("| {0} | {1} | {2} | {3} |".format(state[12], state[13], state[14], state[15]))
    print("-----------------")
