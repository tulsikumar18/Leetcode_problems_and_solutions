class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for ch in s:
            ## opening brackets , simply push it into stack..
            if ch in '({[':
                stack.append(ch)
            
            else:
                # stack shouldn't be empty..
                if stack:
                    if stack[-1] != pairs[ch]:
                        return False
                    else:
                        stack.pop(-1)
                
                else:
                    return False

        if stack:
            return False

        return True




    

        