class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.counters = {}
        self.count = 0
        self.lru_start = 1
        self.lrus = defaultdict(lambda: OrderedDict())

    def get(self, key: int) -> int:
        if key in self.counters:
            # remove prev
            key_count = self.counters[key]
            self.counters[key] += 1
            value = self.lrus[key_count][key]
            del self.lrus[key_count][key]
            if len(self.lrus[self.lru_start]) == 0:
                self.lru_start += 1
            # add new
            self.lrus[key_count + 1][key] = value
            # print(self.count, self.counters)
            # print(self.lru_start, self.lrus)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        # put
        if key in self.counters:
            # remove prev
            key_count = self.counters[key]
            self.counters[key] += 1
            del self.lrus[key_count][key]
            if len(self.lrus[self.lru_start]) == 0:
                self.lru_start += 1
            # add new
            self.lrus[key_count + 1][key] = value
        else:
            # resize
            if self.count == self.cap:
                if self.cap == 0:
                    return
                delkey, _ = self.lrus[self.lru_start].popitem(last=False)
                # print('del', delkey)
                if len(self.lrus[self.lru_start]) == 0:
                    self.lru_start += 1
                self.count -= 1
                del self.counters[delkey]
            # add new
            self.counters[key] = 1
            self.count += 1
            self.lru_start = 1
            self.lrus[1][key] = value
        # print(self.count, self.counters)
        # print(self.lru_start, self.lrus)
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)