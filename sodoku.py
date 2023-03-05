

class SodokuTable():

    def __init__(self, known_numbers):
        # known_numbers is a dictionary where key is a cell in the table
        self.table = {}
        for i in range(1, 82): # Building sodoku table
            if f'x{i}' in known_numbers.keys():
                self.table[f'x{i}'] = known_numbers[f'x{i}']
            else:
                self.table[f'x{i}'] = 'x'


    def print_table(self): #Prints the table to actually look more like a sodoku
        row = []
        for i in range(1, 82):
            if (i % 9 == 0 and i > 0):
                row.append(self.table[f'x{i}'])
                print(row)
                row.clear()
            else:
                row.append(self.table[f'x{i}'])


    def get_col(self, col):
        index = col + 1
        column = []
        for i in range(0,9):
            column.append(self.table[f'x{index + (i * 9)}'])
        return column

    def get_row(self, row):
        rows = []
        index = (row * 9) + 1
        for i in range(index, index + 9):
            rows.append(self.table[f'x{i}'])
        return rows




        


nums = {'x0' : '0', 'x1' : '1', 'x2' : '2', 'x3' : '3', 'x10' : '10', 'x11' : '20', 'x29' : '30'}

test = SodokuTable(nums)

test.print_table()

print(f'\n{test.get_row(1)}')






