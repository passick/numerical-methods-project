from tkinter import *
import solver

class App:

    def __init__(self, master):
        self.entries = [
                ("x_0"  , Entry()),
                ("y_0"  , Entry()),
                ("T"    , Entry()),
                ("rho_a", Entry()),
                ("rho_b", Entry()),
                ("S_c"  , Entry()),
                ("S_d"  , Entry()),
                ("z_e"  , Entry()),
                ("z_f"  , Entry()),
                ("beta" , Entry()) 
                ]
        current_row = 0
        for entry in self.entries:
            # Label(text=entry[0], width=15).grid(row=current_row, column=0)
            Label(text=entry[0], width=5).grid(row=current_row, column=1)
            entry[1].grid(row=current_row, column=2)
            entry[1].insert(0, "1")
            current_row += 1
        self.solve_button = Button(text='Solve', command=self.solve)
        self.solve_button.grid(row=current_row, column=2)
        self.plot = Label(width=80, height=30)
        self.plot.grid(row=0, column=0, rowspan=current_row)

    def solve(self):
        parameters = {}
        for entry in self.entries:
            try:
                parameters[entry[0]] = float(entry[1].get())
            except ValueError:
                return
        solver.solve(**parameters)

root = Tk()

app = App(root)

root.mainloop()
