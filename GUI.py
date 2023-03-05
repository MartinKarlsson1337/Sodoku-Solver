from tkinter import *
from tkinter import ttk
import sodoku as sod

class SodokuWindow():
    def __init__(self):
        self.puzzle = sod.SodokuTable(sod.nums)
        self.table = self.puzzle.table
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

    def show(self):
        for i in range(1, 10):
            for j in range(1,10):
                ttk.Label(self.frm, text=self.puzzle.table[f'x{i*j}'], font={'24 bold'}).grid(column=j-1, row=i-1)

        btn = Button(text="Solve!", command=self.solve_update).grid(column=0, row=10)
        self.root.mainloop()

    def solve_update(self):
        sol = self.puzzle.solve()
        for i in range(1, 10):
            for j in range(1, 10):
                ttk.Label(self.frm, text=sol.table[f'x{i*j}'], font={'24 bold'}).grid(column=j-1, row=i-1)

# class MainMenu():
#     def __init__(self):
#         self.root = Tk()
#         self.frm = ttk.Frame(self.root, padding=10)
#         self.frm.grid()
#         self.sodoku_window = SodokuWindow()
#         self.button = ttk.Button(text="Open solver", command=self.show_sodoku_window).grid(column=1, row=0)

#     def show(self):
#         self.root.mainloop()

#     def show_sodoku_window(self):
#         self.root.destroy()
#         self.sodoku_window.show()

# MainMenu().show()

SodokuWindow().show()


