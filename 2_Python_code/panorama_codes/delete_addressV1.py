# script to delete the address object

from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject
import pandas as pd

file_path = "address_object.xlsx"

dfSheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
ADDRESS_NAME_LIST = dfSheet1["ADDRESS_NAME"].tolist()
ADDRESS_VALUE_LIST =  dfSheet1["ADDRESS_VALUE"].tolist()
DESCRIPTION_LIST = dfSheet1["DESCRIPTION"].tolist()

dfSheet2 = pd.read_excel(file_path, sheet_name='Sheet2')
DEVICE_GROUP_NAME_LIST = dfSheet2["DEVICE_GROUP_NAME"].tolist()
ADDRESS_TYPE_LIST = dfSheet2["ADDRESS_TYPE"].tolist()

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"

DEVICE_GROUP_NAME = DEVICE_GROUP_NAME_LIST[0]  
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)

device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

for n in range(0, (len(ADDRESS_VALUE_LIST))-1 ):
    ADDRESS_NAME = ADDRESS_NAME_LIST[n]
    addr_obj = AddressObject(name=ADDRESS_NAME_LIST[n],)
    device_group.add(addr_obj)
    addr_obj.delete()
    print(f"Address object '{ADDRESS_NAME}' is deleted")
