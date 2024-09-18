from typing import List, Optional
from common import ListNode

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = []
        for _ in range(m):
            row = [-1] * n 
            matrix.append(row)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0 
        direction_index = 0 

        curr = head
 
        while m > 0 and n > 0 and curr:
            if direction_index % 2 == 0:
                steps = n
            else:
                steps = m
            
            for _ in range(steps):
                if curr:
                    matrix[x][y] = curr.val
                    curr = curr.next
                else:
                    break
                
                dx, dy = directions[direction_index]
                x += dx
                y += dy
            
            if direction_index % 2 == 0:
                m -= 1
            else:
                n -= 1
            
            if direction_index == 0:
                x += 1
                y -= 1
            elif direction_index == 1:
                x -= 1
                y -= 1
            elif direction_index == 2:
                x -= 1
                y += 1
            elif direction_index == 3:
                x += 1
                y += 1
            
            direction_index = (direction_index + 1) % 4
        
        return matrix