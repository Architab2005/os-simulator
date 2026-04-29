import tkinter as tk
from tkinter import messagebox, ttk
from data.process import Process      
from logic.scheduler import fcfs, sjf, rr  

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Simulator")
        self.procs = []
        
        # --- Input Section ---
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="PID").grid(row=0, column=0)
        tk.Label(input_frame, text="Arr").grid(row=0, column=1)
        tk.Label(input_frame, text="Burst").grid(row=0, column=2)
        
        self.e_p = tk.Entry(input_frame, width=5)
        self.e_a = tk.Entry(input_frame, width=5)
        self.e_b = tk.Entry(input_frame, width=5)
        
        self.e_p.grid(row=1, column=0); self.e_a.grid(row=1, column=1); self.e_b.grid(row=1, column=2)
        
        tk.Button(input_frame, text="Add Process", command=self.add).grid(row=1, column=3, padx=10)
        
        # --- List Display Section ---
        tk.Label(root, text="Added Processes:").pack()
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)
        
        # --- Simulation Buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Run FCFS", command=lambda: self.run('fcfs')).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Run SJF", command=lambda: self.run('sjf')).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Run RR", command=lambda: self.run('rr')).pack(side=tk.LEFT, padx=5)
        
        # --- Footer ---
        footer = tk.Label(root, text="Developed by : Archita B | B.TECH CSE'26", 
                          font=("Arial", 10, "italic"), fg="grey")
        footer.pack(side=tk.BOTTOM, pady=10)

    def add(self):
        try:
            pid = self.e_p.get()
            arr = int(self.e_a.get())
            burst = int(self.e_b.get())
            p = Process(pid, arr, burst)
            self.procs.append(p)
            
            # Update the list on the screen
            self.listbox.insert(tk.END, f"PID: {pid} | Arrival: {arr} | Burst: {burst}")
            
            # Clear entries
            self.e_p.delete(0, tk.END); self.e_a.delete(0, tk.END); self.e_b.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers")

    def run(self, alg):
        if not self.procs:
            messagebox.showwarning("Warning", "Add processes first")
            return
            
        if alg == 'fcfs': results = fcfs(self.procs[:])
        elif alg == 'sjf': results = sjf(self.procs[:])
        else: results = rr(self.procs[:], 2)
        
        msg = "\n".join([f"P{p.pid}: WT={p.waiting_time}, TAT={p.turnaround_time}" for p in results])
        messagebox.showinfo("Simulation Results", msg)