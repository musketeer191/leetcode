"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
# successor of a node is the node with the smallest key greater than node.val
# BST: left subtree of a node contains smaller values and right subtree contains larger values.
# if a node has right subtree then the left most leaf node of the right subtree will be its successor
# else: node has no right subtree, then to search for larger values, need to go up, two cases then happen:
# i) if node is the left child of its parent, then its parent will be its successor (larger and smallest of such, why?)
# ii) if node is the right child of its parent, then its parent is smaller than it. In other words, if, starting from the node, we keep going left then we only meet values smaller than it, only when we start turn right (if any), then we meet the first value larger than it, and this will be its successor
# All cases covered (tmr implement)
