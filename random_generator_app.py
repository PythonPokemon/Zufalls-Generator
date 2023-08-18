import tkinter as tk
import random
import string

class RandomGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zufallsgenerator")

        self.result_label = tk.Label(self.root, text="", wraplength=300)
        self.result_label.pack(padx=10, pady=5)

        self.generate_button = tk.Button(self.root, text="Generieren", command=self.generate)
        self.generate_button.pack(padx=10, pady=5)

        self.type_var = tk.StringVar()
        self.type_var.set("Zahlen")
        self.type_menu = tk.OptionMenu(self.root, self.type_var, "Zahlen", "Buchstaben", "Passwort")
        self.type_menu.pack(padx=10, pady=5)

        self.length_label = tk.Label(self.root, text="Länge:")
        self.length_label.pack(padx=10, pady=5)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack(padx=10, pady=5)

    def generate(self):
        generator_type = self.type_var.get()
        length = int(self.length_entry.get())

        if generator_type == "Zahlen":
            result = ''.join(random.choice(string.digits) for _ in range(length))
        elif generator_type == "Buchstaben":
            result = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        elif generator_type == "Passwort":
            chars = string.ascii_letters + string.digits + string.punctuation
            result = ''.join(random.choice(chars) for _ in range(length))
        
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomGeneratorApp(root)
    root.mainloop()
