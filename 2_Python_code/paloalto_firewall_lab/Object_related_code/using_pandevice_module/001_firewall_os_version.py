import pandevice
import re

if __name__ == '__main__':

    try:
        api_user = "api-user"
        api_password = "Suresh@1234"
        firewalls_IP = ["10.10.10.10"]
        command = "show system info"
        os_filter = "<sw-version>(.*)</sw-version>"

        for firewall in firewalls_IP:
            firewall_connect = pandevice.firewall.Firewall(hostname=firewall,api_username=api_user,api_password=api_password)
            firewall_info = firewall_connect.op(cmd=command,xml=True)

    except Exception as error:
        print(error)

