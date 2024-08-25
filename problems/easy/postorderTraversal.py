from typing import List, Optional
from common import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result += self.postorderTraversal(root.left)
            result += self.postorderTraversal(root.right)
            result.append(root.val)
        return result