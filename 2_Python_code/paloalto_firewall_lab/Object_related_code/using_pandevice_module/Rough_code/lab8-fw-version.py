#!/usr/bin/env python
# Copyright (c) 2017, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


from pandevice import firewall
import sys
import re

if __name__ == '__main__':

  try:

    #---------------------------------------------------------------------------------------------------------------------------------------------------
    # This is the section where you can set user , password , command , os_filter and firewall_list.
    api_user      = "api-user"
    api_password  = "Suresh@1234"
    firewalls     = [["PUT_FW1_HOSTNAME_HERE","10.10.10.10"]]

    command       = "show system info"
    os_filter     = "<sw-version>(.*)</sw-version>"
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    # This is the section  where the framework connect to the firewalls to execute the command and display the result. 
    for firewall_name, firewall_ip in firewalls:
      firewall_connect = firewall.Firewall(hostname=firewall_ip, api_username=api_user, api_password=api_password)
      system_info      = firewall_connect.op(cmd=command, xml=True)
      
      #un-comment the line below to see the full ouput of the operational command
      #print(system_info)
  
      system_version   = re.search(os_filter,str(system_info))
      print(firewall_name+" - version: "+system_version.group(1))
    #---------------------------------------------------------------------------------------------------------------------------------------------------

  except:
    print("ERROR   : Connecting to "+firewall_ip+". Check the Firewall IP address and Credentials.")
    sys.exit(0)	