import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)


for child in root:
    print(child.tag, child.attrib)

print(root[0][1].text)

for child in root:
    print(f"rank: {child[0].text} --> year: {child[1].text} --> gdppc")
