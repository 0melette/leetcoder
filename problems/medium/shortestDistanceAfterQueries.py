from typing import List
from collections import deque

class Solution:
    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        visited = [False] * n
        node_queue = deque()

        node_queue.append(0)
        visited[0] = True

        current_layer_node_count = 1
        next_layer_node_count = 0
        layers_explored = 0

        while node_queue:
            for _ in range(current_layer_node_count):
                current_node = node_queue.popleft()

                if current_node == n - 1:
                    return layers_explored

                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    node_queue.append(neighbor)
                    next_layer_node_count += 1
                    visited[neighbor] = True

            current_layer_node_count = next_layer_node_count
            next_layer_node_count = 0
            layers_explored += 1

        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        for i in range(n - 1):
            adj_list[i].append(i + 1)

        for road in queries:
            u, v = road
            adj_list[u].append(v)
            answer.append(self.bfs(n, adj_list))

        return answer

