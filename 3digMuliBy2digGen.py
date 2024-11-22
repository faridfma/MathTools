import tkinter as tk
from tkinter import filedialog, messagebox
import random

class MultiplicationMathGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Math Problem Generator: 3 Digits multiplied by 2 Digits")
        
        # Set up window size
        self.root.geometry("600x250")

        # Add a label for instructions
        self.instruction_label = tk.Label(self.root, text="Click 'Generate' and save multiplication problems.", font=("Arial", 14))
        self.instruction_label.pack(pady=20)

        # Add a 'Generate' button
        self.generate_button = tk.Button(self.root, text="Generate and Save Problems", font=("Arial", 12), command=self.generate_and_save_problems)
        self.generate_button.pack(pady=10)

    def generate_and_save_problems(self):
        """Generates random multiplication problems and saves them to a text file."""
        
        # Generate 48 multiplication problems (16 lines with 3 problems each)
        generated_problems = []
        solutions = []  # List to store the solutions
        problem_counter = 1  # Initialize the problem counter
        
        for _ in range(16):  # 16 lines of 3 problems each
            # Generate three unique problems in a row
            multiplicand1 = random.randint(100, 999)
            multiplier1 = random.randint(10, 99)
            product1 = multiplicand1 * multiplier1
            
            multiplicand2 = random.randint(100, 999)
            multiplier2 = random.randint(10, 99)
            product2 = multiplicand2 * multiplier2
            
            multiplicand3 = random.randint(100, 999)
            multiplier3 = random.randint(10, 99)
            product3 = multiplicand3 * multiplier3
            
            # Format the problem set for the three problems
            problem_numbers_line = f"({problem_counter})".rjust(6) + f"({problem_counter+1})".rjust(30) + f"({problem_counter+2})".rjust(30)
            multiplicand_line = f"{multiplicand1}".rjust(13) + f"{multiplicand2}".rjust(31) + f"{multiplicand3}".rjust(29)
            # Corrected multiplier_line without x_line, as it's unnecessary now
            multiplier_line = f"x {multiplier1}".rjust(13) + f"x {multiplier2}".rjust(31) + f"x {multiplier3}".rjust(29)
            
            # Store the solution for the three problems
            solutions.append(f"({problem_counter}) {product1}")
            solutions.append(f"({problem_counter+1}) {product2}")
            solutions.append(f"({problem_counter+2}) {product3}")
            
            problem_counter += 3  # Increment by 3 for each new problem

            # Add the result line with underscores after the multiplication
            underline = "______________".rjust(24) + " " + "______________".rjust(30) + " " + "______________".rjust(28)
            
            # Add the formatted problems and the underline to the list
            generated_problems.append((
                problem_numbers_line, multiplicand_line, multiplier_line, underline
            ))

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
            file.write("Math Multiplication Problems\n\n\n\n")

            # Loop through the generated problems and add them to the text file
            for problem_set in generated_problems:
                # Unpack the problem set into individual components
                problem_numbers_line, multiplicand_line, multiplier_line, underline = problem_set

                # Write the three unique problems for this row
                file.write(f"{problem_numbers_line}\n")
                file.write(f"{multiplicand_line}\n")
                file.write(f"{multiplier_line}\n")
                
                # Add the result line with underscores
                file.write(f"{underline}\n")
               
                # Add space between each problem set
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets
                file.write("\n")  # Add space between sets

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
app = MultiplicationMathGUI(root)

# Run the application
root.mainloop()
