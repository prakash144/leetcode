class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
       
        # DFS : O(V + E), O(V)
        V = len(graph)
        color = [0] * V  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if color[node] == 1:
                return False # cycle detected
            if color[node] == 2:
                return True # already known to be safe

            color[node] = 1  # mark as visiting
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False 
            color[node] = 2 # mark as safe

            return True

        result = []
        for i in range(V):
            if dfs(i):
                result.append(i) 

        return result