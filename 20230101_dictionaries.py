
# these are super intuitive

myself = {'name': 'Kristy', 'age': 27, 'cities': ['Reno', 'Seattle']}
print(myself)


# call the key to get the value

print(myself['name'])
print(myself['age'])


# but what if the key I call isn't in the dictionary?

# print(myself['job'])
# throws an error

print(myself.get('job', 'Not Found'))
# finishes the code and returns a preset option for a bad query


# so let me go ahead and add that job to the dictionary

myself['job'] = 'Administrator'
print(myself.get('job', 'Not Found'))















