import heapq
class Twitter:
    def __init__(self):
        self.following = [set() for _ in range(1000)]
        self.tweets = [[] for _ in range(1000)]
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        while heap and len(res) < 10:
            negTime, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            prev_idx = idx - 1
            if prev_idx >= 0:
                time, prevTweetId = self.tweets[uid][prev_idx]
                heapq.heappush(heap, (-time, prevTweetId, uid, prev_idx))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
