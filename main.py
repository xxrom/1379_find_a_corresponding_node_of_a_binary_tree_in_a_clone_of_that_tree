# Definition for a binary tree node.
class Node:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def findInTree(self, currentNode: Node) -> Node:
    if currentNode.val == self.target:
      return currentNode

    val = self.findInTree(
        currentNode.left) if currentNode.left != None else None
    if val != None:
      return val

    val = self.findInTree(
        currentNode.right) if currentNode.right != None else None
    if val != None:
      return val

    return None

  def getTargetCopy(self, original: Node, cloned: Node, target: Node) -> Node:
    if (target == None or original == None or cloned == None or
        target.val == None):
      return None

    self.target = target.val

    return self.findInTree(cloned)


my = Solution()
original = Node(7, Node(4), Node(3, Node(6), Node(19)))
clone = Node(7, Node(4), Node(3, Node(6), Node(19)))

ans = my.getTargetCopy(original, clone, Node(3))
print("ans", ans)

# Runtime: 644 ms, faster than 95.41% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 23.2 MB, less than 100.00% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.