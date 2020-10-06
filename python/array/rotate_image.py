class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #thing to remember with 2d grid swaps is that there is only so many things we can do, this is one of them
        
        n = len(matrix[0]) #length of the row (and col)
        for row in range(n):
          for col in range(row, n):
            #swap for each cell
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row] 
            
        for i in range(n):
          matrix[i].reverse() #have to reverse it

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = 
[[1,2,3],
[4,5,6],
[7,8,9]]

Output: 
[[7,4,1],
[8,5,2],
[9,6,3]]