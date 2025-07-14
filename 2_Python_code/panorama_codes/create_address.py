from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"
DEVICE_GROUP_NAME = "BW-ISS"  

# Address object details
ADDRESS_NAME = "Test-Threenew"
ADDRESS_VALUE = "10.10.10.2"
ADDRESS_TYPE = "ip-netmask"  
DESCRIPTION = "Created via pan-os-python"

# Connect to Panorama
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)

# Get the Device Group
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

# Create Address Object
addr_obj = AddressObject(
    name=ADDRESS_NAME,
    value=ADDRESS_VALUE,
    type=ADDRESS_TYPE,
    description=DESCRIPTION
)
device_group.add(addr_obj)

# Commit address object to candidate config
addr_obj.create()

print(f"Address object '{ADDRESS_NAME}' created in device group '{DEVICE_GROUP_NAME}'.")
