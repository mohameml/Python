
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Garde une trace des minima

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)  # Ajoute seulement si val ≤ minimum actuel

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()  # Supprime le minimum s'il est dépilé

    def getMin(self):
        return self.min_stack[-1]  # O(1)


# ["MinStack","push","push","push","getMin","pop","getMin","pop","getMin","pop","push","push","push","getMin","pop","top","getMin","pop","getMin","pop"]
# [[],[0],[1],[0],[],[],[],[],[],[],[-2],[-1],[-2],[],[],[],[],[],[],[]]

# val : [null,null,null,null,0,null,0,null,1,null,null,null,null,-2,null,-2,-2,null,-1,null]
# exp : [null,null,null,null,0,null,0,null,1,null,null,null,null,-2,null,-2,-2,null,-1,null]


ms = MinStack()
ms.push(0)
ms.push(1)
ms.push(0)
print(ms.getMin())  # 0 
ms.pop()
print(ms.getMin())  # 0 
ms.pop()
print(ms.getMin())  # 1
ms.pop()
