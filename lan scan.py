import tkinter as tk
from tkinter import ttk
from scapy.all import ARP, Ether, srp
from getmac import get_mac_address
from socket import gethostbyaddr

def scan_devices(network_bits):
    target_ip = target_ip_entry.get()
    if network_bits == 24:
        target_ip += '/24'
    elif network_bits == 16:
        target_ip += '/16'
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    output_text.delete('1.0', tk.END)
    for device in devices:
        mac = device['mac']
        ip = device['ip']
        try:
            hostname = gethostbyaddr(ip)[0]
        except:
            hostname = 'Unknown'
        output_text.insert(tk.END, f"Device Name: {hostname} IP: {ip} MAC: {mac}\n")

root = tk.Tk()
root.title('LAN Device Scanner')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

target_ip_label = ttk.Label(mainframe, text='Target IP:')
target_ip_label.grid(column=0, row=0)
target_ip_entry = ttk.Entry(mainframe)
target_ip_entry.grid(column=1, row=0)

scan_24_button = ttk.Button(mainframe, text='Scan 24-bit', command=lambda: scan_devices(24))
scan_24_button.grid(column=0,row=1)

scan_16_button = ttk.Button(mainframe, text='Scan 16-bit', command=lambda: scan_devices(16))
scan_16_button.grid(column=1,row=1)

output_label = ttk.Label(mainframe, text='Output:')
output_label.grid(column=0,row=2,columnspan=2)
output_text = tk.Text(mainframe)
output_text.grid(column=0,row=3,columnspan=2)

root.mainloop()