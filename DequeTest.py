from collections import deque

myDeque = deque([(1,"첫번째"), (2,"두번째"), (3, "3번째"), (4, "네번째"), (5, "다섯번째")])

print("전체 데큐 :", myDeque)

firstData = myDeque.popleft()

print("왼쪽 첫번째 데이터 : ", firstData)
print("현재 데큐 : ", myDeque)

myDeque.append(firstData)
print("현재 데큐 :",myDeque)