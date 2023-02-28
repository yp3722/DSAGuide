#Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        lm = len(mat)
        ln = len(mat[0])

        #edge cases one d arrays
        if lm == 1:
            return mat[0]
        if len(mat[0])==1:
            op = []
            for i in range(lm):
                op.append(mat[i][0])
            return op

        op  = []

        i=0
        j=0
        directionIsForward = True #moving forwards = Top-Right and backwards = Bottom-Left 

        while( (i==lm-1 and j==ln-1)==False):
            op.append(mat[i][j])
            
            if directionIsForward :
                #normal case traverse top-right
                if i>0 and j<ln-1:
                    i-=1
                    j+=1
                
                #case top-right corner
                elif i==0 and j==(ln-1):
                    i+=1
                    directionIsForward=False
                #case top boundary
                elif i==0:
                    j+=1
                    directionIsForward=False
                #case right boundary
                elif j==ln-1:
                    i+=1
                    directionIsForward=False
            else:
                #normal traversal case bottom-left
                if i<lm-1 and j>0:
                    i+=1
                    j-=1
                #case bottom-left cornor
                elif i==(lm-1) and j==0:
                    j+=1
                    directionIsForward=True
                #case bottom boundary
                elif i==lm-1:
                    j+=1
                    directionIsForward=True
                #case left boundary
                elif j==0:
                    i+=1
                    directionIsForward = True
        op.append(mat[i][j])
        return op
                
                    
                




        



        