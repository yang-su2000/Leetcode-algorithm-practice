class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ls = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                ls.append(t)
                continue
            for t2 in transactions:
                name2, time2, amount2, city2 = t2.split(',')
                if abs(int(time) - int(time2)) <= 60 and name == name2 and city != city2:
                    ls.append(t)
                    break
        return ls