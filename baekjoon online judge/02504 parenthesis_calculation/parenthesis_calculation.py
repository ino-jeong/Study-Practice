class Stack():
    def __init__(self):
        self.data = []
        self.idx = []

    def push(self, idx, x):
        self.idx.append(idx)
        self.data.append(x)

    def pop(self):
        return (self.idx.pop(), self.data.pop())

    def peek(self):
        last_idx = len(self.data) - 1
        return (self.idx[last_idx], self.data[last_idx])

    def size(self):
        return len(self.data)


def addition_or_multiplication(peek, cal):  # compare two(2) parenthesis data whether they should be added or multiplied
    if peek[1][1] + 1 == cal[1][0]:  # if cal is just right next of peek, they are in contact : [peek][cal]
        return 1  # two data should be added
    elif peek[1][0] - 1 == cal[1][0] and peek[1][1] + 1 == cal[1][1]:  # in case of peek is included in cal : [cal[peek]]
        return 2  # two data should be multiplied
    else:
        return 0  # none of them


def handle_calculation(calculation_tuple, calculation_stack):
    if calculation_stack.size() == 0:  # if calculation stack (score stack) is empty, just push score
        calculation_stack.push(*calculation_tuple)
    else:
        calculation_peek = calculation_stack.peek()  # check top element of calculation stack
        data_relationship = addition_or_multiplication(calculation_peek, calculation_tuple)

        while data_relationship == 1 or data_relationship == 2:  # if top element of calculation stack is to be added or to be multiplied
            if data_relationship == 1:  # addition
                temp = calculation_stack.pop()
                calculation_tuple = (calculation_tuple[0] + temp[0], (temp[1][0], calculation_tuple[1][1]))
            else:  # multiplication
                temp = calculation_stack.pop()
                calculation_tuple = (calculation_tuple[0] * temp[0], (calculation_tuple[1][0], calculation_tuple[1][1]))

            if calculation_stack.size() == 0:  # if no more data to be peeked
                break
            calculation_peek = calculation_stack.peek()
            data_relationship = addition_or_multiplication(calculation_peek, calculation_tuple)

        calculation_stack.push(*calculation_tuple)  # after all calculation done, push again data


#  *************** main ***************

line_input = input()

stack = Stack() # store parenthesis data
calculation_stack = Stack() # store calculation data : '()' = 2 / '[]' = 3
is_valid = 'YES'  # is input parenthesis line is valid statement?

if line_input[0] == ')' or line_input[0] == ']':  # if start character is ) or ], this statement is already not valid
    is_valid = 'NO'

else :
    for idx in range(len(line_input)):

        ch = line_input[idx]

        if ch == '(' or ch == '[':
            stack.push(idx, ch)

        elif ch == ')':
            (i, data) = stack.pop()
            if data != '(':
                is_valid = 'NO'
                break

            calculation = (2, (i, idx))  # score tuple: (score, (left idx, right idx)) of data
            handle_calculation(calculation, calculation_stack)

        else:
            (i, data) = stack.pop()
            if data != '[':
                is_valid = 'NO'
                break

            calculation = (3, (i, idx))  # score tuple: (score, (left idx, right idx)) of data
            handle_calculation(calculation, calculation_stack)

    if stack.size() != 0:
        is_valid = 'NO'

if is_valid == 'NO':
    print(0)
else:
    print(calculation_stack.pop()[0])