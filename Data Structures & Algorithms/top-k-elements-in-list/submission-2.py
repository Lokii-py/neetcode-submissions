class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_count.items():
            bucket = buckets[freq]
            bucket.append(num)
        
        output = []
        for i in range(len(buckets) - 1, - 1, -1):
            for num in buckets[i]:
                output.append(num)

            if len(output) == k:
                return output