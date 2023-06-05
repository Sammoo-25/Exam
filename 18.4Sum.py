import itertools
from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    combinations = itertools.combinations(nums, 4)

    for combo in combinations:
        if sum(combo) == target:
            result.append(list(combo))
    return result
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))