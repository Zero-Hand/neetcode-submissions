class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     lst1 = list(s)
     lst2 = list(t)
     if len(lst1) != len(lst2):
        return False
     lst1.sort()
     lst2.sort()
     if lst1 == lst2:
        return True
     return False   
