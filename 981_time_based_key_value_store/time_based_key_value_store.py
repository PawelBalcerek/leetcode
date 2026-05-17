from collections import defaultdict


class TimeBasedKeyValueStore:
    def __init__(self) -> None:
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.__search(self.store[key], timestamp)

    def __search(self, values: list[tuple[int, str]], timestamp: int) -> str:
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return values[l - 1][1] if l - 1 >= 0 else ""
