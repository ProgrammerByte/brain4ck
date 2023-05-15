import sys
program = open(str(sys.argv[1]), 'rb').read().decode("utf-8")

num_cells = 32000
cells = [0] * num_cells
values = [0,1,2,3,4,5,6,7]

program = [*program]

def resolve(n):
    n = int(n)
    if n < 0:
        return (8 - (-n) % 8) % 8
    return n % 8

def resolve_cells(n):
    return (n + num_cells) % num_cells

ptr = 0
ptr_stack = []

i = 0
while i < len(program):
    c = program[i]

    if ptr < 0:
        ptr += num_cells
    elif ptr >= num_cells:
        ptr -= num_cells
    value_ptr = resolve(ptr)
    
    op = None
    if c.isnumeric():
        if int(c) >= 8:
            print()
            print("Current value being altered: " + str(value_ptr))
            print("Current instruction values:  " + str(values))
            print("Current memory address:      " + str(ptr))
            print("Cell and neighbors view:     " + "[..." + str(cells[resolve_cells(ptr - 1)]) + ", " + str(cells[ptr]) + ", " + str(cells[resolve_cells(ptr + 1)]) + "...]")
        else:
            op = resolve(values[int(c)])

    if op == 0:
        values[value_ptr] -= cells[ptr]
        cells[ptr] = int(input("\n"))
        values[value_ptr] += cells[ptr]
        values[value_ptr] = resolve(values[value_ptr])
    elif op == 1:
        print(chr(cells[ptr]), end="")
    elif op == 2:
        ptr += 1
    elif op == 3:
        ptr -= 1
    elif op == 4:
        ptr_stack.append(i)
        if cells[ptr] == 0:
            num = 1
            print(i)
            while num > 0 and i < len(program) - 1:
                i += 1
                if program[i].isnumeric():
                    if resolve(values[int(program[i])]) == 5:
                        num -= 1
                    elif resolve(values[int(program[i])]) == 4:
                        num += 1
    elif op == 5:
        if cells[ptr] == 0:
            if len(ptr_stack) > 0:
                ptr_stack.pop()
        else:
            if len(ptr_stack) == 0:
                i = -1
            else:
                i = ptr_stack[len(ptr_stack) - 1]
    elif op == 6:
        cells[ptr] += 1
        values[value_ptr] = (values[value_ptr] + 1) % 8
    elif op == 7:
        cells[ptr] -= 1
        values[value_ptr] = (values[value_ptr] + 7) % 8
    
    i += 1
