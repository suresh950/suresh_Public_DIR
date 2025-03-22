""""
TO create the object group
"""

import urllib3
import ssl
import requests
import sys
import csv
if __name__ == '__main__':
    urllib3.disable_warnings()
    # API Key and Firewall Details
    api_key = "LUFRPT1zTFVUMXh0NmV2bDZOQ0lJbWRraUU0RjZSOEE9RTlLL1RFd01yeGF0b29aMFZoZWE5UDRHWFF5RHFBVW9MOWcrSVprMmtXaDlOLzd5cjdJaDhkUW9UbDB6WkxYWA=="
    firewall_ip = "10.10.10.10"
    address_file = "lab6-address.csv"
    headers = {
        "X-PAN-KEY": api_key,  # Correct API key header
        "Content-Type": "application/json"
    }
    try:
        with open(address_file, 'r') as file_:
            csv_reader = csv.reader(file_)
            group_name =  "commangrpnew"
            address_name_list = []
            for row in csv_reader:
                address_name = row[0]
                address_ip = row[1]
                address_name_list.append(row[0])
                # Corrected JSON payload (No @name inside JSON)
            json_data_2 = {
                          "entry": {
                                    "@name":group_name,
                                    "static": {
                                    "member":
                                                address_name_list
                                            },
                                    }
                          }
            # Palo Alto API endpoint (name passed as a query parameter)
            api_url = f"https://{firewall_ip}/restapi/v10.1/Objects/AddressGroups?location=vsys&vsys=vsys1&name={group_name}"
            # Sending request with API Key in headers
            api_request = requests.post(url=api_url, headers=headers, json=json_data_2,verify=False)
            api_response = api_request.text
            print(f"{address_name} creation -> {api_response}")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print(f"Check the Firewall IP address, API Key, and CSV file path.")
        sys.exit(0)

