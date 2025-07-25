import tkinter as tk

def on_click(char):
    if char == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "エラー")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("シンプル電卓")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+",
    "="
]

row = 1
col = 0
for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, font=("Arial", 18), width=5, height=2,
                    command=lambda char=btn_text: on_click(char))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
