from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"


DEVICE_GROUP_NAME = "BW-ISS"  
# ADDRESS_GROUP_NAME = "Prod"
ADDRESS_TO_REMOVE = "one"


panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

address_groups = AddressGroup.refreshall(device_group)

for group in address_groups:
    for address_object in group.static_value:
        print(address_object)
        if address_object == ADDRESS_TO_REMOVE:
            print("the one is in : --> ",group)
            if group.static_value and ADDRESS_TO_REMOVE in group.static_value:
                group.static_value.remove(ADDRESS_TO_REMOVE)
                group.apply()  # Push the updated address group
                print(f"✅ Removed '{ADDRESS_TO_REMOVE}' from address group .")
            else:
                print(f"ℹ️ Address '{ADDRESS_TO_REMOVE}' not found in group. Nothing changed.")
