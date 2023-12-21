""""
Collection Modules - Deque

Is a high-performance list
"""
from collections import deque

deq = deque('Hello World')
print(deq)

# ADD Elements at the end of the list
deq.append('y')
print(deq)

# ADD Elements at the first position of the list
deq.appendleft('k')
print(deq)

# Remove elements

print(deq.popleft())

print(deq.pop())
