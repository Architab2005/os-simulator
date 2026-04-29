from data.process import Process 
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for p in processes:
        if current_time < p.arrival_time: current_time = p.arrival_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        current_time = p.completion_time
    return processes

def sjf(processes):
    processes.sort(key=lambda x: x.arrival_time)
    n = len(processes)
    completed, ready_q = [], []
    curr, remaining = 0, processes[:]
    while len(completed) < n:
        for p in remaining[:]:
            if p.arrival_time <= curr:
                ready_q.append(p); remaining.remove(p)
        if ready_q:
            ready_q.sort(key=lambda x: x.burst_time)
            p = ready_q.pop(0)
            curr += p.burst_time
            p.completion_time = curr
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed.append(p)
        else: curr += 1
    return completed

def rr(processes, quantum):
    processes.sort(key=lambda x: x.arrival_time)
    curr, ready_q, completed, n = 0, [], [], len(processes)
    remaining = processes[:]
    while len(completed) < n:
        for p in remaining[:]:
            if p.arrival_time <= curr:
                ready_q.append(p); remaining.remove(p)
        if ready_q:
            p = ready_q.pop(0)
            exec_time = min(p.remaining_time, quantum)
            p.remaining_time -= exec_time
            curr += exec_time
            for p_new in remaining[:]:
                if p_new.arrival_time <= curr:
                    ready_q.append(p_new); remaining.remove(p_new)
            if p.remaining_time > 0: ready_q.append(p)
            else:
                p.completion_time = curr
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                completed.append(p)
        else: curr += 1
    return completed