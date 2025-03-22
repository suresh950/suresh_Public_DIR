"""
TO Create firewall policy
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
policy_name = "Netflixblock2"
api_url = f"https://{firewall_ip}/restapi/v10.1/Policies/SecurityRules?location=vsys&vsys=vsys1&name={policy_name}"

headers = {
    "X-PAN-KEY": api_key,  # Correct API key header
    "Content-Type": "application/json"
}
jeson_file= {
  "entry": {
    "@name": "Netflixblock2",
    "from": {
      "member": [
        "any"
      ]
    },
    "to": {
      "member": [
        "any"
      ]
    },
    "source": {
      "member": [
        "any"
      ]
    },
    "source-user": {
      "member": [
        "any"
      ]
    },
    "destination": {
      "member": [
        "any"
      ]
    },
    "service": {
      "member": [
        "application-default"
      ]
    },
    "category": {
      "member": [
        "any"
      ]
    },
    "application": {
      "member": [
        "any"
      ]
    },
    "action": "allow",
    "icmp-unreachable": "no",
    "rule-type": "universal",
    "log-start": "yes",
    "log-end": "yes",

  }
}
api_request = requests.post(url=api_url, headers=headers, json= jeson_file,verify=False)
api_response = api_request.json()

print(f"creation -> {api_response}")