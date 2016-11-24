from tkinter import *
import solver

class App:

    def __init__(self, master):
        self.entries = [
                ("x_0"       , Entry()),
                ("y_0"       , Entry()),
                ("T"         , Entry()),
                ("rho_a"     , Entry()),
                ("rho_b"     , Entry()),
                ("S_c"       , Entry()),
                ("S_d"       , Entry()),
                ("z_e"       , Entry()),
                ("z_f"       , Entry()),
                ("beta"      , Entry()),
                ("beta_left" , Entry()),
                ("beta_right", Entry())
                ]
        current_row = 0
        for entry in self.entries:
            # Label(text=entry[0], width=15).grid(row=current_row, column=0)
            Label(text=entry[0], width=7).grid(row=current_row, column=1)
            entry[1].grid(row=current_row, column=2)
            entry[1].insert(0, "1")
            current_row += 1
            if entry[0] == 'beta':
                self.solve_button = Button(text='Solve', command=self.solve)
                self.solve_button.grid(row=current_row, column=2)
                current_row += 1
        self.automatic_solve = Button(text='Solve automatically',
                command=lambda : self.solve(automatic=True))
        self.automatic_solve.grid(row=current_row, column=2)
        self.plot = Label(width=80, height=30)
        self.plot.grid(row=0, column=0, rowspan=current_row)

    def solve(self, automatic=False):
        parameters = {}
        for entry in self.entries:
            try:
                parameters[entry[0]] = float(entry[1].get())
            except ValueError:
                if entry[0] == 'beta' and automatic:
                    continue
                if (entry[0] == 'beta_left' or entry[0] == 'beta_right') \
                        and not automatic:
                    continue
                return
        solver.solve(**parameters)

root = Tk()

app = App(root)

root.mainloop()
