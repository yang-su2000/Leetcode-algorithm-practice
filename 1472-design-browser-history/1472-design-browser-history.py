class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = homepage
        self.f = []
        self.b = []

    def visit(self, url: str) -> None:
        self.b.append(self.cur)
        self.cur = url
        self.f.clear()

    def back(self, steps: int) -> str:
        while steps and self.b:
            self.f.append(self.cur)
            self.cur = self.b.pop()
            steps -= 1
        return self.cur

    def forward(self, steps: int) -> str:
        while steps and self.f:
            self.b.append(self.cur)
            self.cur = self.f.pop()
            steps -= 1
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)