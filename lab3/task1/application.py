import json


def read_json(fname):
    """
    function to read json file
    """
    result = list()
    f = open(fname, 'r', encoding='utf-8')
    number = int(f.readline())
    i = 0
    for line in f:
        result.append(json.loads(line))
    return result


def average(in_list):
    result = {}
    for each in in_list:
        av, n = 0, 0
        for kk in each:
            if kk != 'serial':
                av += each[kk]
                n += 1
        av = av / n
        result[each['serial']] = av
    mm = max(result.values())
    res = {}
    for each in result:
        if result[each] == mm:
            res[each] = mm
    with open('res.json', 'w') as ff:
        print(json.dump(res, ff))


average(read_json('training.json'))
