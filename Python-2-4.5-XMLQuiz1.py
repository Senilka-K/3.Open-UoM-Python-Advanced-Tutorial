import xml.etree.ElementTree as ET

root = ET.Element("tag1")

tag2 = ET.Element("tag2")
tag2.text = "Animal"

tag3 = ET.Element("tag3")
tag3.text = "Domestic"

tag4 = ET.Element("tag4")
tag4_1 = ET.Element("tag4.1")
tag4_1.text = "Cat"
tag4_2 = ET.Element("tag4.2")
tag4_2.text = "Persian"
tag4.append(tag4_1)
tag4.append(tag4_2)

tag5 = ET.Element("tag5")
tag5.text = "Iran"

tag6 = ET.Element("tag6")
tag6.text = "Male"

tag7 = ET.Element("tag7")
tag7.text = "2021.05.04"

root.append(tag2)
root.append(tag3)
root.append(tag4)
root.append(tag5)
root.append(tag6)
root.append(tag7)

tree = ET.ElementTree(root)

tree.write("animal.xml")

ET.dump(root)