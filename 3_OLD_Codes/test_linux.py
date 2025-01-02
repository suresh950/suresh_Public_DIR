import paramiko
import time

cli_command_list = ["df -h"]
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

login_to_switch("192.168.126.134","student","Forcepoint1")