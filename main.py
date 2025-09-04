import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        # First row
        self.create_button(btns_frame, "7", 1, 0)
        self.create_button(btns_frame, "8", 1, 1)
        self.create_button(btns_frame, "9", 1, 2)
        self.create_button(btns_frame, "/", 1, 3)

        # Second row
        self.create_button(btns_frame, "4", 2, 0)
        self.create_button(btns_frame, "5", 2, 1)
        self.create_button(btns_frame, "6", 2, 2)
        self.create_button(btns_frame, "*", 2, 3)

        # Third row
        self.create_button(btns_frame, "1", 3, 0)
        self.create_button(btns_frame, "2", 3, 1)
        self.create_button(btns_frame, "3", 3, 2)
        self.create_button(btns_frame, "-", 3, 3)

        # Fourth row
        self.create_button(btns_frame, "0", 4, 0)
        self.create_button(btns_frame, ".", 4, 1)
        self.create_button(btns_frame, "=", 4, 2, self.evaluate)
        self.create_button(btns_frame, "+", 4, 3)

        # Fifth row (scientific functions)
        self.create_button(btns_frame, "sin", 5, 0, lambda: self.scientific_function("sin"))
        self.create_button(btns_frame, "cos", 5, 1, lambda: self.scientific_function("cos"))
        self.create_button(btns_frame, "tan", 5, 2, lambda: self.scientific_function("tan"))
        self.create_button(btns_frame, "log", 5, 3, lambda: self.scientific_function("log"))

        # Sixth row (scientific functions)
        self.create_button(btns_frame, "sqrt", 6, 0, lambda: self.scientific_function("sqrt"))
        self.create_button(btns_frame, "pi", 6, 1, lambda: self.scientific_function("pi"))
        self.create_button(btns_frame, "exp", 6, 2, lambda: self.scientific_function("exp"))
        self.create_button(btns_frame, "C", 6, 3, self.clear)

    def create_button(self, frame, text, row, col, command=None):
        if not command:
            command = lambda: self.on_button_click(text)
        button = tk.Button(frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=command)
        button.grid(row=row, column=col, padx=1, pady=1)

    def on_button_click(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input, Make Sure you enter pattern after numbers!")
            self.expression = ""

    def scientific_function(self, func):
        try:
            if func == "sin":
                result = str(math.sin(math.radians(float(self.expression))))
            elif func == "cos":
                result = str(math.cos(math.radians(float(self.expression))))
            elif func == "tan":
                result = str(math.tan(math.radians(float(self.expression))))
            elif func == "log":
                result = str(math.log10(float(self.expression)))
            elif func == "sqrt":
                result = str(math.sqrt(float(self.expression)))
            elif func == "pi":
                result = str(math.pi)
            elif func == "exp":
                result = str(math.exp(float(self.expression)))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input, Make Sure you enter pattern after numbers!")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()