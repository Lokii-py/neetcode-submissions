class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        neg, zer, pos = [], [], []
        for num in nums:
            if num<0:
                neg.append(num)
            elif num>0:
                pos.append(num)
            else:
                zer.append(num)
        res = set()
        if len(zer)>2:
            res.add((0,0,0))
        n,p = set(neg), set(pos)

        if len(zer)>0:
            for each in n:
                if -each in p:
                    res.add((each,0,-each))

        for i in range(len(neg)):
            for j in range(i+1,len(neg)):
                target = -(neg[i]+neg[j])
                if target in p:
                    res.add(tuple(sorted([neg[i], neg[j], target])))
        
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                target = -(pos[i]+pos[j])
                if target in n:
                    res.add(tuple(sorted([target, pos[i], pos[j]])))
        
        return list(res)
