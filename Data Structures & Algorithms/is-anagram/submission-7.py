class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #alternate solution from Group Anagrams
        res = []
        for word in (s,t):
          count = [0] *26
          for c in word:
            count[ord(c)- ord("a")] +=1
          res.append(count)
        return res[0] == res[1]