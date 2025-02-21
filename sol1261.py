# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s = set()
        self.build(root, 0)

    def build(self, root: Optional[TreeNode], i: int):
        if not root:
            return

        self.s.add(i)
        self.build(root.left, 2 * i + 1) 
        self.build(root.right, 2 * i + 2)
        

    def find(self, target: int) -> bool:
        return target in self.s
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)