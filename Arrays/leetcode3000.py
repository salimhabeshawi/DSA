import math
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        maxd = 0
        maxa = 0
        for i, j in enumerate(dimensions):
            area = dimensions[i][0] * dimensions[i][1]
            diagonal = math.sqrt((dimensions[i][0])**2 + (dimensions[i][1])**2)
            if diagonal > maxd:
                maxd = diagonal
                maxa = area
            elif diagonal == maxd:
                if area > maxa:
                    maxa = area
            else:
                continue
        return maxa
        
