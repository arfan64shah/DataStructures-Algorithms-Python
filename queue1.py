from collections import deque

queue = deque()

queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)
queue.appendleft(4)

print(queue)

queue.pop()

print(queue)