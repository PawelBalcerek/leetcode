from collections import deque
from heapq import heapify_max, heappop_max, heappush_max


class Solution:
    def task_scheduler(self, tasks: list[str], n: int) -> int:
        task_counts = {}
        for t in tasks:
            task_counts[t] = task_counts.get(t, 0) + 1
        counts = [v for v in task_counts.values()]
        heapify_max(counts)

        result = 0
        queue = deque()  # (count - 1, cooldown [result + n])
        while counts or queue:
            result += 1

            count = heappop_max(counts) - 1 if counts else 0
            if count:
                queue.append((count, result + n))

            if queue and queue[0][1] == result:
                heappush_max(counts, queue.popleft()[0])

        return result
