import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Projekt na info (Kuba Sobstyl)")
        master.resizable(False, False)  # uniemożliwienie zmiany rozmiaru okna

        # Utwórz pole tekstowe dla wyświetlania wyniku
        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Helvetica", 24), anchor="e", bg="black", fg="white")
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="news")

        # Utwórz przyciski dla cyfr i operatorów
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 1), ("C", 4, 0), ("=", 4, 2), ("/", 4, 3),
        ]

        for label, row, col in buttons:
            if label in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                button = tk.Button(master, text=label, font=("Helvetica", 20), width=5, height=2, bg="black", fg="white", command=lambda label=label: self.button_click(label))
            else:
                button = tk.Button(master, text=label, font=("Helvetica", 20), width=5, height=2, bg="orange", command=lambda label=label: self.button_click(label))
            if label == '=':
                button.configure(bg='orange')
            button.grid(row=row, column=col)

    def button_click(self, label):
        if label == "C":
            self.result_var.set("")
        elif label == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("ERROR")
        else:
            self.result_var.set(self.result_var.get() + label)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
