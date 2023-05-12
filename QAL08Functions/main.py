def addition(number1,number2):
    total = number1 + number2
    return total

def print_result(number1, number2, total):
    print(number1, "+", number2, "=", number1 + number2)

for i in range(3):
    for j in range(4):
        total = addition(i,j)
        print_result(i, j, total)

