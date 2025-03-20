#!/usr/bin/env python
import ssl
import urllib3
import requests
import json
import sys
import csv
import xml.etree.ElementTree as ET

if __name__ == '__main__':

  urllib3.disable_warnings()
  
  #---------------------------------------------------------------------------------------------------------------------------------------------------
  # This is the section where you can set your api_key , firewalln IP  and path for the CSV file
  api_key       = "PUT_YOUR_API_KEY_HERE"
  firewall_ip   = "PUT_YOUR_FW_IP_HERE"
  rules_file    = "lab6-rules.csv"
  #---------------------------------------------------------------------------------------------------------------------------------------------------

  
  file_      = open(rules_file, 'r')
  csv_reader = csv.reader(file_)

try:

  for row in csv_reader:   
    #-----------------------------------------------------------------------------------------------------------
    # In the CSV file, row[0] is the value of rule name
    # In the CSV file, row[1] is the value of the source zone ( any )
    # In the CSV file, row[2] is the value of the source IP
    # In the CSV file, row[3] is the value of destination zone ( any )
    # In the CSV file, row[4] is the value of the destination IP
    # In the CSV file, row[5] is the value of the application
    # In the CSV file, row[6] is the value of the service 
    # In the CSV file, row[7] is the value of the action
    #
    # The .split(" ") funtion is only usefull is you have several IPs , Zones , Applications in the same rule. Separate them with a space in the CSV files.

    rule_name         = row[0]
    source_zone       = row[1].split(" ")
    source_ip         = row[2].split(" ")   
    destination_zone  = row[3].split(" ")    
    destination_ip    = row[4].split(" ")    
    application       = row[5].split(" ")    
    service           = row[6].split(" ")   
    action            = row[7] 
    
    # This is the JSON data & URI . The structure can be retrieve from the rest-api doc
    json_data         = {"entry": { "@name": rule_name, "from": {"member": source_zone}, "source": {"member": source_ip}, "to": {"member": destination_zone}, "destination": {"member": destination_ip}, "application": {"member": application}, "service": {"member": service}, "action":action } }
    uri               = "/restapi/9.0/Policies/SecurityRules?location=vsys&vsys=vsys1&name="+rule_name+"&key="+api_key
    #-----------------------------------------------------------------------------------------------------------

    api_url         = "https://"+firewall_ip+uri
    api_request     = requests.post(url=api_url,data=json.dumps(json_data),verify=False)
    api_response    = api_request.text

    print(row[0]+" creation ->"+api_response)

except:
  print("ERROR   : Connecting to "+firewall_ip+". Check the Firewall IP address and API Key.")
  print("Check if the path of the "+rules_file+" file is correct.")
  sys.exit(0)	
