import json
from os import name
from typing import ItemsView

li = ["直隸","陝西","山西","山東","河南","浙江","江西","湖廣",
    "四川","廣東","福建","廣西","貴州","雲南","交阯"]
di_first = {}
di_second = {}

def find_divide_place(place):
    a = place.find("縣")
    b = place.find("府")
    c = place.find("州")
    d = place.find("衛")
    e = place.find("州府")
    nmin = 10000
    if a!=-1:
        nmin =min(nmin, a)
    if e==-1:  
        if b!=-1:
            nmin = min(nmin,b)
        if c!=-1:
            nmin = min(nmin, c)
    else:
        nmin = min(nmin,e+1)
    if d!=-1:
        nmin = min(nmin,d)
    return nmin

# def make_dict():
#     for item in li:
#         di_first[item]=item
#     di_first["陜西"]="陝西"

def first_layer_divide(src_path, dst1_path, dst2_path):
    with open(src_path,'r', encoding='utf-8') as f:
        data = json.load(f)
    total_dict = {}
    err_list =[]
    for item in li:
        temp= {}
        temp['name'] = item
        temp['children']= []
        total_dict[item] = temp

    for i in range(len(data)):
        item = data[i]
        if(len(item['place'])>2):
            if(item['place'][0:2] in di_first.keys()):
                temp = di_first[item['place'][0:2]]
                item['place'] =item['place'][2:]
                total_dict[temp]['children'].append(item)
            else:
                err_list.append(item)
        else:
            err_list.append(item)

    js1 = json.dumps(total_dict,ensure_ascii=False)
    js2 = json.dumps(err_list,ensure_ascii=False)

    with open(dst1_path, 'w', encoding='utf-8') as f:
        f.write(js1)
    with open(dst2_path, 'w', encoding='utf-8') as f:
        f.write(js2)

# make_dict()
# first_layer_divide('id_place.json', 'first.json', 'err_first.json')

def second_layer_divide(src_path, dst1_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    dst1 = {}
    for i in data.keys():
        dst1[i] = {}
        dst1[i]['name'] = i
        dst1[i]['children'] = {}
        save = dst1[i]['children']
        item = data[i]['children']
        for j in item:
            place = j['place']
            nmin = find_divide_place(place)
            j['place'] = place[nmin+1:]
            sub = place[:nmin+1]
            if sub not in save.keys():
                save[sub] = {}
                save[sub]['name'] = sub
                save[sub]['children'] = []
                save[sub]['children'].append(j)
            else:
                save[sub]['children'].append(j)
    
    with open(dst1_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dst1, ensure_ascii=False))

# second_layer_divide("first.json",'second.json')

def third_layer_divide(src_path, dst_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = {}
    for i in data.keys():
        result[i] = {}
        result[i]['name'] = i
        result[i]['children'] = {}
        data1 = data[i]['children']
        temp1 = result[i]['children']
        for j in data1.keys():
            temp1[j] = {}
            temp1[j]['name'] = j
            temp1[j]['children'] = {}
            data2 = data1[j]['children']
            temp2 = temp1[j]['children']
            for k in data2:
                place = k['place']
                place = place[0: find_divide_place(place)+1]
                if place not in temp2.keys():
                    temp2[place] = {}
                    temp2[place]['name'] = place
                    temp2[place]['value'] = 1
                else:
                    temp2[place]['value']+=1

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

# third_layer_divide('second.json', 'third.json')

def count_num(object):
    num = 0
    if 'value' in object.keys():
        return object['value']
    else:
        for i in object['children'].keys():
            num+=count_num(object['children'][i])
        return num

def make_dict(src_path, dst1_path,dst2_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    result= {}
    for i in data.keys():
        result[i] = {}
        data1 = data[i]['children']
        for j in data1.keys():
            data2 = data1[j]['children']
            for k in data2.keys():
                if len(k)>0:
                    result[i][k] = j
    for i in data.keys():
        data1 = data[i]['children']
        temp = []
        for j in data1.keys():
            word = j
            if word in result[i].keys():
                num = count_num(data1[j])
                temp.append(word)
                data1[result[i][word]]['children'][word]['value'] += num
        for j in temp:
            del data1[j]
    with open(dst1_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))
    with open(dst2_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

make_dict('third.json', 'dict.json', 'third_new.json')
