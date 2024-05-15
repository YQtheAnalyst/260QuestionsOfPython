# Unpacking Elements from Iterables of Arbitrary Length
# You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a “too many values to unpack” exception.

iter1 = [1,2,3,4,5,6,'ok',7,8,9,'no']
# To replicate the exception:
# item1, item2 = iter1

# What if I only want to unpack the numbers?
*item1, text1 = iter1
print(item1)
print(text1)

# Solution:
# Application case
# if you want to drop the lowest grade and highest grade
grades = [12,83,9,90,23,45,66,86,64,70]
grades = sorted(grades)
lowest,*grades,highest = grades
print(lowest)
print(grades)
print(highest)

# So "Unpacking" can quickly grasp the values on the tail and head!

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(name)
print(email)
print(phone)

# Application case 2
# If I want to split the foo and bar in the following tuple
records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]

# foo_list = []
# bar_list = []
# for i in records:
#     (name, *value) = i
#     if name == 'foo':
#         foo_list.append(i)
#     elif name == "bar":
#         bar_list.append(i)
#
# print(foo_list)
# print(bar_list)

def get_foo(value1, value2):
    print(value1)
    print(value2)

def get_bar(values):
    z= values
    print(z)

for tags, *args in records:
    if tags == "foo":
        get_foo(*args)
    elif tags == "bar":
        get_bar(*args)


# Application case 3
# an easy function is given to the variable
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
name, *fields, link1, link2 = line.split(':')
print(name)
print(link1)
print(link2)

# Application case 4
# recursive algorithm
# todo do not understand
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


# Conclusion
# star expression is useful when you do not know about the length of an arbitrary iterable, and are interested in head and tail values.
# unpacked variable can be assigned values or use in for loop directly
# unpacked variable can also be used when the target is a transformation of a value, as long as it is iterable
# You need more practice to use *args
