import json
from os import name
from types import prepare_class


def process_xian(fu_data, name):
    xian_data = []
    xian_num = {}
    xian_dict = {}
    xian_data.append({'name': '其他' , 'children':[]})
    qita = xian_data[0]
    dellist = []
    for item in fu_data['children']:
        p = item.find('州')
        if p!=-1:
            zhou = item[0 : p+1]
            xian = item[p+1:]
            if zhou not in xian_num.keys():
                xian_num[zhou] = 1
                xian_data.append({'name': zhou, 'children': [xian]})
            else:
                xian_num[zhou] +=1
                for i in xian_data:
                    if i['name'] == zhou:
                        i['children'].append(xian)
            if(len(xian) > 0) and xian not in xian_dict.keys():
                xian_dict[xian] = zhou
        else:
            qita['children'].append(item)
    for item in qita['children']:
        if item in xian_dict.keys():
            zhou = xian_dict[item]
            if item not in dellist:
                dellist.append(item)
            for i in xian_data:
                if i['name'] == zhou:
                    i['children'].append(item)
    for item in dellist:
        while item in qita['children']:
            qita['children'].remove(item)
    
    dellist = []

    for item in qita['children']:
        if len(item)> 2:
            if item not in xian_num.keys():
                xian_num[item] = 1
                xian_data.append({'name':item, 'children':[item]})
                dellist.append(item)
            else:
                for i in xian_data:
                    if i['name'] == item:
                        i['children'].append(item)
            xian_num[item] +=1

    for item in dellist:
        while item in qita['children']:
            qita['children'].remove(item)
    
    i = 0
    for item in xian_data:
        if(len(item['children']) == 0):
            break
        i += 1
    if i < len(xian_data):
        del xian_data[i]
    for item in xian_data:
        item['value'] = len(item['children'])
        del item['children']

    if fu_data['name'] == "衛" or fu_data['name'] == "所":
        num = 0
        for item in xian_data:
            num += item['value']
        return num

    # if not name in ["交阯", "貴州","雲南"]:
    #     for item in xian_data:
    #         if item['value'] <2:
    #             item['value'] =0 

    return xian_data

with open('fu_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
num = 0
for i in data:
    for j in i['children']:
        if j['name'] == "衛" or j['name'] == "所":
            j['value'] = process_xian(j, i['name'])
            del j['children']
        else:
            j['children'] = process_xian(j, i['name'])
            for k in j['children']:
                num += k['value']
with open('xian_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'name': 'ming', 'children':data}, ensure_ascii=False))
print(num)
