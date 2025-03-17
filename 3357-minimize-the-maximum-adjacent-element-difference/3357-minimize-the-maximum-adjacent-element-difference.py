class Solution:
        def minDifference(self, A: List[int]) -> int:
            n = len(A)
            max_adj, mina, maxb = 0, inf, 0
            for a,b in pairwise(A):
                if a > 0 and b > 0:
                    max_adj = max(max_adj, abs(a - b))
                elif a > 0 or b > 0:
                    mina = min(mina, max(a, b))
                    maxb = max(maxb, max(a, b))
            res = 0
            min_2r = (maxb - mina + 2) // 3 * 2 # min 2r if [a,x,y,b] is better
            for i in range(n):
                if (i > 0 and A[i - 1] == -1) or A[i] > 0: continue
                j = i
                while j < n and A[j] == -1:
                    j += 1
                a, b = inf, 0
                if i > 0:
                    a = min(a, A[i - 1])
                    b = max(b, A[i - 1])
                if j < n:
                    a = min(a, A[j])
                    b = max(b, A[j])
                res = max(res, min(maxb - a, b - mina, min_2r if j - i > 1 else inf))
            return max(max_adj, (res + 1) // 2)