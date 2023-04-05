#https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = [{} for i in range(n)]
        mem[n-1][-1*nums[n-1]]=1
        if mem[n-1].get(nums[n-1])==None:
            mem[n-1][nums[n-1]]=1
        else:
            mem[n-1][nums[n-1]]+=1
        for i in range(n-2,-1,-1):
            pos = nums[i]
            neg = -1*nums[i]
            for k in mem[i+1].keys():
                if mem[i].get(pos+k)==None:
                    mem[i][pos+k]=1*mem[i+1][k]
                else:
                    mem[i][pos+k]+=(1*mem[i+1][k])                
                if mem[i].get(neg+k)==None:
                    mem[i][neg+k]=1*mem[i+1][k]
                else:
                    mem[i][neg+k]+=(1*mem[i+1][k])                
        if mem[0].get(target)==None:
            return 0
        return mem[0][target]
                
            