#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (86.24%)
# Likes:    1963
# Dislikes: 3745
# Total Accepted:    248.6K
# Total Submissions: 288.3K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a
# tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work. You
# just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
# can be decoded to the original URL.
#
# Implement the Solution class:
#
#
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given
# shortUrl. It is guaranteed that the given shortUrl was encoded by the same
# object.
#
#
#
# Example 1:
#
#
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
#
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding
# it.
#
#
#
# Constraints:
#
#
# 1 <= url.length <= 10^4
# url is guranteed to be a valid URL.
#
#
#


# @lc code=start
class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl):
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl

        return self.encodeMap[longUrl]

    def decode(self, shortUrl):
        return self.decodeMap[shortUrl]


# Your Codec object will be instantiated and called as such:
# @lc code=end

codec = Codec()
codec.decode(codec.encode("https://www.udemy.com/course/ue5-multiplayer-fps/"))

# Input: url = "https://leetcode.com/problems/design-tinyurl"


class Codec:
    def __init__(self):
        self.db = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        chunks = longUrl.split("/")
        self.db = {}
        code = "".join([chunk[:2] for chunk in chunks])
        shortUrl = "http://tinyurl.com/" + code
        self.db[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        return self.db[shortUrl]
