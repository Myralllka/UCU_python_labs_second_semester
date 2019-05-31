import urllib.request
import json

def input_name():
    return int(input('print here sectionCode: '))


def parse_f(data, sec_code):
    dict_res = {}
    for each in data['sections']:
        if int(each['sectionCode']) == sec_code:
            dict_res['section_name'] = each['sectionName']
            dict_res['leneach'] = len(each['groups'])
            # for i in each['groups']:

    with open('kisc_results.json', w, encoding='utf-8') as ff:
        json.dump(ff, ensure_ascii=False)
    # print(data)



def main():
    name = input_name()
    url = 'https://data.gov.ua/dataset/ed5fc1b8-2da6-4041-885a-c37357c8acc0/resource/663245c2-deb6-4ede-8d6f-b864f9d5989d/download/kisc.json'
    data = urllib.request.urlopen(url).read()
    data = json.loads(data.decode('utf-8'))
    parse_f(data, name)


if __name__ == '__main__':
    main()
