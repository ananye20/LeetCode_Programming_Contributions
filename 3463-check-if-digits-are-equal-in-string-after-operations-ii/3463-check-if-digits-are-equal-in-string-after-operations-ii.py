class Solution:
    def hasSameDigits(self, s: str) -> bool:
        C5 = []
        i = 0
        while i < 5:
            row = []
            j = 0
            while j < 5:
                row.append(0)
                j += 1
            C5.append(row)
            i += 1
        i = 0
        while i < 5:
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    C5[i][j] = 1
                else:
                    C5[i][j] = (C5[i-1][j] + C5[i-1][j-1]) % 5
                j += 1
            i += 1

        def CombMod5(n, k):
            if k > n:
                return 0
            r = 1
            while n > 0 or k > 0:
                n0 = n % 5
                k0 = k % 5
                if k0 > n0:
                    return 0
                r = (r * C5[n0][k0]) % 5
                n //= 5
                k //= 5
            return r

        def CombMod10(n, k):
            if k > n:
                return 0
            c2 = 1 if (k & n) == k else 0
            c5 = CombMod5(n, k)
            x = c5
            if x % 2 != c2:
                x += 5
            return x % 10

        n = len(s)
        d = 0
        i = 0
        while i < n - 1:
            c = CombMod10(n - 2, i)
            diff = (int(s[i]) - int(s[i+1])) % 10
            d = (d + c * diff) % 10
            i += 1
        return d == 0