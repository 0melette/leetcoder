
from typing import List
from common import Node

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        
        self.traversePostorder(root, result)
        return result
    
    def traversePostorder(self, currentNode: 'Node', postorderList: List[int]) -> None:
        if not currentNode:
            return
        
        for childNode in currentNode.children:
            self.traversePostorder(childNode, postorderList)
            
        postorderList.append(currentNode.val)