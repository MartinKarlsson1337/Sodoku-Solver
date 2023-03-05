import csp
import tkinter

class SodokuTable():

    def __init__(self, known_numbers):
        # known_numbers is a dictionary where key is a cell in the table
        self.table = {}
        self.vars = []
        self.domains = {}
        self.neighbours = {}
        for i in range(1, 82): # Building sodoku table
            if f'x{i}' in known_numbers.keys():
                self.table[f'x{i}'] = known_numbers[f'x{i}']
                self.domains[f'x{i}'] = [known_numbers[f'x{i}']]
            else:
                self.table[f'x{i}'] = 'x'
                self.domains[f'x{i}'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            self.vars.append(f'x{i}')
            self.neighbours[f'x{i}'] = []
        self.create_constraint_graph()


    def print_table(self): #Prints the table to actually look more like a sodoku
        row = []
        for i in range(1, 82):
            if (i % 9 == 0 and i > 0):
                row.append(self.table[f'x{i}'])
                print(row)
                row.clear()
            else:
                row.append(self.table[f'x{i}'])

    def print_table_vars(self):
        row = []
        for i in range(1, 82):
            if (i % 9 == 0 and i > 0):
                row.append(f'x{i}')
                print(row)
                row.clear()
            else:
                row.append(f'x{i}')

    def constraint(self, A, a, B, b):
        if a == b: 
            return False
        else: 
            return True

    def get_col(self, col): # Returns a column och the table as a list
        index = col + 1
        column = []
        for i in range(0,9):
            column.append(f'x{index + (i * 9)}')
        return column

    def get_row(self, row): # return a row from the table as a list
        rows = []
        index = (row * 9) + 1
        for i in range(index, index + 9):
            rows.append(f'x{i}')
        return rows

    def get_block(self, x, y): # returns a block from the table as a 2-D array
        block = [[], [], []]
        for i in range(0, 3):
            col = self.get_col(i + (x * 3))
            for j in range(0,3):
                block[i] = [col[j + (y * 3)], col[j + (y * 3) - 1], col[j + (y * 3) - 2]]
        return block    

    def get_col_of_var(self, var_name):
        for i in range(0, 9):
            col = self.get_col(i)
            if var_name in col:
                return i

    def get_row_of_var(self, var_name):
        for i in range(0, 9):
            row = self.get_row(i)
            if var_name in row:
                return i
            
    def get_coordinates(self, var_name):
        return (self.get_col_of_var(var_name), self.get_row_of_var(var_name))

    def create_constraint_graph(self):
        for i in range(0,3): # All cells in the same block are neighbours
            for j in range(0,3):
                block = self.get_block(i, j)
                for col in block:
                    for var in col:
                        self.neighbours[var].extend(block[0])
                        self.neighbours[var].extend(block[1])
                        self.neighbours[var].extend(block[2])

        for i in range(0,9): # All cells in the same column are neighbours
            cols = self.get_col(i)
            for var in cols:
                self.neighbours[var].extend(cols)

        for i in range(0,9): # All cells in the same row are neighbours
            rows = self.get_row(i)
            for var in rows:
                self.neighbours[var].extend(rows)

        for var in self.neighbours: # Remove all duplicates
            no_dupes = []
            for neighbour in self.neighbours[var]:
                if neighbour not in no_dupes and neighbour != var:
                    no_dupes.append(neighbour)
            self.neighbours[var] = no_dupes
                
    def solve(self): # Solves CSP and returns it as a SodokuTable
        problem = csp.CSP(self.vars, self.domains, self.neighbours, self.constraint)
        sol = csp.backtracking_search(problem, inference=csp.forward_checking, )
        return SodokuTable(sol)


# Test data
nums = {'x1' : '9', 'x3' : '1', 'x5': '6', 'x8' : '4',
        'x10' : '2', 'x13' : '1', 'x14' : '4', 'x15' : '9', 'x18': '3',
        'x19' : '3', 'x21' : '6', 'x22' : '5', 'x27' : '1',
        'x30' : '4', 'x32' : '1', 'x35' : '6',
        'x37' : '1', 'x38' : '9', 'x40' : '2', 'x41' : '7', 'x45' : '4',
        'x47' : '3', 'x51' : '8', 'x53' : '2', 'x54' : '9',
        'x55' : '4', 'x57' : '2', 'x58' : '7', 'x61' : '8', 'x63' : '5',
        'x64' : '5', 'x67' : '8', 'x69' : '4', 'x71' : '3',
        'x75' : '3', 'x77' : '9', 'x78' : '5', 'x80' : '1', 'x81' : '2'}







