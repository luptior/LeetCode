class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        d = {}

        for s in strs:
            k = "".join(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]

        return list(d.values())