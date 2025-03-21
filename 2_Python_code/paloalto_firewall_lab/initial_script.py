import ssl
import urllib3
import requests
import sys
import xml.etree.ElementTree as ET

api_key = "LUFRPT1zTFVUMXh0NmV2bDZOQ0lJbWRraUU0RjZSOEE9RTlLL1RFd01yeGF0b29aMFZoZWE5UDRHWFF5RHFBVW9MOWcrSVprMmtXaDlOLzd5cjdJaDhkUW9UbDB6WkxYWA=="
xml_command = "<show><system><info></info></system></show>"
xml_elements = ["model", "hostname","sw-version"]
fw_ip_address= ["10.10.10.10"]



try:
    for ip in fw_ip_address:
        api_url = f'https://{ip}/api/?type=op&cmd={xml_command}&key={api_key}'
        urllib3.disable_warnings()
        api_request = requests.get(url=api_url,verify=False)
        api_responce = api_request.text
        xml_tree_root =ET.fromstring(api_responce)

    for a in xml_tree_root.iter():
        print(a)

    for tag in xml_elements:
        for leaf in xml_tree_root.iter(tag):
            if leaf.tag == tag:
                print(tag+":"+leaf.text)
except Exception as error:
    print(error)