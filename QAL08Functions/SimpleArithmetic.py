def multiply(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
       return 0

    if num1 == 0 or num2 == 0:
        return 0

    neg_flag = False
    if num1 < 0:
        num1 = -num1
        neg_flag = not neg_flag
    if num2 < 0:
        num2 = -num2
        neg_flag = not neg_flag

    result = 0
    for i in range(0, num2):
        result += num1

    if neg_flag:
        result = -result
    return result



