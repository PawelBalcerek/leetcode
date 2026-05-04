class Solution:
    def car_fleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        cars = []

        for i in range(len(positions)):
            cars.append((positions[i], speeds[i]))

        cars.sort(reverse=True)
        stack = []
        
        for position, speed in cars:
            finished_after = (target - position) / speed
            if not stack or stack[-1] < finished_after:
                stack.append(finished_after)

        return len(stack)
