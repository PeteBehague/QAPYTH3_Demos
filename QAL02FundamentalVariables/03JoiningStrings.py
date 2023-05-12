# Joining strings to strings
greeting = "Hello, "
name = input("Please enter your name: ")
question = ", how are you today?"
sentence = greeting + name + question
print(sentence)

# Adding numbers (as strings)
number1 = input("Please enter first number : ")
number2 = input("Please enter second number: ")
answer = number1 + number2
print(answer)

# Managing line breaks
line1 = "Said Hamlet to Ophelia,\nI'll draw a sketch of thee,\n"
line2 = "What kind of pencil shall I use?\n2B or not 2B?"
print(line1 + line2)

# Combining strings and numbers
equation = "2 + 2 ="
answer = 4
print(equation,answer)
output = equation + " " + answer
# output = equation + " " + str(answer)
print(output)
