from pandevice import firewall
import re
from pprint import pprint
import xml.etree.ElementTree as ET
import sys

if __name__ == '__main__':

    try:
        api_user = "api-user"
        api_password = "Suresh@1234"
        firewalls_IP = ["10.10.10.10"]
        command = "show system info"
        os_filter = "<sw-version>(.*)</sw-version>"

        for ip in firewalls_IP:
            print(f"Connecting to firewall.....{ip}")
            firewall_connect = firewall.Firewall(hostname=ip,api_username=api_user,api_password=api_password)
            execute_command = firewall_connect.op(cmd=command, xml=True)
            print(execute_command)
            tree = ET.parse(execute_command)

            system_version = re.search(os_filter, str(execute_command))
            print(firewall + " - version: " + system_version.group(1))

    except Exception as error:
        print(error)
        sys.exit(0)

