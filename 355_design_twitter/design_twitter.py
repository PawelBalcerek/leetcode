from collections import defaultdict
from heapq import heapify_max, heappop, heappop_max, heappush


class Solution:
    def __init__(self):
        self.tweet_id = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_id, tweetId))
        self.tweet_id += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = []
        for f in self.followers[userId] | {userId}:
            for t in self.tweets[f][-10:]:
                heappush(tweets, t)
                if len(tweets) > 10:
                    heappop(tweets)

        heapify_max(tweets)

        news_feed = []
        while tweets:
            news_feed.append(heappop_max(tweets)[1])
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
