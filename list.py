marks = [20.3, 36.5, 93.7, 88.3, 90.4]

print(marks[4])

# marks[3] = 70.2

print(marks[3])
marks.append(60.3)
marks.sort(reverse=True)
print(marks)
print(marks)

list = [1, 2, 3, 4, 5]
list.reverse()
list.pop(3)
print(list)
list2 = ['a', 'b', 'c', 'd']
list3 = list + list2
list3.insert(2, 'x')
list3.remove(5)

print(list3)

tuples = (1, 2, 3, 4, 5)
print(tuples[2])
print(type(tuples))
# tuples(3) = 0  # This line will raise an error because tuples are immutable 
print(tuples[2 : 4])
print(len(tuples))
print(tuples.count(3))
print(tuples.index(4))