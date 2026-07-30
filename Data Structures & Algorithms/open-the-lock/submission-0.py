from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        matrix of all possible combinations, if cells are adjacent that means they 
        can reach eachother with only one turn.
        run BFS from 0000 (top left) to the target combination, invalid path if passing through 
        a deadend (use a set)
        '''
        visited = set()
        q = deque()
        for s in deadends:
            visited.add(s)
        if '0000' in visited:
            return -1
        if target == '0000':
            return 0
        q.append('0000')
        turns = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(4):
                    new2 = curr[:i] + str((int(curr[i]) - 1)%10) + curr[i+1:]
                    new = curr[:i] + str((int(curr[i]) + 1)%10) + curr[i+1:]
                    if new == target or new2 == target:
                        return turns + 1
                    if new not in visited:
                        visited.add(new)
                        q.append(str(new))
                    if new2 not in visited:
                        visited.add(new2)
                        q.append(str(new2))
            turns += 1
        return -1
                
            


        


