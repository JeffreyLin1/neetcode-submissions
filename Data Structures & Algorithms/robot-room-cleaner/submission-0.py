# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = [
            (-1, 0), # north
            (0, 1), # east
            (1, 0), # south
            (0, -1) # west
        ]
        v = set()
        def recall():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        def dfs(r, c, d):
            robot.clean()
            v.add((r, c))
            for i in range(4):
                nd = (i + d) % 4
                dr, dc = dirs[nd]
                if (r + dr, c + dc) not in v and robot.move():
                    dfs(r + dr, c + dc, nd)
                    recall()
                robot.turnRight()
        
        dfs(0, 0, 0)






















        