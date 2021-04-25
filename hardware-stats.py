#!/usr/bin/env python3
import os
from time import sleep
import psutil
from tabulate import tabulate

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def print_cpu_info():
    print("="*20, "CPU Information", "="*20)
    table = []
    table.append(["Cores:", f"{psutil.cpu_count(logical=False)} / {psutil.cpu_count(logical=True)}"])
    cpufreq = psutil.cpu_freq()
    table.append(["Frequency:", f"{cpufreq.max:.2f}Mhz {cpufreq.min:.2f}Mhz {cpufreq.current:.2f}Mhz"])
    table.append(["Usage:", f"{psutil.cpu_percent()}%"])
    if not os.name in ("nt", "dos"):
        cputemp = psutil.sensors_temperatures()
        table.append(["Temperature:", f"{cputemp['cpu_thermal'][0].current}°C"])
    print(tabulate(table))
    print("")

def print_memory_info():
    print("="*20, "Memory Information", "="*20)
    table = []
    svmem = psutil.virtual_memory()
    table.append(["Virtual: ", get_size(svmem.total), get_size(svmem.used), get_size(svmem.available), f"{svmem.percent}%"])
    swap = psutil.swap_memory()
    table.append(["Swap:", get_size(swap.total), get_size(swap.used), get_size(swap.free), f"{swap.percent}%"])
    print(tabulate(table, headers=("Type", "Total", "Used", "Free", "Percentage")))
    print("")


if __name__ == "__main__":
    while True:
        clear_console()
        print_cpu_info()
        print_memory_info()
        sleep(1)
