#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#
# Constraints:
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.
#
from typing import *
from collections import *

# Time:
# Space:

# @lc code=start
class TimeMap:

    def __init__(self):

    def set(self, key: str, value: str, timestamp: int) -> None:

    def get(self, key: str, timestamp: int) -> str:

# @lc code=end