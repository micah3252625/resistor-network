import tkinter as tk
from tkinter import messagebox


# Resistor Class
class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

    def get_resistance(self):
        return self.resistance


# Resistor Network Class
class ResistorNetwork:
    def __init__(self):
        self.resistors = []

    def add_resistor(self, resistor):
        self.resistors.append(resistor)

    def clear_resistors(self):
        self.resistors = []

    def total_series_resistance(self):
        # Total resistance in series is just the sum of all resistors
        return sum([res.get_resistance() for res in self.resistors])

    def total_parallel_resistance(self):
        # Total resistance in parallel is 1/(1/R1 + 1/R2 + ...)
        try:
            total_inverse = sum([1 / res.get_resistance() for res in self.resistors])
            return 1 / total_inverse
        except ZeroDivisionError:
            messagebox.showerror("Error", "A resistor with 0 ohms is present. Invalid for parallel circuit.")
            return 0


# Resistance Calculator Application (with Tkinter GUI)
class ResistanceCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resistance Calculator")
        self.network = ResistorNetwork()

        # GUI Components
        self.title_label = tk.Label(root, text="Resistance Calculator", font=('Arial', 18, 'bold'))
        self.title_label.pack(pady=10)

        self.resistor_entry = tk.Entry(root, width=30)
        self.resistor_entry.pack(pady=5)
        self.add_button = tk.Button(root, text="Add Resistor", command=self.add_resistor)
        self.add_button.pack(pady=5)

        # Listbox to show added resistors
        self.resistor_listbox_label = tk.Label(root, text="Added Resistors (Ohms):")
        self.resistor_listbox_label.pack(pady=5)

        self.resistor_listbox = tk.Listbox(root, height=6, width=40)
        self.resistor_listbox.pack(pady=5)

        self.series_button = tk.Button(root, text="Calculate Series Resistance", command=self.calculate_series)
        self.series_button.pack(pady=5)

        self.parallel_button = tk.Button(root, text="Calculate Parallel Resistance", command=self.calculate_parallel)
        self.parallel_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Total Resistance: ", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear Resistors", command=self.clear_resistors)
        self.clear_button.pack(pady=5)

    # Add resistor to the network
    def add_resistor(self):
        try:
            resistance_value = float(self.resistor_entry.get())
            if resistance_value < 0:
                raise ValueError("Resistance cannot be negative.")
            resistor = Resistor(resistance_value)
            self.network.add_resistor(resistor)
            self.resistor_entry.delete(0, tk.END)

            # Update the listbox with the new resistor
            self.resistor_listbox.insert(tk.END, f"{resistance_value} ohms")
            messagebox.showinfo("Success", f"Resistor of {resistance_value} ohms added.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for resistance.")

    # Calculate total series resistance
    def calculate_series(self):
        total_resistance = self.network.total_series_resistance()
        self.result_label.config(text=f"Total Series Resistance: {total_resistance:.2f} ohms")

    # Calculate total parallel resistance
    def calculate_parallel(self):
        total_resistance = self.network.total_parallel_resistance()
        if total_resistance > 0:
            self.result_label.config(text=f"Total Parallel Resistance: {total_resistance:.2f} ohms")

    # Clear all resistors from the network
    def clear_resistors(self):
        self.network.clear_resistors()
        self.result_label.config(text="Total Resistance: ")
        self.resistor_listbox.delete(0, tk.END)  # Clear the listbox display
        messagebox.showinfo("Cleared", "All resistors have been cleared.")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ResistanceCalculatorApp(root)
    root.mainloop()
