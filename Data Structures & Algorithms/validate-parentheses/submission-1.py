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



 # Mistake: Used list2[i-1] / list2[i], but i refers to the original string.
# Since list2 changes size when elements are popped, its indices no longer match i.
# Use list2[-2] and list2[-1] to always check the current last two elements.
