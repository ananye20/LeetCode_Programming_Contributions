class Solution:
    def filterRestaurants(self, A, vegan, price, dist):
        A.sort(key=lambda x: (-x[1], -x[0]))
        return [i for i, _, v, p, d in A if v >= vegan and p <= price and d <= dist]