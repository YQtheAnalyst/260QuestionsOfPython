# You want to make a list of the largest or smallest N items in a collection

list1 = [1,2,76,34,0,87,-9,235,7,67.9,-2.4]

largest5 = sorted(list1)[-5:]
print(largest5)

smallest3 = sorted(list1)[:3]
print(smallest3)


portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# Solution
import heapq
print(heapq.nlargest(5,list1))
print(heapq.nsmallest(3,list1))

# find smallest in a dictionary containing keys
print(heapq.nlargest(3, portfolio, key=lambda s: s['price']))
print(portfolio[0]['price'])

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
cheap_name = [i['name'] for i in cheap]
print(cheap_name)

# If N is closed to the overall number, you can choose to use min() or max()
# or sorted()
# heapq is quicker if N and overall numbers are very different.

# Todo: Further Question:
# How to find the second largest number?
list2 = [1,2,76,34,0,87,-9,235,7,67.9,-2.4,600,600,600,600]
print(heapq.nlargest(2,list2)) # does not work
list2.remove(max(list2)) # does not work
print(list2)

