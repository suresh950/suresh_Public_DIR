from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject
import pandas as pd
import threading

# File and Panorama credentials
file_path = "address_object.xlsx"
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"

# Read Excel sheets
dfSheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
ADDRESS_NAME_LIST = dfSheet1["ADDRESS_NAME"].tolist()
ADDRESS_VALUE_LIST = dfSheet1["ADDRESS_VALUE"].tolist()
DESCRIPTION_LIST = dfSheet1["DESCRIPTION"].tolist()

dfSheet2 = pd.read_excel(file_path, sheet_name='Sheet2')
DEVICE_GROUP_NAME_LIST = dfSheet2["DEVICE_GROUP_NAME"].tolist()
ADDRESS_TYPE_LIST = dfSheet2["ADDRESS_TYPE"].tolist()

DEVICE_GROUP_NAME = DEVICE_GROUP_NAME_LIST[0]
ADDRESS_TYPE = ADDRESS_TYPE_LIST[0]  # Assuming one common type

# Set up Panorama and Device Group
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

# Thread-safe creation function
def create_address_object(n):
    try:
        addr_obj = AddressObject(
            name=ADDRESS_NAME_LIST[n],
            value=ADDRESS_VALUE_LIST[n],
            type=ADDRESS_TYPE,
            description=DESCRIPTION_LIST[n]
        )
        device_group.add(addr_obj)
        addr_obj.create()
        print(f"✅ Created: {ADDRESS_NAME_LIST[n]}")
    except Exception as e:
        print(f"❌ Error for {ADDRESS_NAME_LIST[n]}: {e}")

# Launch threads
threads = []
for n in range(len(ADDRESS_NAME_LIST)):
    t = threading.Thread(target=create_address_object, args=(n,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

print("🎉 All address objects created!")
