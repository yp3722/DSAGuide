#https://leetcode.com/problems/flood-fill/

class Solution:

    def DFSfill(self,image,r,c,x,y,prevColor,newColor):
        if x>=0 and x<r and y>=0 and y<c and prevColor == image[x][y] and prevColor!=newColor:
            image[x][y] = newColor
            self.BFSfill(image,r,c,x+1,y,prevColor,newColor)
            self.BFSfill(image,r,c,x-1,y,prevColor,newColor)
            self.BFSfill(image,r,c,x,y+1,prevColor,newColor)
            self.BFSfill(image,r,c,x,y-1,prevColor,newColor)

    def BFSfill(self,image,r,c,sr,sc,prevColor,newColor):
        q = collections.deque()
        q.append([sr,sc])
        while(len(q)!=0):
            pos = q.popleft()
            x,y = pos[0],pos[1]
            if x>=0 and x<r and y>=0 and y<c and prevColor == image[x][y] and prevColor!=newColor:
                image[x][y]=newColor
                q.append([x+1,y])
                q.append([x-1,y])
                q.append([x,y+1])
                q.append([x,y-1])
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        self.DFSfill(image,r,c,sr,sc,image[sr][sc],color)
        #self.BFSfill(image,r,c,sr,sc,image[sr][sc],color)
        return image
