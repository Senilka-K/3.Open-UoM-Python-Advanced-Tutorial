import xml.etree.ElementTree as ET

vehicle_xml_data_as_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>"

root = ET.fromstring(vehicle_xml_data_as_string)

for vehicle in root.findall(".//vehicle"):
    registration_no = vehicle.find("registration_no").text
    if registration_no == "DE2115":
        selected_vehicle = vehicle

if selected_vehicle is not None:
   selected_vehicle.find("make").text = "Nissan"
   selected_vehicle.find("model").text = "Skyline"


nissan_vehicles = root.findall(".//vehicle[make='Nissan']/registration_no")
for reg_no_element in nissan_vehicles:
    print(reg_no_element.text)


    