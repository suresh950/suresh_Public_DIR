"""
    This script will log in to the firewall and run the command
"""
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
        # os_filter = "<sw-version>(.*)</sw-version>"
        for ip in firewalls_IP:
            print(f"Connecting to firewall.....{ip}")
            firewall_connect = firewall.Firewall(hostname=ip,api_username=api_user,api_password=api_password)
            execute_command = firewall_connect.op(cmd=command, xml=True)
            print(execute_command)
            xml_string = execute_command.decode("utf-8")
            tree = ET.ElementTree(ET.fromstring(xml_string))
            root = tree.getroot()
            print("===" * 50)
            print(f"{root.tag}---> {root.attrib} ---> status: {root.attrib['status']}")
            for a in root:
                print(f"hostname: {a[0][0].text}")
                print(f"ip-address: {a[0][1].text}")
                print(f"public-ip-address: {a[0][2].text}")
                print(f"netmask: {a[0][3].text}")
                print(f"default-gateway: {a[0][4].text}")
                print(f"is-dhcp: {a[0][5].text}")
                print(f"ipv6-address: {a[0][6].text}")
            # print(root)
    except Exception as error:
        print(error)
        sys.exit(0)
