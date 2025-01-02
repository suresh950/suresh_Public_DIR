# import subprocess
# import sys
# def install_package(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# if __name__ == "__main__":
#     install_package("paramiko")

import paramiko
import time
import os
username = os.environ.get('Username')
passwd = os.environ.get('Password')
cli_command_list = ["enable","terminal length 0","show Version"]
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
    except:
        return False

login_to_switch("devnetsandboxiosxe.cisco.com",user=username,passwd=passwd)
