"""
    pandevice module using and passing the command and get output and filtering using regular expression
    this code is providing PaloAlto Firewall OS version
"""
from pandevice import firewall
import re
import sys
if __name__ == '__main__':
    try:
        api_user = "api-user"
        api_password = "Suresh@1234"
        firewalls_IP = ["10.10.10.10",
                        "10.10.10.11",
                        "10.10.10.12",
                        "10.10.10.13"]
        command = "show system info"
        os_version_filter = "<sw-version>(.*)</sw-version>"
        for ip in firewalls_IP:
            firewall_connect = firewall.Firewall(hostname=ip,api_username=api_user,api_password=api_password)
            execute_command = firewall_connect.op(cmd=command, xml=True)
            system_version = re.search(os_version_filter, str(execute_command))
            print(f"Firewall [{ip}] OS version: {system_version.group(1)}")
    except Exception as error:
        print(error)
        sys.exit(0)

