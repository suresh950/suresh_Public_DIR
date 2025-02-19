import subprocess
import sys
# def install_package(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# if __name__ == "__main__":
#     install_package("paramiko")

import paramiko
import time
import os
user1 = os.environ.get('Username')
pass1 = os.environ.get('Password')
SRV= os.environ.get('Router')

# username = input("username ")
# passwd = input("password ")
cli_command_list = ["docker cp dff50bac59d5:/tmp/semaphore/repository_1_4 /home/mainpyub",pass1]
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
        return True  # Indicate successful login
    except Exception as error:
        print(error)
        return False

login_to_switch(ip = SRV,user=user1,passwd=pass1)

