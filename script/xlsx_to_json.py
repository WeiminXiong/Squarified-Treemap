import json
from os import name
import xlrd

def xlsx_to_json(src_path, dst_path):
    wb = xlrd.open_workbook(src_path)
    namelist = []
    sheet = wb.sheet_by_index(0)
    for i in  range(1, sheet.nrows):
        namedict = {}
        namedict['id'] = sheet.cell_value(i, 0)
        namedict['place'] = sheet.cell_value(i, 9)
        # print(namedict['place'])
        if(len(namedict['place'])>2 and '□' not in namedict['place']):
            if(namedict['place'][-1]=='人'):
                namedict['place'] = namedict['place'][:-1]
            namelist.append(namedict)
    j = json.dumps(namelist,ensure_ascii= False)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(j)

xlsx_to_json("ming_jinshilu_52y_release.xls", "id_place.json")
