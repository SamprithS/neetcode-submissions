from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common = counter.most_common(k)
        return [item[0] for item in most_common]
        