from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup
from panos.policies import SecurityRule, PreRulebase, PostRulebase
import pandas as pd
import threading

PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"

file_path = "palo_decom.xlsx"

dfSheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
ADDRESS_VALUE_LIST = dfSheet1["ADDRESS_VALUE"].tolist()

dfSheet2 = pd.read_excel(file_path, sheet_name='Sheet2')
DEVICE_GROUP_NAME_LIST = dfSheet2["DEVICE_GROUP_NAME"].tolist()

try:
    DEVICE_GROUP_NAME = DEVICE_GROUP_NAME_LIST[0]
    panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)
    device_group = DeviceGroup(DEVICE_GROUP_NAME)
    panorama.add(device_group)

    # Preload rules and groups to avoid repeated API calls per thread
    pre_rulebase = PreRulebase()
    device_group.add(pre_rulebase)
    post_rulebase = PostRulebase()
    device_group.add(post_rulebase)

    all_rules = SecurityRule.refreshall(post_rulebase)
    all_address_objects = AddressObject.refreshall(device_group)
    all_address_groups = AddressGroup.refreshall(device_group)

    # Match value to object names (build lookup map)
    value_to_name = {obj.value: obj.name for obj in all_address_objects if obj.value in ADDRESS_VALUE_LIST}

    def addr_obj_remove(ADDRESS_OBJECT_TO_REMOVE):
        # Remove from policies
        for rule in all_rules:
            updated = False
            if rule.source and ADDRESS_OBJECT_TO_REMOVE in rule.source:
                if len(rule.source) == 1:
                    rule.delete()
                    print(f"📝 Removed rule: {rule.name}")
                    continue
                else:
                    rule.source.remove(ADDRESS_OBJECT_TO_REMOVE)
                    updated = True
            if rule.destination and ADDRESS_OBJECT_TO_REMOVE in rule.destination:
                if len(rule.destination) == 1:
                    rule.delete()
                    print(f"📝 Removed rule: {rule.name}")
                    continue
                else:
                    rule.destination.remove(ADDRESS_OBJECT_TO_REMOVE)
                    updated = True
            if updated:
                rule.apply()
                print(f"✅ Removed '{ADDRESS_OBJECT_TO_REMOVE}' from rule: {rule.name}")

        # Remove from address groups
        for group in all_address_groups:
            if ADDRESS_OBJECT_TO_REMOVE in group.static_value:
                group.static_value.remove(ADDRESS_OBJECT_TO_REMOVE)
                group.apply()
                print(f"✅ Removed '{ADDRESS_OBJECT_TO_REMOVE}' from address group {group.name}")

        # Delete the address object
        addr_obj = AddressObject(name=ADDRESS_OBJECT_TO_REMOVE)
        device_group.add(addr_obj)
        addr_obj.delete()
        print(f"🗑️ Address object '{ADDRESS_OBJECT_TO_REMOVE}' deleted")

    # Launch threads
    threads = []
    for address_value, address_name in value_to_name.items():
        t = threading.Thread(target=addr_obj_remove, args=(address_name,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("✅ All address removals complete.")

except Exception as error:
    print("❌", error)
