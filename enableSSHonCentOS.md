## To open a port on CentOS, the primary tool used is firewalld. Check FirewallD status.

Code
```python
    sudo firewall-cmd --state
```
If it's not running, you can start and enable it:
Code

    sudo systemctl start firewalld
    sudo systemctl enable firewalld
Identify the zone.
FirewallD uses zones to define different levels of trust for network connections. The public zone is often used for general internet-facing services. You can list active zones or determine the zone of a specific interface:
Code

    sudo firewall-cmd --get-active-zones
    # or, for a specific interface like eth0:
    sudo firewall-cmd --get-zone-of-interface=eth0
open the port.
To open a specific port, for example, TCP port 8080, in the public zone permanently (so it persists after a reboot):
Code

    sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
Replace 8080 with the desired port number and tcp with udp if it's a UDP port. You can also specify a port range, e.g., 5000-6000/tcp. Reload FirewallD.
After making permanent changes, reload the firewall rules for them to take effect:
Code

    sudo firewall-cmd --reload
Verify the open port.
You can list the open ports in a specific zone to confirm the change:
Code

    sudo firewall-cmd --zone=public --list-ports
Alternatively, you can list all rules for a zone:
Code

    sudo firewall-cmd --zone=public --list-all
