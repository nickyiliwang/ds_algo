def minWindow(s, t):
    if len(s) < len(t):
        return ""

    if t == "":
        return ""

    window, countT = {}, {}

    # CountT map, default 0 unless key exists, then increment
    for c in t:
        countT[c] = countT.get(c, 0) + 1

    # len of countT counts how many keys are there.
    # "have" and "need" helps with keeping track of meeting the result condition
    have, need = 0, len(countT)

    # results initialization
    res, resLength = [-1, -1], float("infinity")

    left = 0
    for right in range(len(s)):
        # we are updating the window, adding the count to it
        c = s[right]
        window[c] = window.get(c, 0) + 1

        # after adding a new char
        # increment have if:
        # this char is in countT (we only care about certain chars)
        # the value belong to the char key in both map match
        # we satisfied a condition
        if c in countT and window[c] == countT[c]:
            have += 1

        # if have and need matches
        while have == need:
            # update our result
            # (right - left + 1) is the size/length of current window
            if (right - left + 1) < resLength:
                res = [left, right]
                resLength = (right - left + 1)

            # pop/shrink from the left of our window
            # first remove the char from the map
            window[s[left]] -= 1
            # if the left pointer char is in countT map
            # and the char in window count is now less than countT
            # this condition will update the "have" count
            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            # ++ to left count
            left += 1

    left, right = res
    return s[left:right + 1] if resLength != float("infinity") else ""


s = "ADOBECODEBANC"
t = "ABC"
minWindow(s, t)