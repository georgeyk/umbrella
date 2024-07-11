"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:

- 1 <= s.length <= 2000
- s only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.

---

Common solution to this problem is O(n**2), using a stack.

The name "Wormhole Teleportation technique" comes from the idea that
we "teleport" when we find a "portal", the parenthesis pairs in this case.
When teleporting the direction is swapped. The stop condition will be met by
going out of bounds.
The movement in traversing the string builds the solution.

Very elegant solution yielding O(n) time complexity.
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        opened = []
        wormholes = {}

        for i, ch in enumerate(s):
            if ch == "(":
                opened.append(i)
            elif ch == ")":
                j = opened.pop()
                wormholes[i] = j
                wormholes[j] = i

        idx = 0
        direction = 1
        result = []

        while idx < n:
            if idx in wormholes:
                idx = wormholes[idx]
                direction *= -1
            else:
                result.append(s[idx])

            idx += direction

        return "".join(result)


if __name__ == "__main__":
    sample_input = "(ed(et(oc))el)"
    retval = Solution().reverseParentheses(sample_input)
    print(retval)
