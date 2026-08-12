class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """



        stack = []
        open_chrs = '([{'

        for i in range(len(s)):

            if s[i] in open_chrs:
                stack.append(s[i])

            else:
                if stack:

                    if (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                        stack.pop(-1)

                    else:
                        return False
                else:
                    return False

        if stack:
            return False
        else:
            return True
    

        