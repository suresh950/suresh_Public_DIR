from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"


DEVICE_GROUP_NAME = "BW-ISS"  
ADDRESS_GROUP_NAME = "Prod"
ADDRESS_TO_REMOVE = "one"

# Connect to Panorama
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)

# Attach to the specific device group
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

# Fetch all address groups under this device group
address_groups = AddressGroup.refreshall(device_group)

# Find the specific address group
target_group = next((ag for ag in address_groups if ag.name == ADDRESS_GROUP_NAME), None)

if not target_group:
    raise ValueError(f"Address group '{ADDRESS_GROUP_NAME}' not found in device group '{DEVICE_GROUP_NAME}'.")

# Refresh it to ensure we have latest data
target_group.refresh()

# Remove the address from the group's static_value
if target_group.static_value and ADDRESS_TO_REMOVE in target_group.static_value:
    target_group.static_value.remove(ADDRESS_TO_REMOVE)
    print(dir(target_group.static_value))
    target_group.apply()  # Push the updated address group
    print(f"✅ Removed '{ADDRESS_TO_REMOVE}' from address group '{ADDRESS_GROUP_NAME}'.")
else:
    print(f"ℹ️ Address '{ADDRESS_TO_REMOVE}' not found in group '{ADDRESS_GROUP_NAME}'. Nothing changed.")