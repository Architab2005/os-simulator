import sys
import os
# Add current directory to Python path for direct execution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from gui.app import App  # Now uses relative import

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the initial size to 600x400 pixels
    root.geometry("600x400")
    
    # Optionally, set a minimum size so it doesn't shrink too small
    root.minsize(400, 300)
    
    App(root)
    root.mainloop()