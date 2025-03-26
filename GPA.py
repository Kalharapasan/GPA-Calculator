import tkinter as tk
from tkinter import messagebox

# Grade to GPA mapping
grade_points = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.1,
    "D-": 1.0, "F": 0.0
}

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")

        self.entries = []
        
        tk.Label(root, text="Course", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Grade", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(root, text="Credits", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)

        self.add_course_row()
        
        tk.Button(root, text="Add Course", command=self.add_course_row, bg="lightblue").grid(row=99, column=0, pady=10)
        tk.Button(root, text="Calculate GPA", command=self.calculate_gpa, bg="lightgreen").grid(row=99, column=1, pady=10)
        tk.Button(root, text="Clear", command=self.clear_entries, bg="lightcoral").grid(row=99, column=2, pady=10)

    def add_course_row(self):
        row = len(self.entries) + 1
        course_name = tk.Entry(self.root)
        course_name.grid(row=row, column=0, padx=5, pady=2)

        grade_var = tk.StringVar()
        grade_dropdown = tk.OptionMenu(self.root, grade_var, *grade_points.keys())
        grade_dropdown.grid(row=row, column=1, padx=5, pady=2)
        grade_var.set("A")  # Default value

        credits_entry = tk.Entry(self.root)
        credits_entry.grid(row=row, column=2, padx=5, pady=2)

        self.entries.append((course_name, grade_var, credits_entry))

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0

        for course_name, grade_var, credits_entry in self.entries:
            grade = grade_var.get()
            try:
                credits = float(credits_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter valid credit hours.")
                return

            if credits < 0:
                messagebox.showerror("Error", "Credit hours cannot be negative.")
                return

            total_credits += credits
            total_points += grade_points[grade] * credits

        if total_credits == 0:
            messagebox.showerror("Error", "Total credits cannot be zero.")
            return

        gpa = total_points / total_credits
        messagebox.showinfo("GPA Result", f"Your GPA is: {gpa:.2f}")

    def clear_entries(self):
        for course_name, grade_var, credits_entry in self.entries:
            course_name.delete(0, tk.END)
            grade_var.set("A")
            credits_entry.delete(0, tk.END)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()
