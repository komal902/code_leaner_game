import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Code Learning Game")
root.geometry("500x400")

problems = [
    {
        "question": "Write a Python function to return the sum of two numbers.",
        "hint": "Use the '+' operator to add the numbers.",
        "function_name": "sum_two_numbers",
        "test_case": (3, 5),
        "expected_output": 8
    },
    {
        "question": "Write a Python function to check if a number is even.",
        "hint": "Use the '%' operator to check divisibility.",
        "function_name": "is_even",
        "test_case": (4,),
        "expected_output": True
    }
]
curr_problem = 0

def check_solution():
    try:
        user_code = code_entry.get("1.0", tk.END)
        local_env = {}
        exec(user_code, {}, local_env)

        curr = problems[curr_problem]
        user_function = local_env.get(current['function_name'])
        
        if user_function is None:
            raise NameError(f"Function '{curr['function_name']}' is not defined.")
        
        result = user_function(*current['test_case'])
        if result == curr['expected_output']:
            messagebox.showinfo("Success!", "Correct solution!")
        else:
            messagebox.showerror("Incorrect", f"Expected {curr ['expected_output']}, but got {result}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def load_problem():
    global curr_problem
    problem = problems[curr_problem]
    question_label.config(text=f"Problem {curr_problem + 1}: {problem['question']}")
    hint_label.config(text=f"HINT: {problem['hint']}")
    code_entry.delete("1.0", tk.END)


def next_problem():
    global curr_problem
    if curr_problem < len(problems) - 1:
        curr_problem += 1
        load_problem()
    else:
        messagebox.showinfo("Done", "You solved all the problems!")

question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
question_label.pack(pady=10)
hint_label = tk.Label(root, text="", wraplength=400, font=("Arial", 10), fg="gray")
hint_label.pack(pady=5)
code_label = tk.Label(root, text="Enter your Python code:")
code_label.pack(pady=5)
code_entry = tk.Text(root, height=10, width=50)
code_entry.pack(pady=10)
check_button = tk.Button(root, text="Check Solution", command=check_solution)
check_button.pack(pady=5)
next_button = tk.Button(root, text="Next Problem", command=next_problem)
next_button.pack(pady=5)

load_problem()
root.mainloop()
 