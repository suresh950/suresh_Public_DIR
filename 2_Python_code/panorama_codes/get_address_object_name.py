from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"
DEVICE_GROUP_NAME = "BW-ISS"  

# Address object details
ADDRESS_VALUE = "3.3.3.33"
 
# Connect to Panorama
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)

# Get the Device Group
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)
address_objects = AddressObject.refreshall(device_group)
# print(address_objects)
for obj in address_objects:
    if obj.value == ADDRESS_VALUE:
        print (obj.name)

