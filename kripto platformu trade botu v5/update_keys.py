import tkinter as tk
from tkinter import messagebox
import os

# Save API keys to keys.py
def save_keys(api_key, api_secret):
    if not api_key or not api_secret:
        messagebox.showerror("Error", "API Key and Secret must not be empty")
        return

    try:
        file_path = 'keys.py'
        with open(file_path, 'w') as file:
            file.write(f"api_key = '{api_key}'\n")
            file.write(f"api_secret = '{api_secret}'\n")

        if os.path.exists(file_path):
            messagebox.showinfo("Success", "API keys have been saved to keys.py")
        else:
            messagebox.showerror("Error", "Failed to save API keys. File does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save API keys: {e}")

def main():
    root = tk.Tk()
    root.title("API Key Input")

    api_key_label = tk.Label(root, text="API Key:")
    api_key_label.pack(pady=(10, 0))
    api_key_entry = tk.Entry(root, width=50)
    api_key_entry.pack(pady=(0, 10))

    api_secret_label = tk.Label(root, text="API Secret:")
    api_secret_label.pack(pady=(10, 0))
    api_secret_entry = tk.Entry(root, width=50, show='*')
    api_secret_entry.pack(pady=(0, 10))

    save_button = tk.Button(root, text="Save API Keys", command=lambda: save_keys(api_key_entry.get(), api_secret_entry.get()))
    save_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
