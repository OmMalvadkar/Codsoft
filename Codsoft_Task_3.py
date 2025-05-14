import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    complexity = complexity_var.get()

    # Validate input
    if not length.isdigit():
        result_label.config(text="Please enter a valid number for length.")
        return

    length = int(length)
    if length < 5 or length > 50:
        result_label.config(text="Length must be between 5 and 50.")
        return

    # Choose character set
    if complexity == "weak":
        characters = string.ascii_letters
    elif complexity == "moderate":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        result_label.config(text="Please select a password complexity.")
        return

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Password: {password}")

# Set up GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.config(bg="azure")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), bg="whitesmoke").pack(pady=10)

# Length input
length_var = tk.StringVar()
tk.Label(root, text="Enter Password Length:", bg="lightblue", font=("Arial", 15)).pack()
tk.Entry(root, textvariable=length_var, font=("Arial", 15), justify='center').pack(pady=8)

# Complexity selection
complexity_var = tk.StringVar(value="")

tk.Label(root, text="Select Password Complexity:", bg="lightblue",font=("Arial", 15)).pack()

tk.Radiobutton(root, text="Weak", variable=complexity_var, value="weak", bg="lightblue", font=("Arial", 15)).pack()
tk.Radiobutton(root, text="Moderate", variable=complexity_var, value="moderate", bg="lightblue", font=("Arial", 15)).pack()
tk.Radiobutton(root, text="Strong", variable=complexity_var, value="strong", bg="lightblue", font=("Arial", 15)).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="cyan", fg="white", font=("Arial", 17)).pack(pady=15)

# Result label
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 15))
result_label.pack(pady=15)

# Run the GUI loop
root.mainloop()
