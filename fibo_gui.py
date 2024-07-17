import tkinter as tk

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Generator")
        
        self.label = tk.Label(root, text="Fibonacci Generator", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.button = tk.Button(root, text="Generate Next", command=self.generate_next)
        self.button.pack(pady=10)
        
        self.output_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.output_label.pack(pady=10)
        
        self.fib_gen = fibonacci_generator()
    
    def generate_next(self):
        next_fib = next(self.fib_gen)
        self.output_label.config(text=str(next_fib))

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()
