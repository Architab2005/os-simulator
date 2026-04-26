import tkinter as tk
from os_simulator.gui.app import App

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the initial size to 600x400 pixels
    root.geometry("600x400")
    
    # Optionally, set a minimum size so it doesn't shrink too small
    root.minsize(400, 300)
    
    App(root)
    root.mainloop()