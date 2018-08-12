# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = False
        if root == None:
            return False
        if sum == root.val and root.left == None and root.right == None:
            return True

        if root.left != None:
            result = result or self.hasPathSum(root.left, sum - root.val)

        if root.right != None:
            result = result or self.hasPathSum(root.right, sum - root.val)

        return result


if __name__ == "__main__":
    print("Path Sum")
    t = TreeNode(1)
    t.left = TreeNode(2)
    s = Solution()
    print (s.hasPathSum(t, 3))
