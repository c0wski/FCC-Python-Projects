# Function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.

def arithmetic_arranger(problems, solve=False):
    first_num = ''
    second_num = ''
    line = ''
    results = ''

    # max 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # split the input into parts
    for problem in problems:
        items = problem.split()
        first = items[0]
        operator = items[1]
        second = items[2]

        # check numbers only contain digits
        if first.isdigit() == False or second.isdigit() == False:
          return 'Error: Numbers must only contain digits.'

        # Addition/subtraction and
        # Operator Check: only + or -
        if operator == '+':
            solution = str(int(first) + int(second))
        elif operator == '-':
            solution = str(int(first) - int(second))
        else:
            return "Error: Operator must be '+' or '-'."

        # Operand length check: max 4
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # format; sort into lines
        length = max(len(first), len(second)) + 2
        top = str(first).rjust(length)
        bottom = operator + str(second).rjust(length - 1)
        lines = ''
        for x in range(length):
            lines += '-'
        result = str(solution.rjust(length))

        # collect data into lines
        if problem != problems[-1]:
            first_num += top + '    '
            second_num += bottom + '    '
            line += lines + '    '
            results += result + '    '

        else:
            first_num += top
            second_num += bottom
            line += lines
            results += result

        if solve:
          string = first_num + '\n' + second_num + '\n' + line + '\n' + results
        else:
          string = first_num + '\n' + second_num + '\n' + line

    return string

