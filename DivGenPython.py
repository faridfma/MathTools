import tkinter as tk
from tkinter import filedialog, messagebox
import random

class DivisionMathGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Division Math Problem Generator: 3 Digits divided by 2 Digits ")
        
        # Set up window size
        self.root.geometry("400x200")

        # Add a label for instructions
        self.instruction_label = tk.Label(self.root, text="Click 'Generate' and save division problems.", font=("Arial", 14))
        self.instruction_label.pack(pady=20)

        # Add a 'Generate' button
        self.generate_button = tk.Button(self.root, text="Generate and Save Problems", font=("Arial", 12), command=self.generate_and_save_problems)
        self.generate_button.pack(pady=10)

    def generate_and_save_problems(self):
        """Generates random division problems and saves them to a text file."""
        
        # Generate 48 division problems (16 lines with 3 problems each)
        generated_problems = []
        solutions = []  # List to store the solutions
        problem_counter = 1  # Initialize the problem counter
        
        for _ in range(16):  # 16 lines of 3 problems each
            problems = []
            for i in range(3):  # 3 problems per line
                # Random divisors and dividends
                divisor = random.randint(10, 99)
                dividend = random.randint(100, 999)
                problems.append(f"{divisor}){dividend}")  # Format each problem
                
                # Calculate the quotient and remainder
                quotient = dividend // divisor
                remainder = dividend % divisor
                
                # Store the solution as (Problem Number) Quotient R Remainder
                solution = f"({problem_counter}) {quotient} R {remainder}"
                solutions.append(solution)
              
                # Increment the problem counter for the next problem
                problem_counter += 1  # Increment by 1 for each new problem
                
            # Create the first line with problem numbers
            problem_numbers_line = f"({problem_counter-3})".rjust(3) + f"({problem_counter-2})".rjust(33) + f"({problem_counter-1})".rjust(32)
            
            # Create the second line with division lines
            division_line = " " * 8 + "______________" + " " * 20 + "______________" + " " * 18 + "______________"
            
            # Create the third line with divisor)dividend formatted problems
            problem_line = f"{problems[0]}".rjust(12) + f"{problems[1]}".rjust(34) + f"{problems[2]}".rjust(32)

            # Add formatted lines to the list
            generated_problems.append((problem_numbers_line, division_line, problem_line))

        # Ask the user for the file location and name
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save as")
        
        if not file_path:
            messagebox.showinfo("Cancel", "File saving was canceled.")  # If canceled, show message and return
            return

        # Open the file for writing
        with open(file_path, 'w') as file:
            # Write the header
            file.write("Math Division Problems\n\n\n\n")

            # Loop through the generated problems and add them to the text file
            for problem_numbers_line, division_line, problem_line in generated_problems:
                file.write(f"{problem_numbers_line}\n")
                file.write(f"{division_line}\n")
                file.write(f"{problem_line}\n")
                
                # Add space between each problem set
                file.write("\n")  # Add space
                file.write("\n")  # Add more space
                file.write("\n")  # Add additional space
                file.write("\n")  # Add even more space
                file.write("\n")  # Add more space
                file.write("\n")  # Add additional space
                file.write("\n")  # Add even more space

            # Add a section for solutions at the end
            file.write("\nSolutions:\n\n")
            for solution in solutions:
                file.write(f"{solution}\n")

            # Add space between each solution
            file.write("\n")  # Add space
            file.write("\n")  # Add more space
            file.write("\n")  # Add additional space

        # Show success message
        messagebox.showinfo("Success", f"Math problems have been saved to {file_path}")

# Create the main window (root)
root = tk.Tk()

# Create an instance of the GUI class
app = DivisionMathGUI(root)

# Run the application
root.mainloop()
