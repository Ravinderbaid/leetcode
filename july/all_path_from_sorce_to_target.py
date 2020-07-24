from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        q = deque([(0, [0])])
        paths = []

        while q:
            node, path = q.popleft()
            if node == n:
                paths.append(path)
            else:
                for child in graph[node]:
                    q.append((child, path + [child]))
        return paths
