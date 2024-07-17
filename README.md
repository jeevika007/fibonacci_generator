# Fibonacci Generator GUI

This project is a simple GUI application for generating Fibonacci numbers using the `tkinter` library in Python. Each click of the "Generate Next" button will display the next Fibonacci number in the sequence.

## Features

- Generates Fibonacci numbers sequentially.
- Simple and user-friendly GUI.

## Requirements

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fibonacci-generator-gui.git
    cd fibonacci-generator-gui
    ```

2. **Verify `tkinter` installation**:
    `tkinter` usually comes pre-installed with Python. You can verify its installation by running:
    ```bash
    python -m tkinter
    ```

## Usage

1. **Save the code**: Copy the following code into a file named `fibonacci_gui.py`.

    ```python
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
    ```

2. **Run the script**:
    ```bash
    python fibonacci_gui.py
    ```

3. **Using the GUI**:
    - Click the "Generate Next" button to display the next Fibonacci number.

## Project Structure

- `fibonacci_gui.py`: The main script that contains the Fibonacci generator function and the `tkinter` GUI implementation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Acknowledgements

- Inspired by the simplicity and efficiency of Python's `tkinter` library.
- Fibonacci sequence definition: Each number is the sum of the two preceding ones, usually starting with 0 and 1.
