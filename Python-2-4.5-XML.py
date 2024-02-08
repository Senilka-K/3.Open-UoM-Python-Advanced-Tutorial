import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

a = root[1][0].text
print(a)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')


