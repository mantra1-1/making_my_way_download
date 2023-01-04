
# lists

course = ['History', 'Math', 'Physics']

print(course)


# and let's not forget about counting the individual data:

course = ['History', 'Math', 'Physics']

print(len(course))


# but what about pulling a specific datum from the list?

course = ['History', 'Math', 'Physics']

print(course[0])
print(course[0:2])
print(course[-1])
# this last one is important because it allows me to pull the last datum of a list no matter the length


# let's play with some addition methods

course = ['History', 'Math', 'Physics']
print(course)

course.append('Art')
print(course)

course.insert(0, 'CompSci')
print(course)


# but what if I want to add a whole list to another list?

course = ['History', 'Math', 'Physics']
course_2 = ['Art', 'CompSci']

course.append(course_2)
# adds the variable as one whole datum
print(course)

course = ['History', 'Math', 'Physics']
course_2 = ['Art', 'CompSci']

course.extend(course_2)
# adds each datum from list 2 to list 1 as new datums
print(course)


















