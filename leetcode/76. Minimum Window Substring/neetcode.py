class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Explore: Why not only start counting when one of the characters from 't' is found,
        # instead of counting everything from start and subtract them again?
        # Because it will only reduce small counts when characters not in 't' are counted,
        # but for the duplicate cases, you would need to subtract again.

        # Added s < t edge case
        if t == "" or len(s) < len(t):
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Why 'need' counts only unique characters?
        # because below, 'have' will only +1 when both window[c] and countT[c] counts are the same
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                # This is the part where it will handle the duplicate cases
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
