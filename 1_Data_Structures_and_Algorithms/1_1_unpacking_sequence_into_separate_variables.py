# Problem 1.1
#You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

tuple1 = (1,2,3,4,5,True,"apple","yes")
(*numbers, bool_value, fruit, answer)= tuple1
print(numbers)
print(bool_value)
print(fruit)
print(answer)

list1 = ['Jason', 13, 'UK', 'male', (2000,12,1),(2024,5,14)]
name, age, location,gender,dob,(year, month, day) = list1
print(name)
print(age)
print(location)
print(gender)
print(dob)
print(year)
print(month)
print(day)


# Discussion
# works for all iterable objects (strins, files, generators, iterators)
# give throwaway variable name if unneeded
string1 = "HwLoo"
capital1, _, capital2, _, _ = string1
print(capital1)
print(capital2)
