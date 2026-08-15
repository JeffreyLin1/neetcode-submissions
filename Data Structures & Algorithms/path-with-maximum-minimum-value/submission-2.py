import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        heap = [(-grid[0][0], 0, 0)]

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [
            [float("-inf") for _ in range(cols)]
            for _ in range(rows)
        ]

        dist[0][0] = grid[0][0]

        while heap:
            curr = heapq.heappop(heap)

            cost = -curr[0]
            r, c = curr[1], curr[2]

            for dr, dc in d:
                nr, nc = r + dr, c + dc

                if (
                    nr >= 0 and
                    nc >= 0 and
                    nr < rows and
                    nc < cols
                ):
                    newScore = min(cost, grid[nr][nc])

                    if newScore > dist[nr][nc]:
                        dist[nr][nc] = newScore
                        heapq.heappush(
                            heap,
                            (-newScore, nr, nc)
                        )

        return dist[rows - 1][cols - 1]