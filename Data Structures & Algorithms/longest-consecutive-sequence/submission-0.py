class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a_set = set(nums) #if there are any duplicates, a set will remove them
        longest = 0

        for num in a_set:
            if num-1 not in a_set:
                longer = 1
                while num+1 in a_set:
                    longer += 1
                    num += 1

                longest = max(longer, longest)

        return longest

        