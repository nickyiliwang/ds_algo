#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (38.96%)
# Likes:    3691
# Dislikes: 485
# Total Accepted:    161.7K
# Total Submissions: 415.2K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' + '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
#
# Implement the Twitter class:
#
#
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
#
#
#
# Example 1:
#
#
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
#
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
#
#
#
# Constraints:
#
#
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
#
#
#

from typing import List
import heapq
from collections import deque, defaultdict


# @lc code=start
# None optimized solution with looping the entire feed database
class Twitter:

    def __init__(self):
        self.followDB = defaultdict(set)
        self.feed = deque([])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        self.followDB[userId].add(userId)
        for tweet in self.feed:
            if tweet[0] in self.followDB[userId] and len(res) < 10:
                res.append(tweet[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDB[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followDB[followerId].discard(followeeId)


# @lc code=end


obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))


# optimized solution with almost linked list like structure.
class Twitter:

    def __init__(self):
        self.count = 0
        self.followDB = defaultdict(set)
        self.feedDB = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feedDB[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followDB[userId].add(userId)  # follows self

        for followeeId in self.followDB[userId]:
            if followeeId in self.feedDB:
                recentIdx = len(self.feedDB[followeeId]) - 1
                prevIdx = recentIdx - 1
                count, tweetId = self.feedDB[followeeId][recentIdx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, prevIdx])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, prevIdx = heapq.heappop(minHeap)
            res.append(tweetId)
            if prevIdx >= 0:
                count, tweetId = self.feedDB[followeeId][prevIdx]
                prevIdx = prevIdx - 1
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, prevIdx],
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDB[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
        self.followDB[followerId].discard(followeeId)

        # if followeeId in self.followDB[followerId]:
        #     self.followDB[followerId].remove(followeeId)


# obj.follow(2, 1)
# obj.getNewsFeed(2)
# obj.postTweet(2, 6)
# obj.getNewsFeed(1)
# obj.getNewsFeed(2)
# obj.unfollow(2, 1)  # this one
# obj.getNewsFeed(1)
# obj.getNewsFeed(2)  # this one
# obj.unfollow(1, 2)
# obj.getNewsFeed(1)
# obj.getNewsFeed(2)
