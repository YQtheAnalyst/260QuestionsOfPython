# Keeping the last N items
# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing

# My solution:
# say if you want to keep the last 3 items seen in iteration
list1 = [0,1,2,3,4,5,6,7,"ok","no"]
l = len(list1)
for i in range(l):
    if i >= list1[-3]:
        print(list1[i])


# Official Solution:
# todo: I am still confused about what is happening here
from collections import deque
def search(lines, pattern, history):
     previous_lines = deque(maxlen=history)
     for line in lines:
         if pattern in line:
            yield line, previous_lines
            previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


# Very confused, maybe see the discussion first

# deque(maxlen) will limit the length inside the q!
# and it will remove the oldest one when adding the new element!
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
# or if you do not want to limit the maxlen, it will create list with no limit!
q1 = deque()
q1.append(1)
q1.append(2)
q1.appendleft(0)
q1.pop()
q1.popleft()
print(q1)
print(type(q)) # the type is collection.deque
print(type(list(q))) # can turn it back to list!

# Adding or popping items from either end of a queue has O(1) complexity. This is unlike
# a list where inserting or removing items from the front of the list is O(N).
# Learned the Big O Notation here！ So it stands the time of execution
# O(1) means it can be executed in a constant time
# O(n) means it depends on the amounts of operations

# Alright, get back to the official solution:
# it seems it wants to return the previous N lines which contain "python"

from collections import deque

def get_previous_lines(filename, pattern, maxlength):
    with open(filename) as file:
        result = deque(maxlen=maxlength)
        for line in file:
            if pattern in line:
                result.append(line)
                print(line)
                if len(result) == maxlength:
                    break

get_previous_lines("somefile.txt", "python", 3)



