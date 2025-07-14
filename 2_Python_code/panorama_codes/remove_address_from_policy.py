from panos.panorama import Panorama
from panos.panorama import DeviceGroup
from panos.objects import AddressObject, AddressGroup
from panos.policies import SecurityRule, PreRulebase, PostRulebase

# Panorama connection details
PANORAMA_HOST = "10.10.10.202"
USERNAME = "admin"
PASSWORD = "Suresh@1234"

DEVICE_GROUP_NAME = "BW-ISS"
ADDRESS_OBJECT_TO_REMOVE = "one"

# Connect to Panorama
panorama = Panorama(PANORAMA_HOST, USERNAME, PASSWORD)

# Attach to the specific device group
device_group = DeviceGroup(DEVICE_GROUP_NAME)
panorama.add(device_group)

# Attach to the pre-rulebase of the device group
post_rulebase = PostRulebase()
device_group.add(post_rulebase)

# Fetch all security rules from the pre-rulebase
security_rules = SecurityRule.refreshall(post_rulebase)
print (security_rules)
# Track changes
changed_rules = []

for rule in security_rules:
    updated = False

    # Remove from source address
    if rule.source and ADDRESS_OBJECT_TO_REMOVE in rule.source:
        rule.source.remove(ADDRESS_OBJECT_TO_REMOVE)
        updated = True

    # Remove from destination address
    if rule.destination and ADDRESS_OBJECT_TO_REMOVE in rule.destination:
        rule.destination.remove(ADDRESS_OBJECT_TO_REMOVE)
        updated = True

    # Apply changes if updated
    if updated:
        rule.apply()
        changed_rules.append(rule.name)
        print(f"✅ Removed '{ADDRESS_OBJECT_TO_REMOVE}' from rule: {rule.name}")

# Report
if not changed_rules:
    print(f"ℹ️ '{ADDRESS_OBJECT_TO_REMOVE}' not found in any pre-rulebase security rule.")
else:
    print(f"🔄 Updated rules: {changed_rules}")