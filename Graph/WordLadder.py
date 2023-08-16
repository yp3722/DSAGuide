from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = {}
        wlen = len(beginWord)
        wordList.append(beginWord)
        f = False
        visited = {}
        for word in wordList:
            visited[word]=False
            if word == endWord:
                f  = True
            for i in range(wlen):
                key = word[0:i]+"*"+word[i+1:]
                if d.get(key)==None:
                    d[key] = []
                d[key].append(word)
        
        if f == False:
            return 0
            
        q = deque()
        q.append((beginWord,1))
        visited[beginWord]=True
        while(len(q)>0):
            x = q.popleft()
            if x[0] == endWord:
                return x[1]
            
            
            for i in range(wlen):
                key = x[0][0:i]+"*"+x[0][i+1:]
                for wrd in d.get(key):
                    if visited[wrd]==False:
                        q.append((wrd,x[1]+1))
                        visited[wrd]=True

        return 0
            