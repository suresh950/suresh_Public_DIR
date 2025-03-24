"""
set address <object_name> <address_type> <address_value>
> configure
# set address <AddressObject_01> ip-netmask 1.1.1.1/32
# set address <AddressObject_02> fqdn my.example.com
# set address <AddressObject_nn> ip-range 2.2.2.2-3.3.3.3
# set address-group <AddressGroup> static [ <AddressObject_01> <AddressObject_02> ...<AddressObject_nn> ]
"""

import pandevice
from pandevice import firewall
import re

firewall_IP_list = ["10.10.10.10",
                    "10.10.10.11",
                    "10.10.10.12",
                    "10.10.10.13"]
comands_list = ["set address AddressObject_01 ip-netmask 1.1.1.1/32",
                "set address AddressObject_02 fqdn my.example.com",
                "set address AddressObject_nn ip-range 2.2.2.2-3.3.3.3"]
username= "api-user"
password="Suresh@1234"

try:
    for ip in firewall_IP_list:
        connect_firewall = firewall.Firewall(hostname=ip,api_username=username,api_password=password)
        for command in comands_list:
            excute_command = connect_firewall.op(cmd=command, xml=True)
            # system_version = re.search(os_version_filter, str(excute_command))

except Exception as error:
    print(error)