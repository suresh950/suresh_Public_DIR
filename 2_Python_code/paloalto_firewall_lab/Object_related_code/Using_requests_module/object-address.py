#!/usr/bin/env python
import ssl
import urllib3
import sys
import csv
import json
import requests

if __name__ == '__main__':

  urllib3.disable_warnings()

  #---------------------------------------------------------------------------------------------------------------------------------------------------
  # This is the section where you can set your api_key , firewalln IP  and path for the CSV file
  api_key       = "PUT_YOUR_API_KEY_HERE"
  firewall_ip   = "10.10.10.10"
  address_file  = "lab6-address.csv"
  #---------------------------------------------------------------------------------------------------------------------------------------------------

try:
  
  file_      = open(address_file, 'r')
  csv_reader = csv.reader(file_)

  for row in csv_reader:   

    #-----------------------------------------------------------------------------------------------------------
    #
    # In the CSV file, row[0] is the value of the address name
    # In the CSV file, row[1] is the value of the IP address
    address_name      = row[0]
    address_ip        = row[1]
    # This is the JSON data. The structure can be retrieve from the rest-api doc
    json_data         = { "entry": { "@name" : address_name ,  "ip-netmask" : address_ip } }
    # This is the URI to create address objects. The syntax can be retrieve from the rest-api doc
    uri               = "/restapi/9.0/Objects/Addresses?location=vsys&vsys=vsys1&name="+row[0]+"&key="+api_key
    #-----------------------------------------------------------------------------------------------------------

    api_url      = "https://"+firewall_ip+uri
    api_request  = requests.post(url=api_url,data=json.dumps(json_data),verify=False)
    api_response = api_request.text
    print(row[0]+" creation ->"+api_response)

except:
  print("ERROR   : Connecting to "+firewall_ip+". Check the Firewall IP address and API Key.")
  print("Check if the path of the "+address_file+" file is correct.")
  sys.exit(0)	






