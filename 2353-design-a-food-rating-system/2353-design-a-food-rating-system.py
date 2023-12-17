from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d = {}
        self.s = defaultdict(lambda: SortedSet())
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.s[cuisine].add((-rating, food))
            self.d[food] = (cuisine, rating)
        # print(self.s)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.d[food]
        self.d[food] = (cuisine, newRating)
        self.s[cuisine].remove((-rating, food))
        self.s[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.s[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)