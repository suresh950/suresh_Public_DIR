from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup
from panos.policies import SecurityRule, PreRulebase, PostRulebase
import pandas as pd

PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"

file_path = "palo_decom.xlsx"

dfSheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
ADDRESS_VALUE_LIST =  dfSheet1["ADDRESS_VALUE"].tolist()

dfSheet2 = pd.read_excel(file_path, sheet_name='Sheet2')
DEVICE_GROUP_NAME_LIST = dfSheet2["DEVICE_GROUP_NAME"].tolist()

try:
    DEVICE_GROUP_NAME = DEVICE_GROUP_NAME_LIST[0]
    panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)
    device_group = DeviceGroup(DEVICE_GROUP_NAME)
    panorama.add(device_group)

    # get the Address object name
    for ADDRESS_VALUE in ADDRESS_VALUE_LIST:
        address_objects = AddressObject.refreshall(device_group)
        for obj in address_objects:
            if obj.value == ADDRESS_VALUE:
                ADDRESS_OBJECT_TO_REMOVE = obj.name

        # check and remove from policy
        pre_rulebase = PreRulebase()
        device_group.add(pre_rulebase)
        post_rulebase = PostRulebase()
        device_group.add(post_rulebase)
        security_rules = SecurityRule.refreshall(post_rulebase)
        changed_rules = []
        for rule in security_rules:
            updated = False
            if rule.source and ADDRESS_OBJECT_TO_REMOVE in rule.source:
                if len(rule.source)==1:
                    rule.delete()
                    updated = False
                    print(f"📝 Removed rule: {rule.name}")
                else:
                    rule.source.remove(ADDRESS_OBJECT_TO_REMOVE)
                    updated = True
            if rule.destination and ADDRESS_OBJECT_TO_REMOVE in rule.destination:
                if len(rule.destination)==1:
                    rule.delete()
                    updated = False
                    print(f"📝 Removed rule: {rule.name}")
                else:
                    rule.destination.remove(ADDRESS_OBJECT_TO_REMOVE)
                    updated = True
            if updated:
                rule.apply()
                changed_rules.append(rule.name)
                print(f"✅ Removed '{ADDRESS_OBJECT_TO_REMOVE}' from rule: {rule.name}")

        # check if it is available in any address Group
        address_groups = AddressGroup.refreshall(device_group)

        for group in address_groups:
            for address_object in group.static_value:
                if address_object == ADDRESS_OBJECT_TO_REMOVE:
                    if group.static_value and ADDRESS_OBJECT_TO_REMOVE in group.static_value:
                        group.static_value.remove(ADDRESS_OBJECT_TO_REMOVE)
                        group.apply()  # Push the updated address group
                        print(f"✅ Removed '{ADDRESS_OBJECT_TO_REMOVE}' from address group {group}.")
                    else:
                        print(f"ℹ️ Address '{ADDRESS_OBJECT_TO_REMOVE}' not found in group. Nothing changed.")
        
        # Delete the address
        addr_obj = AddressObject(name=ADDRESS_OBJECT_TO_REMOVE)
        device_group.add(addr_obj)
        addr_obj.delete()
        print(f"Address object '{ADDRESS_OBJECT_TO_REMOVE}' is deleted")

except Exception as error:
    print("❌", error)
