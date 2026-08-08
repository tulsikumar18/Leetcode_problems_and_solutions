class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        # push to minStack , if it is empty or values is less than last minimum in minStack
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)        
        

    def pop(self):
        """
        :rtype: None
        """

        if not self.stack:
            return None
        else:
            val = self.stack.pop()
            ## if the popped elment is the min value then it has to be popped from the minStack as well.

            if val == self.minStack[-1]:
                self.minStack.pop()

            return val
    

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minStack:
            return None
        else:
            return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()