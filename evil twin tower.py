import tkinter as tk
from tkinter import ttk
import subprocess
import time

def create_hotspot():
    ssid = ssid_entry.get()
    password = password_entry.get()
    command = f'netsh wlan set hostednetwork mode=allow ssid={ssid} key={password}'
    subprocess.run(command, shell=True)
    command = 'netsh wlan start hostednetwork'
    subprocess.run(command, shell=True)
    update_device_list()

def update_device_list():
    command = 'netsh wlan show hostednetwork'
    output = subprocess.check_output(command, shell=True).decode()
    device_list.delete(0, tk.END)
    for line in output.split('\n'):
        if 'Number of clients' in line:
            num_clients = int(line.split(':')[-1].strip())
            device_list.insert(tk.END, f'Number of connected devices: {num_clients}')
    root.after(10000, update_device_list)

root = tk.Tk()
root.title('Wi-Fi Hotspot Creator')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

ssid_label = ttk.Label(mainframe, text='Network Name (SSID):')
ssid_label.grid(column=0, row=0)
ssid_entry = ttk.Entry(mainframe)
ssid_entry.grid(column=1, row=0)

password_label = ttk.Label(mainframe, text='Password:')
password_label.grid(column=0, row=1)
password_entry = ttk.Entry(mainframe)
password_entry.grid(column=1, row=1)

transmit_button = ttk.Button(mainframe, text='Transmit', command=create_hotspot)
transmit_button.grid(column=0,row=2,columnspan=2)

device_list_label = ttk.Label(mainframe, text='Connected Devices:')
device_list_label.grid(column=0,row=3,columnspan=2)
device_list = tk.Listbox(mainframe)
device_list.grid(column=0,row=4,columnspan=2)

root.mainloop()