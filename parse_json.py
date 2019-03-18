
import json

with open('/Users/ryan/Documents/json-to-xml/cvexref.json', 'r') as f:
    json_dict = json.load(f)
    f.close()

def search_json(search_string,date_range):
    date_range = date_range.split()
    refined = []
    refined_two = []
    search_set = set(search_string.lower().split())
    for item in json_dict['cvexref']['notice']:
        if len(search_set) == len(search_set & set(item['@title'].lower().split())):
            refined.append(item)
    for item in refined:
        if date_range != '' and item['@number'].split('-')[0] in date_range:
            refined_two.append(item)
        else:
            return refined
    return refined_two

def main():
    for item in software_list:
        search.json(item)
    
if __name__ == '__main__':
    software_list = ['7-zip','Microsoft Windows']
    
    for item in software_list:
        i = 0
        new = search_json(item,'2016 2017 2018 2019')
        for item in new:
            i += 1
            print(item['@title'], '#', i)
        print(i)