class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookie_child = {}
        if not s:
            return 0

        g.sort()
        s.sort()

        for i, _ in enumerate(g):
            for cookie in s:
                if cookie >= g[i]:
                    cookie_child[i] = cookie
                    s.remove(cookie)
                    break

        return len(cookie_child)