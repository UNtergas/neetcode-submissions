class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord==endWord:
            return 1
        if endWord not in wordList:
            return 0
        bucket=defaultdict(list)
        for w in wordList + [beginWord]:
            for i in range(len(w)):
                key = w[:i] + "*" + w[i+1:]
                bucket[key].append(w)

        visited=set()
        queue=deque([(1,beginWord)])
        while queue:
            d,current = queue.popleft()
            visited.add(current)
            for i in range(len(current)):
                key = current[:i] + "*" + current[i+1:]
                for n in bucket[key]:
                    if n == endWord:
                        return d+1
                    if n in visited:
                        continue
                    queue.append((d+1,n))
                bucket[key] = []
        return 0