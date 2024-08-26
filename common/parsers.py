import json
from common import TreeNode, Node

def json_parser(input_data):
    return json.loads(input_data)

def tree_parser(input_data):
    values = json.loads(input_data)
    return build_tree(values)

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        current = queue.pop(0)

        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def nary_tree_parser(input_data):
    values = json.loads(input_data)
    return build_nary_tree(values)

def build_nary_tree(values):
    if not values:
        return None

    root = Node(values[0])
    queue = [root]
    i = 2  

    while queue and i < len(values):
        current = queue.pop(0)
        while i < len(values) and values[i] is not None:
            child = Node(values[i])
            current.children.append(child)
            queue.append(child)
            i += 1
        i += 1  

    return root