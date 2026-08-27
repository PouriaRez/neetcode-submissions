class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            # for key in hmap:
            #     if sorted_word == key:
            #         hmap[key].append(word)
            #         break
            hmap[sorted_word].append(word)

        return [hmap[key] for key in hmap]