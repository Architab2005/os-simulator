# OS Simulator

A Python-based Operating System scheduling algorithm simulator. This project provides a graphical user interface (GUI) to simulate and visualize how processes are managed using core operating system scheduling strategies.

## Features
- **Scheduling Algorithms**:
  - **FCFS** (First-Come, First-Served)
  - **SJF** (Shortest Job First)
  - **Round Robin** (RR)
- **Graphical Interface**: Built with `tkinter`, featuring an interactive process queue management system.
- **Results Tracking**: Instant calculation of Waiting Time (WT) and Turnaround Time (TAT) for each process.

## Project Structure
```text
os_simulator\
    ├── __init__.py
    ├── main.py
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── .vscode\
    │   └── settings.json
    ├── data\
    │   ├── __init__.py
    │   └── process.py
    ├── logic\
    │   ├── __init__.py
    │   └── scheduler.py
    └── gui\
        ├── __init__.py
        └── app.py
```

### Why `.vscode/settings.json`?
This file is included to configure the **Pylance** language server in Visual Studio Code. Because this project is structured as a Python package, the absolute imports used in the code can trigger "Missing Import" warnings. The settings file adds the current directory to the search path, ensuring that your IDE correctly resolves all module imports without requiring manual configuration.

## Setup

1. Run the application :
   ```bash
  python main.py
   ```

## Developed by
**Archita B** | B.TECH CSE'26