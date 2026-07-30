import heapq
class Twitter:
    def __init__(self):
        self.following = [set() for _ in range(1000)]
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        t = []
        for i in range(len(self.tweets)-1, -1, -1):
            if self.tweets[i][0] in self.following[userId] or self.tweets[i][0] == userId:
                t.append(self.tweets[i][1])
                if len(t) == 10:
                    return t
        return t

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
