class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        
        rows = m
        columns = n
        unique_paths = [[1 for x in range(columns)] for y in range(rows)]
        
        for x in range(1, rows):
            for y in range(1, columns):
                unique_paths[x][y] = unique_paths[x][y-1] + unique_paths[x-1][y]
        
        return unique_paths[rows - 1][columns - 1]
       
       
       
       #timeComplexity: 0(m) * 0(n)
       #spaceComplexity: 0(m) * 0(n)
