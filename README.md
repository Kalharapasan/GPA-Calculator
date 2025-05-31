# 🎓 Advanced GPA Calculator (Python + Tkinter)

A simple yet powerful GPA Calculator built using **Python** and **Tkinter**, with dark mode support and data saving features.

---

## ✨ Features

- ✅ Add multiple courses with **grade and credit** inputs
- 🎯 Calculates GPA dynamically as you type
- 💾 **Save & Load** GPA data using JSON
- 🌙 Toggle between **Light & Dark Mode**
- ❌ Delete course rows individually
- 🧮 Grade-to-GPA conversion using standard scale

---

## 🧰 Technologies Used

- Python 3
- Tkinter (GUI)
- ttk.Combobox
- JSON for data persistence

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/28866f6c-4f0d-46fc-8ef1-ef58860f1edf)


---

## 🚀 How to Run

1. **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/gpa-calculator.git](https://github.com/Kalharapasan/GPA-Calculator.git)
    cd GPA-Calculator
    ```

2. **Run the Python file**:
    ```bash
    python GPA2.py
    ```

---

## 💾 Save File Format

All data is stored in a `gpa_data.json` file like this:

```json
[
  {"course": "Math", "grade": "A", "credits": "3"},
  {"course": "Science", "grade": "B+", "credits": "2"}
]
