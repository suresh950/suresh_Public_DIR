import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

print("==="*50)
for child in root:
    print(child.tag, child.attrib)
print("==="*50)
print(root[0][1].text)
print("==="*50)
for child in root:
    print(f"rank: {child[0].text}"
          f"--> year: {child[1].text} "
          f"--> gdppc: {child[2].text} "
          f"--> neighbor: {child[3].tag} = {child[3].attrib}")
print("==="*50)
print(f"{root[0][4].tag} ----> {root[0][4].attrib}")
print("==="*50)
print(f"{root[2][4].tag} ----> {root[2][4].attrib}")
