import sys


# Definition of addition function
def add(nums):
    result = 0
    for n in nums:
        result += n
    return result


# Definition of multiplication function
def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result


# Definition to evaluate the S-expression

'''I have used stack to evaluate the expression. 'buffer_list' is the list containing every character of 
    the expression as a single element in the list. For example ifexpression = "(add 1 2)" then the 
    buffer_list = ['(', ' ', 'a', 'd', 'd', ' ', '1', '2', ')']'''

'''I maintain a stack named 'calc_stack' to prioritize which sub-expression to evaluate first.'''
def evaluate_sexpression(expression):

    buffer_list = []
    buffer_list.extend(expression)

    if buffer_list[0] != '(':
        print("Error: Please provide valid expression")
        return
    calc_stack = []
    buffer_string = ""
    buffer_int = ""
    valid_paranthesis_count = 0

    for i in range(len(buffer_list)):

        if buffer_list[i].isalpha():
            buffer_string += buffer_list[i]
            continue

        if buffer_list[i].isnumeric():
            buffer_int += buffer_list[i]
            continue

        if buffer_string:
            calc_stack.append(buffer_string)
            buffer_string = ""

        if buffer_int:
            calc_stack.append(int(buffer_int))
            buffer_int = ""

        if buffer_list[i] == ')':
            valid_paranthesis_count -= 1

            if valid_paranthesis_count < 0:
                print("Error: Please provide expression with balanced paranthesis")
                return

            nums = []
            while calc_stack[-1] != '(':
                nums.append(calc_stack.pop())
            calc_stack.pop()

            if nums[-1] == 'add':
                nums.pop()
                if not calc_stack and i == len(buffer_list) - 1:
                    print(add(nums))
                    return
                else:
                    calc_stack.append(add(nums))

            if nums[-1] == 'multiply':
                nums.pop()
                if not calc_stack and i == len(buffer_list) - 1:
                    print(multiply(nums))
                    return
                else:
                    calc_stack.append(multiply(nums))

        if buffer_list[i] == "(":
            valid_paranthesis_count += 1
            calc_stack.append(buffer_list[i])

        else:
            continue



if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Error: Please provide the S-expression to evaluate")
    else:
        evaluate_sexpression(sys.argv[1])