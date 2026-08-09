class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parent_list = []
        for word in strs:
            char_count = {}
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            parent_list.append({
                "word": word,
                "count": char_count
            })
            
        output = []
        used = set()
        for i in range(len(parent_list)):
            if i in used:
                continue
            group = [parent_list[i]["word"]]
            used.add(i)
            for j in range(i + 1, len(parent_list)):
                if parent_list[i]["count"] == parent_list[j]["count"]:
                    group.append(parent_list[j]["word"])
                    used.add(j)
            output.append(group)
            
        return output