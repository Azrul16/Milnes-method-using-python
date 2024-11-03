import tkinter as tk
from tkinter import messagebox
import milne_method

class NumericalMethodsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerical Methods Toolkit")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select a Problem to Solve:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.buttons = [
            ("Fluid Velocity", self.fluid_velocity_gui),
            ("Spacecraft Position", self.spacecraft_position_gui),
            ("Pollutant Concentration", self.pollutant_concentration_gui),
            ("Bacteria Population", self.bacteria_population_gui),
            ("Financial Asset", self.financial_asset_gui),
        ]

        for text, func in self.buttons:
            button = tk.Button(self.root, text=text, command=func, font=('Arial', 12))
            button.pack(pady=5)

    def fluid_velocity_gui(self):
        self.create_input_window("Fluid Velocity", self.solve_fluid_velocity)

    def spacecraft_position_gui(self):
        self.create_input_window("Spacecraft Position", self.solve_spacecraft_position)

    def pollutant_concentration_gui(self):
        self.create_input_window("Pollutant Concentration", self.solve_pollutant_concentration)

    def bacteria_population_gui(self):
        self.create_input_window("Bacteria Population", self.solve_bacteria_population)

    def financial_asset_gui(self):
        self.create_input_window("Financial Asset", self.solve_financial_asset)

    def create_input_window(self, title, solve_method):
        window = tk.Toplevel(self.root)
        window.title(title)
        
        tk.Label(window, text="Initial Values (comma-separated):").grid(row=0, column=0)
        entry_initial = tk.Entry(window)
        entry_initial.grid(row=0, column=1)
        
        tk.Label(window, text="Time Period:").grid(row=1, column=0)
        entry_t_end = tk.Entry(window)
        entry_t_end.grid(row=1, column=1)
        
        tk.Label(window, text="Step Size:").grid(row=2, column=0)
        entry_h = tk.Entry(window)
        entry_h.grid(row=2, column=1)
        
        result = tk.StringVar()
        tk.Label(window, textvariable=result).grid(row=4, columnspan=2, pady=10)
        
        tk.Button(window, text="Calculate", command=lambda: solve_method(entry_initial, entry_t_end, entry_h, result)).grid(row=3, columnspan=2, pady=10)
    
    def solve_fluid_velocity(self, entry_initial, entry_t_end, entry_h, result):
        try:
            initial_values = list(map(float, entry_initial.get().split(',')))
            t_end = float(entry_t_end.get())
            h = float(entry_h.get())
            t, y = milne_method.solve_fluid_velocity(initial_values, t_end, h)
            result.set(f"t: {t}\ny: {y}")
        except ValueError:
            result.set("Invalid input. Please enter numeric values.")
    
    def solve_spacecraft_position(self, entry_initial, entry_t_end, entry_h, result):
        try:
            initial_values = list(map(float, entry_initial.get().split(',')))
            t_end = float(entry_t_end.get())
            h = float(entry_h.get())
            t, y = milne_method.solve_spacecraft_position(initial_values, t_end, h)
            result.set(f"t: {t}\ny: {y}")
        except ValueError:
            result.set("Invalid input. Please enter numeric values.")
    
    def solve_pollutant_concentration(self, entry_initial, entry_t_end, entry_h, result):
        try:
            initial_values = list(map(float, entry_initial.get().split(',')))
            t_end = float(entry_t_end.get())
            h = float(entry_h.get())
            t, y = milne_method.solve_pollutant_concentration(initial_values, t_end, h)
            result.set(f"t: {t}\ny: {y}")
        except ValueError:
            result.set("Invalid input. Please enter numeric values.")
    
    def solve_bacteria_population(self, entry_initial, entry_t_end, entry_h, result):
        try:
            initial_values = list(map(float, entry_initial.get().split(',')))
            t_end = float(entry_t_end.get())
            h = float(entry_h.get())
            t, y = milne_method.solve_bacteria_population(initial_values, t_end, h)
            result.set(f"t: {t}\ny: {y}")
        except ValueError:
            result.set("Invalid input. Please enter numeric values.")
    
    def solve_financial_asset(self, entry_initial, entry_t_end, entry_h, result):
        try:
            initial_values = list(map(float, entry_initial.get().split(',')))
            t_end = float(entry_t_end.get())
            h = float(entry_h.get())
            t, y = milne_method.solve_financial_asset(initial_values, t_end, h)
            result.set(f"t: {t}\ny: {y}")
        except ValueError:
            result.set("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsApp(root)
    root.mainloop()
