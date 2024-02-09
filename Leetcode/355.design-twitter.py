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
from collections import deque


# @lc code=start
class Twitter:

    def __init__(self):
        self.database = {}
        self.feed = deque([])
        self.time = -1

    def createUser(self, userId):
        self.database[userId] = {"follows": set([userId])}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.database:
            self.createUser(userId)

        self.feed.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        for tweet in self.feed:
            if tweet[0] in self.database[userId]["follows"]:
                res.append(tweet[1])

        while len(res) > 10:
            res.pop()

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.database:
            self.createUser(followerId)
        if followeeId not in self.database:
            self.createUser(followeeId)

        self.database[followerId]["follows"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.database or followeeId not in self.database:
            return

        if followeeId in self.database[followerId]["follows"]:
            self.database[followerId]["follows"].remove(followeeId)


# Your Twitter object will be instantiated and called as such:

# param_2 = obj.getNewsFeed(userId)
# obj.unfollow(followerId,followeeId)
# @lc code=end


obj = Twitter()
obj.postTweet(1, 5)
obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.unfollow(1, 2)
obj.getNewsFeed(1)


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
