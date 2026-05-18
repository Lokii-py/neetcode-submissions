class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse = True))
        output = []
        for key, value in sorted_dict.items():
            output.append(key)

        return output[:k]