"""
Twitter
10 개의 최신 트윗을 볼 수 있음
unique tweetId 생성

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

"""
from typing import List
from collections import deque


class Twitter:

    def __init__(self):
        self.t = 0
        self.followers = {}
        self.tweets_user = {}  # key = tweetId, value = userId
        self.created_tweets = {}  # key = userId, value = [(tweetId, time)]
        self.latest_tweets = {}  # key = userId, value = [(tweetId, time)]

    def _merge(self, tweets1: deque, tweets2: deque):
        p1, p2 = 0, 0
        merged = deque()

        while p1 < len(tweets1) and p2 < len(tweets2):
            # t 가 클수록 최신임
            if tweets1[p1][1] < tweets2[p2][1]:
                merged.append(tweets2[p2])
                p2 += 1
            else:
                merged.append(tweets1[p1])
                p1 += 1

        while p1 < len(tweets1):
            merged.append(tweets1[p1])
            p1 += 1

        while p2 < len(tweets2):
            merged.append(tweets2[p2])
            p2 += 1

        return merged

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers:
            self.followers[userId] = [userId]

        for follower in self.followers[userId]:
            if follower not in self.latest_tweets:
                self.latest_tweets[follower] = deque()
            self.latest_tweets[follower].appendleft((tweetId, self.t))

        if userId not in self.created_tweets:
            self.created_tweets[userId] = deque()

        self.created_tweets[userId].appendleft((tweetId, self.t))
        self.tweets_user[tweetId] = userId
        self.t += 1 # time

    def getNewsFeed(self, userId: int) -> List[int]:
        latest = self.latest_tweets.get(userId, [])
        return [latest[i][0] for i in range(min(10, len(latest)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.followers[followeeId] = [followeeId]

        if followerId not in self.followers[followeeId]:
            self.followers[followeeId].append(followerId)
            self.latest_tweets[followerId] = self._merge(self.latest_tweets.get(followerId, deque()), self.created_tweets.get(followeeId, deque()))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.followers[followeeId] = []
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)

        if followerId in self.latest_tweets:
            new_tweets = deque()
            for tweet in self.latest_tweets.get(followerId, []):
                if self.tweets_user[tweet[0]] != followeeId:
                    new_tweets.append(tweet)
            self.latest_tweets[followerId] = new_tweets


if __name__ == '__main__':
    obj = Twitter()
    # obj.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
    # obj.getNewsFeed(1) # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    # obj.follow(1, 2)  # User 1 follows user 2.
    # obj.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
    # obj.getNewsFeed(1)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    # obj.unfollow(1, 2)  # User 1 unfollows user 2.
    # obj.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
    #
    # obj.postTweet(1, 1)
    # obj.getNewsFeed(1)
    # obj.follow(2, 1)
    # obj.getNewsFeed(2)  # [1]

    # obj.postTweet(1, 4)
    # obj.postTweet(2, 5)
    # obj.unfollow(1, 2)
    # obj.follow(1, 2)
    # obj.getNewsFeed(1)

    obj.postTweet(1, 5)
    obj.follow(1, 2)
    obj.follow(2, 1)
    obj.getNewsFeed(2)
    obj.postTweet(2, 6)
    obj.getNewsFeed(1)
    obj.getNewsFeed(2)
    obj.unfollow(2, 1)
    obj.getNewsFeed(1)
    obj.getNewsFeed(2)
    obj.unfollow(1, 2)
    obj.getNewsFeed(1)
    obj.getNewsFeed(2)