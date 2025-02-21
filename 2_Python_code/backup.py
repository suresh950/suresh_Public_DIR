import subprocess
import sys
from datetime import datetime

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_package("paramiko")

import paramiko
import time
import os
user1 = os.environ.get('Username')
pass1 = os.environ.get('Password')

# username = input("username ")
# passwd = input("password ")
router_list = ["10.168.20.1","10.168.20.11"]
cli_command_list = ["enable",pass1,"terminal length 0","show Version"]
def login_to_switch(ip, user, passwd, successfull=None):
    ssh_client = paramiko.client.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=ip,
                           port=22,
                           username=user,
                           password=passwd,
                           look_for_keys=False,
                           allow_agent=False)
        print(f"{'!' * 120} Connected successfully: {ip}")
        device_access = ssh_client.invoke_shell()
        for commands in cli_command_list:
            device_access.send(f"{commands}\n".encode("utf-8"))
            time.sleep(2)
            print(commands)
        output = device_access.recv(9899)
        print(output.decode())
        device_access.close()
        output_date = output.decode()

        time_new = datetime.now()
        time_now = time_new.strftime("%d/%m/%Y %H:%M:%S")
        with open(f"/tmp/semaphore/Backup{time_now}.txt", "w") as outputnew:
            outputnew.write(str(output_date))

        return True  # Indicate successful login
    except Exception as error:
        print(error)
        return False
for ip in router_list:
    login_to_switch(ip = ip,user=user1,passwd=pass1)
