from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup
from panos.policies import SecurityRule, PreRulebase, PostRulebase

PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"
DEVICE_GROUP_NAME = "BW-ISS"
ADDRESS_OBJECT_TO_REMOVE = "one"

try:
    panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)
    device_group = DeviceGroup(DEVICE_GROUP_NAME)
    panorama.add(device_group)
# check and remove from policy
    pre_rulebase = PreRulebase()
    device_group.add(pre_rulebase)
    post_rulebase = PostRulebase()
    device_group.add(post_rulebase)
    security_rules = SecurityRule.refreshall(post_rulebase)
    print (security_rules)
    changed_rules = []
    for rule in security_rules:
        updated = False
        if rule.source and ADDRESS_OBJECT_TO_REMOVE in rule.source:
            rule.source.remove(ADDRESS_OBJECT_TO_REMOVE)
            updated = True
        if rule.destination and ADDRESS_OBJECT_TO_REMOVE in rule.destination:
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
    
except Exception as error:
    print(error)
