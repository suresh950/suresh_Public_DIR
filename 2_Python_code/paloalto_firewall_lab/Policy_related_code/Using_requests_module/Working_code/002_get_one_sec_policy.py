"""
TO get (policy_name = "Netflix-block") from security policy available in firewall in raw formate ----->without commit
"""
import urllib3
import ssl
import requests
import sys
import csv

if __name__ == '__main__':
    urllib3.disable_warnings()

api_key = "LUFRPT1zTFVUMXh0NmV2bDZOQ0lJbWRraUU0RjZSOEE9RTlLL1RFd01yeGF0b29aMFZoZWE5UDRHWFF5RHFBVW9MOWcrSVprMmtXaDlOLzd5cjdJaDhkUW9UbDB6WkxYWA=="
firewall_ip = "10.10.10.10"
policy_name = "Netflix-block"
api_url = f"https://{firewall_ip}/restapi/v10.1/Policies/SecurityRules?location=vsys&vsys=vsys1&name={policy_name}"

headers = {
    "X-PAN-KEY": api_key,  # Correct API key header
    "Content-Type": "application/json"
}

api_request = requests.get(url=api_url, headers=headers, verify=False)
api_response = api_request.json()

print(f"creation -> {api_response}")