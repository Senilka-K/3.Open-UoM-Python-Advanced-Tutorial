# import json
# def as_complex(dct):
#     if '__complex__' in dct:
#         return complex(dct['real'], dct['imag'])
#     return dct

# json.loads('{"__complex__": true, "real": 1, "imag": 2}',
#     object_hook=as_complex)

# # import decimal
# # json.loads('1.1', parse_float=decimal.Decimal)

import json
myVar = '{"name": "Bob", "languages": ["English", "French"]}'

parsed_json = json.loads(myVar)

if isinstance(parsed_json, dict):
    json_objects_count = len(parsed_json)

else:
    json_objects_count = 1

print(json_objects_count)
