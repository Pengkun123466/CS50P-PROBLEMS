class Jar:
    def __init__(self, capacity=12):#初始化一个饼干罐，该容量表示饼干罐中最多能容纳的饼干数量
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):#如果罐中有 3 块饼干，那么 __str__ 应返回 "🍪🍪🍪"。
        return "🍪" * self._size

    def deposit(self, n):#向饼干罐中添加 n 块饼干
        if self._size + n > self.capacity:
            raise ValueError
        self.size = self.size + n
        
    def withdraw(self, n):#从饼干罐中取出 n 块饼干 
        if self._size - n < 0:
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):#应返回饼干罐的容量
        return self._capacity

    @property
    def size(self):#返回饼干罐中实际的饼干数量
        return self._size
