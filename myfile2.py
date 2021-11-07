import json
import yaml

with open ('myfile2.json', 'r') as json_file:
    ourjson = json.load (json_file)

print (ourjson)

print("La dirrecion ip es: {}".format(ourjson['ipadd_prefix']))
print("la mascara de subredes  {}".format(ourjson['mask_subred']))

print (yaml.dump(ourjson))
