"""
347. Top K Frequent Elements

Given an integer array `nums` and an integer `k`,
return the `k` most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    1. Create a 2D-array A with size nums + 1,
        where each subarray store elements corresponding to their frequency.
    2. Map each element's frequency to the element itself using a hash map.
    3. Iterate through the mappings (element, frequency),
        appending each element to A[frequency].
        This step organizes elements by increasing frequency.
    4. Print an array of k elements, starting from the end of the array in A.

    Time Complexity: O(n)
    """
    k_elements = []
    count_buckets = [[] for i in range(len(nums) + 1)]
    count_map = {}  # element : count

    for n in nums:
        count_map[n] = 1 + count_map.get(n, 0)

    for num, count in count_map.items():
        count_buckets[count].append(num)

    for i in range(len(count_buckets) - 1, 0, -1):
        for num in count_buckets[i]:
            k_elements.append(num)
            if len(k_elements) == k:
                return k_elements
    return []
