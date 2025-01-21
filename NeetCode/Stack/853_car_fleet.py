"""
853. Car Fleet

There are n cars at given miles away from the starting mile 0,
traveling to reach the mile target.

You are given two integer array position and speed,
both of length n, where position[i] is the starting mile of the ith car and
speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next
to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other.
The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target,
it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3

Explanation:
- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet,
  meeting each other at 12. The fleet forms at target.
- The car starting at 0 (speed 1) does not catch up to any other car,
  so it is a fleet by itself.
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet,
  meeting each other at 6. The fleet moves at speed 1 until it reaches target.

Example 2:
    Input: target = 10, position = [3], speed = [3]
    Output: 1

Explanation:
    There is only one car, hence there is only one fleet.

Example 3:
    Input: target = 100, position = [0,2,4], speed = [4,2,1]
    Output: 1

Explanation:
- The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet,
  meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
- Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become
  one fleet, meeting each other at 6. The fleet moves at speed 1 until it
  reaches target.
"""

from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    We sort cars by their time to reach the target in
    descending order to process the slowest cars first.

    This simplifies fleet merging:

    1. Why descending order?
       - Processing in ascending order (fastest first) makes it unclear which
         fleet a car will merge into, as it may catch up to multiple fleets.
       - In descending order, the car at the top of the stack is the slowest and
         closest to the target, ensuring we handle one fleet at a time.

    2. Fleet merging:
       - For each car, calculate its time to reach the target and
         compare it to the fleet at the top of the stack.
       - If the current car is faster (or takes the same time),
         it merges with the fleet at the top.
       - If it’s slower, it forms a new fleet.

    3. Stack utility:
       - The stack records distinct fleets by their time to reach the target.
       - By iterating in descending order,
         we consistently determine fleet formation.

    Time Complexity: O(n log n)
    Space complexity: O(n)
    """
    car_info = [(p, s) for p, s in zip(position, speed)]
    car_info.sort(reverse=True)
    stack = []
    for p, s in car_info:
        stack.append((target - p) / s)  # time = distance / speed
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
