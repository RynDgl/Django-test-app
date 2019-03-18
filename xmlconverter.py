
import xmltodict
import pprint
import json

def xml_to_json(path_to_xml_file,path_to_new_json_file):
    with open(path_to_xml_file) as fd:
        doc = xmltodict.parse(fd.read())

    with open(path_to_new_json_file,'w') as fo:
        json.dump(doc,fo)

    print('Done')