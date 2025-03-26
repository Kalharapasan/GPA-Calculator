import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Grade to GPA mapping
grade_points = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.1,
    "D-": 1.0, "F": 0.0
}

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced GPA Calculator")
        self.root.geometry("500x500")
        self.root.config(bg="#f0f0f0")
        
        self.dark_mode = False
        self.entries = []
        self.load_data()
        
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="GPA Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Table Headers
        header_frame = tk.Frame(self.root, bg="#f0f0f0")
        header_frame.pack()
        tk.Label(header_frame, text="Course", font=("Arial", 12, "bold"), width=12, bg="#f0f0f0").grid(row=0, column=0)
        tk.Label(header_frame, text="Grade", font=("Arial", 12, "bold"), width=8, bg="#f0f0f0").grid(row=0, column=1)
        tk.Label(header_frame, text="Credits", font=("Arial", 12, "bold"), width=8, bg="#f0f0f0").grid(row=0, column=2)
        
        # Courses Container
        self.course_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.course_frame.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Course", command=self.add_course_row, bg="lightblue").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Save Data", command=self.save_data, bg="lightgreen").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Load Data", command=self.load_data, bg="orange").grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Toggle Dark Mode", command=self.toggle_theme, bg="gray").grid(row=0, column=3, padx=5)

        self.gpa_label = tk.Label(self.root, text="Your GPA: 0.00", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.gpa_label.pack(pady=10)

        # Add an initial course row
        self.add_course_row()

    def add_course_row(self, course="", grade="A", credits=""):
        row = len(self.entries)
        course_name = tk.Entry(self.course_frame, width=15)
        course_name.grid(row=row, column=0, padx=5, pady=2)
        course_name.insert(0, course)

        grade_var = tk.StringVar(value=grade)
        grade_dropdown = ttk.Combobox(self.course_frame, textvariable=grade_var, values=list(grade_points.keys()), width=5)
        grade_dropdown.grid(row=row, column=1, padx=5, pady=2)

        credits_entry = tk.Entry(self.course_frame, width=5)
        credits_entry.grid(row=row, column=2, padx=5, pady=2)
        credits_entry.insert(0, credits)

        delete_button = tk.Button(self.course_frame, text="X", command=lambda: self.remove_course_row(row), bg="red", fg="white")
        delete_button.grid(row=row, column=3, padx=5, pady=2)

        self.entries.append((course_name, grade_var, credits_entry, delete_button))
        grade_var.trace("w", lambda *args: self.calculate_gpa())
        credits_entry.bind("<KeyRelease>", lambda event: self.calculate_gpa())

    def remove_course_row(self, index):
        # Remove row from UI and list
        self.entries[index][0].destroy()
        self.entries[index][1].set("")  # Reset dropdown
        self.entries[index][2].destroy()
        self.entries[index][3].destroy()
        self.entries.pop(index)
        self.calculate_gpa()

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0

        for course_name, grade_var, credits_entry, _ in self.entries:
            grade = grade_var.get()
            try:
                credits = float(credits_entry.get()) if credits_entry.get() else 0
            except ValueError:
                return  # Ignore invalid input

            total_credits += credits
            total_points += grade_points.get(grade, 0) * credits

        if total_credits == 0:
            self.gpa_label.config(text="Your GPA: 0.00")
            return

        gpa = total_points / total_credits
        self.gpa_label.config(text=f"Your GPA: {gpa:.2f}")

    def save_data(self):
        data = []
        for course_name, grade_var, credits_entry, _ in self.entries:
            data.append({"course": course_name.get(), "grade": grade_var.get(), "credits": credits_entry.get()})

        with open("gpa_data.json", "w") as file:
            json.dump(data, file)
        messagebox.showinfo("Saved", "Your GPA data has been saved.")

    def load_data(self):
        if os.path.exists("gpa_data.json"):
            with open("gpa_data.json", "r") as file:
                data = json.load(file)

            # Clear existing entries
            for _, _, _, delete_button in self.entries:
                delete_button.invoke()  # Simulate delete button click

            # Load saved data
            for item in data:
                self.add_course_row(item["course"], item["grade"], item["credits"])
            
            self.calculate_gpa()
        else:
            messagebox.showwarning("No Data", "No saved GPA data found.")

    def toggle_theme(self):
        if self.dark_mode:
            self.root.config(bg="#f0f0f0")
            self.course_frame.config(bg="#f0f0f0")
            self.gpa_label.config(bg="#f0f0f0")
            self.dark_mode = False
        else:
            self.root.config(bg="#2b2b2b")
            self.course_frame.config(bg="#2b2b2b")
            self.gpa_label.config(bg="#2b2b2b", fg="white")
            self.dark_mode = True

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()
