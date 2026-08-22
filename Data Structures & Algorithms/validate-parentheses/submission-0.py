class Solution:
    def isValid(self, s: str) -> bool:
        list2 = []
        dict1 = {'(':')',
        '{' : '}',
        '[' : ']'
        }
        

        for c in s:
            list2.append(c)

            if len(list2) >= 2:
                if list2[-2] in dict1 and dict1[list2[-2]] == list2[-1]:
                    list2.pop()
                    list2.pop()

        return not list2
