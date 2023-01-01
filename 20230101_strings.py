# print greeting message

print("Hello World!")


# or

message = "Hello World!"

print(message)


# or for multiple lines

message = """Hello World!
How are you?"""

print(message)


# now let's count the length of our string

message = "Hello World!"

print(len(message))


# print a specific character or range of characters

message = "Hello World!"

print(message[6])
print(message[0:5])  # characters 0 up to but not including 5


# now let's edit the strings a little

message = "Hello World!"

print(message.lower())
print(message.upper())


# okay more editing but fun

question = "Would you like to play a game?"
name = "Kristy"

# option 1 : easy to understand, but very long
message = "Hello, " + name + ". " + question
print(message)

# option 2 : cleaner and easier to scale up
message = "Hello, {}. {}".format(name, question)
print(message)






