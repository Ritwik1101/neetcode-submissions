class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in anagram_map:
                anagram_map[key].append(i)
            else:
                anagram_map[key]=[i]
        return list(anagram_map.values())            




        