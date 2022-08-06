# дз стандартный вывод

def print_operation_table(operation, rows=9, columns=9):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i > 1 and j > 1:
                print(operation(i, j), end='\t')
            else:
                print(i * j, end='\t')
        print()
print_operation_table(lambda x, y: x * y, 5)
