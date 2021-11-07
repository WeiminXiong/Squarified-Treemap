import json

def process_fu_data(si_data):
    fu_data = []
    num_fu = {}
    for data_item in si_data['children']:
        fu = data_item[:2]
        jiguan = data_item[2:]

        if len(fu) > 0 and (fu[0] == "府" or fu[0] == "縣"):
            fu = fu[1:] + jiguan[0]
            jiguan = jiguan[1:]
        if len(jiguan) > 0 and jiguan[0] == "州":
            fu = fu + "州"
            jiguan = jiguan[1:]
        if len(jiguan) > 0 and jiguan[0] == "府":
            jiguan = jiguan[1:]

        if si_data["name"] == "北直隸":
            if fu == "北平":
                fu = "順天"
        elif si_data["name"] == "南直隸":
            if fu == "盧州":
                fu = "廬州"
            elif fu == "懷安":
                fu = "淮安"
            elif fu == "楊州":
                fu = "揚州"
            elif fu == "寍國":
                fu = "寧國"
        elif si_data["name"] == "陝西":
            if fu in ["同州", "盩厔", "長安", "醴泉", "華陰", "涇陽", "藍田", "咸寧", "臨潼", "商州", "朝邑"]:
                jiguan = fu + jiguan
                fu = "西安"
            elif fu == "郃陽" or fu == "澄城":
                jiguan = "同州" + fu + jiguan
                fu = "西安"
            elif jiguan == "涇陽縣":
                fu = "西安"
            elif fu == "平凉":
                fu = "平涼"
            elif fu == "岐山":
                jiguan = fu + jiguan
                fu = "鳳翔"
            elif fu == "宜川":
                jiguan = fu + jiguan
                fu = "延安"
            elif fu == "狄道":
                jiguan = fu + jiguan
                fu = "臨洮"
            elif fu in ["神木", "寧州", "行都"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "山西":
            if fu == "潞州":
                fu = "潞安"
            elif fu == "澤洲":
                fu = "澤州"
            elif fu == "汾洲":
                fu = "汾州"
            elif fu in ["平定州", "陽曲", "榆次", "代州", "文水", "清源", "石州", "太谷", "忻州"]:
                jiguan = fu + jiguan
                fu = "太原"
            elif fu in ["太平", "臨汾", "稷山", "猗氏", "蒲州", "萬泉", "襄陵", "安邑", "洪洞", "絳州", "平陸", "夏縣", "趙城", "臨晉"]:
                jiguan = fu + jiguan
                fu = "平陽"
            elif fu in ["陵川", "黎城", "潞城", "襄垣"]:
                jiguan = fu + jiguan
                fu = "潞安"
            elif fu in ["蔚州", "渾源州", "懷仁", "應州", "馬邑"]:
                jiguan = fu + jiguan
                fu = "大同"
            elif fu in ["孝義"]:
                jiguan = fu + jiguan
                fu = "汾州"
            elif fu in ["靈川"]:
                jiguan = fu + jiguan
                fu = "澤州"
            elif fu in ["榆社"]:
                jiguan = fu + jiguan
                fu = "遼州"
            elif fu in ["都司", "臨縣", "望成", "壼關", "廣靈", "隰州", "文山", "儀衛"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "山東":
            if fu == "兗州" or fu == "兊州" or fu == "袞州":
                fu = "兖州"
            elif fu == "暨州":
                fu = "登州"
            elif fu == "青洲":
                fu = "青州"
            elif fu == "菜州":
                fu = "萊州"
            elif fu in ["東平", "濟寧州", "單縣", "滕縣", "汶上", "曹縣", "東平州", "泰安", "曹州"]:
                jiguan = fu + jiguan
                fu = "兖州"
            elif fu in ["日照", "沂水", "莒州", "高苑", "諸城", "臨朐", "益都", "安丘"]:
                jiguan = fu + jiguan
                fu = "青州"
            elif fu in ["武定州", "歷城", "齊河", "濱州", "德州", "平原", "長山", "禹城", "淄川", "齊東"]:
                jiguan = fu + jiguan
                fu = "濟南"
            elif fu in ["館陶", "恩縣", "濮州"]:
                jiguan = fu + jiguan
                fu = "東昌"
            elif fu in ["昌邑", "掖縣", "膠州", "平度州"]:
                jiguan = fu + jiguan
                fu = "萊州"
            elif fu in ["蓬萊", "萊陽", "黃縣", "招遠", "文登"]:
                jiguan = fu + jiguan
                fu = "登州"
            elif fu in ["□"]:
                jiguan = fu + jiguan
                fu = "其他"
            elif fu == "貴州":
                fu = "青州"
                jiguan == "日照縣"
        elif si_data["name"] == "河南":
            if fu == "汝寕" or fu == "汝寍":
                fu = "汝寧"
            elif fu == "懷德":
                fu = "懷慶"
            elif fu == "開州" or fu == "開府":
                fu = "開封"
            elif fu in ["陝州", "洛陽", "孟津", "靈寶", "偃師", "嵩縣"]:
                jiguan = fu + jiguan
                fu = "河南"
            elif fu in ["光州", "信陽州", "息縣", "固始", "上蔡"]:
                jiguan = fu + jiguan
                fu = "汝寧"
            elif fu in ["祥符", "郾城" ,"夏邑", "扶溝", "太康", "歸德", "歸德州", "陳留", "鹿邑", "項城", "蘭陽", "封丘"]:
                jiguan = fu + jiguan
                fu = "開封"
            elif fu in ["汝州", "郟縣", "裕州", "唐縣"]:
                jiguan = fu + jiguan
                fu = "南陽"
            elif fu in ["獲嘉", "汲縣"]:
                jiguan = fu + jiguan
                fu = "衛輝"
            elif fu in ["□", "信陽", "□□"]:
                jiguan = fu + jiguan
                fu = "其他"
            elif fu == "南陽" and jiguan == "洛陽縣":
                fu = "河南"
        elif si_data["name"] == "浙江":
            if fu == "明州" or fu == "寍波" or fu == "寧江":
                fu = "寧波"
            elif fu == "温州" or fu == "知州":
                fu = "溫州"
            elif fu == "巖州":
                fu = "嚴州"
            elif fu == "照興":
                fu = "紹興"
            elif fu == "今華":
                fu = "金華"
            elif fu in ["仁和", "錢塘", "臨安", "海寧"]:
                jiguan = fu + jiguan
                fu = "杭州"
            elif fu in ["西安", "開化", "常山", "龍游"]:
                jiguan = fu + jiguan
                fu = "衢州"
            elif fu in ["鄞縣", "定海", "慈谿"]:
                jiguan = fu + jiguan
                fu = "寧波"
            elif fu in ["山陰", "餘姚", "蕭山", "會稽", "上虞", "嵊縣", "餘杭", "諸暨"]:
                jiguan = fu + jiguan
                fu = "紹興"
            elif fu in ["景寧", "麗水", "遂昌"]:
                jiguan = fu + jiguan
                fu = "處州"
            elif fu in ["海鹽", "崇德", "秀水", "平湖", "桐鄉"]:
                jiguan = fu + jiguan
                fu = "嘉興"
            elif fu in ["天台", "臨海", "黃巖", "寧海"]:
                jiguan = fu + jiguan
                fu = "台州"
            elif fu in ["安吉", "長興", "烏程", "德清"]:
                jiguan = fu + jiguan
                fu = "湖州"
            elif fu in ["建德"]:
                jiguan = fu + jiguan
                fu = "嚴州"
            elif fu in ["蘭谿", "義烏", "東陽"]:
                jiguan = fu + jiguan
                fu = "金華"
            elif fu in ["瑞安", "永嘉"]:
                jiguan = fu + jiguan
                fu = "溫州"
            elif fu in ["新城", "□縣", "□□", "慶元", "黃岩"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "江西":
            if fu == "康定":
                fu = "南康"
            elif fu == "臨州":
                fu = "瑞州"
            elif fu == "隴江" or fu == "臨安":
                fu = "臨江"
            elif fu == "廣州":
                fu = "廣信"
            elif fu == "饒洲":
                fu = "饒州"
            elif fu in ["吉水", "廬陵", "龍泉", "安福", "泰和", "永豐", "萬安", "吉永"]:
                jiguan = fu + jiguan
                fu = "吉安"
            elif fu in ["興國", "贛縣"]:
                jiguan = fu + jiguan
                fu = "贛州"
            elif fu in ["鄱陽", "安仁", "樂平", "餘干", "浮梁"]:
                jiguan = fu + jiguan
                fu = "饒州"
            elif fu in ["新淦", "新喻", "清江", "峽江"]:
                jiguan = fu + jiguan
                fu = "臨江"
            elif fu in ["新建", "進賢", "豐城", "武寧"]:
                jiguan = fu + jiguan
                fu = "南昌"
            elif fu in ["臨川", "樂安", "崇仁", "金谿"]:
                jiguan = fu + jiguan
                fu = "撫州"
            elif fu in ["宜春", "萍鄉"]:
                jiguan = fu + jiguan
                fu = "袁州"
            elif fu in ["南豐"]:
                jiguan = fu + jiguan
                fu = "建昌"
            elif fu in ["貴溪"]:
                jiguan = fu + jiguan
                fu = "廣信"
            elif fu in ["高安"]:
                jiguan = fu + jiguan
                fu = "瑞州"
            elif fu in ["大庾", "大臾"]:
                jiguan = fu + jiguan
                fu = "南安"
            elif fu in ["德化"]:
                jiguan = fu + jiguan
                fu = "九江"
            elif fu in ["□", "眉州", "□縣", "□□", "上猶"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "湖廣":
            if fu == "溪州":
                fu = "衡州"
            elif fu == "民昌":
                fu = "武昌"
            elif fu == "黄州" or fu == "黃洲":
                fu = "黃州"
            elif fu == "寶應":
                fu = "寶慶"
            elif fu in ["安陸州", "沔陽州", "京山", "安陸"]:
                jiguan = fu + jiguan
                fu = "承天"
            elif fu in ["茶陵", "攸縣", "湘陰", "湘鄉", "茶陵州"]:
                jiguan = fu + jiguan
                fu = "長沙"
            elif fu in ["桂陽", "衡山", "酃縣"]:
                jiguan = fu + jiguan
                fu = "衡州"
            elif fu in ["漢川"]:
                jiguan = fu + jiguan
                fu = "漢陽"
            elif fu in ["桃源", "龍陽"]:
                jiguan = fu + jiguan
                fu = "常德"
            elif fu in ["盧溪", "湘潭"]:
                jiguan = fu + jiguan
                fu = "辰州"
            elif fu in ["蒲圻" ,"嘉魚", "大冶", "江夏"]:
                jiguan = fu + jiguan
                fu = "武昌"
            elif fu in ["巴陵"]:
                jiguan = fu + jiguan
                fu = "岳州"
            elif fu in ["黃岡", "黃梅", "羅田", "麻城", "黃崗", "黃陂", "蘄州"]:
                jiguan = fu + jiguan
                fu = "黃州"
            elif fu in ["夷陵州", "江陵", "監利", "公安"]:
                jiguan = fu + jiguan
                fu = "荊州"
            elif fu in ["零陵"]:
                jiguan = fu + jiguan
                fu = "永州"
            elif fu in ["雲夢"]:
                jiguan = fu + jiguan
                fu = "德安"
            elif fu in ["□州", "鄖陽"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "四川":
            if fu == "嘉定州":
                fu = "嘉定"
            elif fu == "叙州":
                fu = "敘州"
            elif fu == "虁州":
                fu = "夔州"
            elif fu == "潼川州" or fu == "潼州州":
                fu = "潼川"
            elif fu == "":
                fu = ""
            elif fu in ["眉州"]:
                jiguan = fu + jiguan
                fu = "嘉定"
            elif fu in ["巴縣"]:
                jiguan = fu + jiguan
                fu = "重慶"
            elif fu in ["安岳"]:
                jiguan = fu + jiguan
                fu = "潼川"
            elif fu in ["閬中"]:
                jiguan = fu + jiguan
                fu = "保寧"
            elif fu in ["綿州", "內江", "德陽"]:
                jiguan = fu + jiguan
                fu = "成都"
            elif fu in ["富順"]:
                jiguan = fu + jiguan
                fu = "敘州"
            elif fu in ["合江"]:
                jiguan = fu + jiguan
                fu = "瀘州"
            elif fu in ["永寧", "卭州", "雅州"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "廣東":
            if fu == "廣東":
                fu = "廣州"
            elif fu in ["吳川", "茂名"]:
                jiguan = fu + jiguan
                fu = "高州"
            elif fu in ["番禺", "東莞", "新會"]:
                jiguan = fu + jiguan
                fu = "廣州"
            elif fu in ["高要", "四會"]:
                jiguan = fu + jiguan
                fu = "肇慶"
            elif fu in ["□", "□□", "恩平"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "福建":
            if fu == "汀洲":
                fu = "汀州"
            elif fu == "廷平":
                fu = "延平"
            elif fu in ["莆田"]:
                jiguan = fu + jiguan
                fu = "興化"
            elif fu in ["沙縣", "尤溪", "永安"]:
                jiguan = fu + jiguan
                fu = "延平"
            elif fu in ["閩縣", "懷安", "福清", "連江", "長樂"]:
                jiguan = fu + jiguan
                fu = "福州"
            elif fu in ["建安", "崇安"]:
                jiguan = fu + jiguan
                fu = "建寧"
            elif fu in ["同安", "晉江", "惠安"]:
                jiguan = fu + jiguan
                fu = "泉州"
            elif fu in ["□□", "□州", "□", "", "政和", "清縣"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "貴州":
            if fu in ["貴州", "宣慰"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "雲南":
            if fu == "太理":
                fu = "大理"
            elif fu in ["嵩明州", "安寧州"]:
                jiguan = fu + jiguan
                fu = "雲南"
            elif fu in ["□", "霑益州"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "交阯":
            if fu == "交阯":
                fu = "交州"
            elif fu in ["多翼"]:
                jiguan = fu + jiguan
                fu = "新安"
            elif fu in ["扶寧"]:
                jiguan = fu + jiguan
                fu = "交州"
            elif fu in [""]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "衛所":
            jiguan = fu + jiguan
            if jiguan[-1] == "衛":
                fu = "衛"
            elif jiguan[-1] == "所":
                fu = "所"
        elif si_data["name"] == "未知":
            jiguan = fu + jiguan
            fu = "未知"
        
        a = jiguan.find("縣")
        if(a!=-1):
            xian = jiguan[0:a]
            temp = jiguan[a:]
        else:
            xian = jiguan
            temp = ""
        
        if xian == "盧陵":
            xian = "廬陵"
        if xian == "臨川新喻":
            xian = "臨川"
        if xian == "豐誠":
            xian = "豐城"
        elif xian == "寍州":
            xian = "寧州"
        elif xian == "進贒":
            xian = "進賢"
        elif xian == "南昌府進賢":
            xian = "進賢"
        if xian == "大臾":
            xian = "大庾"
        if xian == "趙珹":
            xian = "趙城"
        if xian == "撫平定州":
            xian = "平定州"
        elif xian[:2] == "岢嵐":
            xian = "岢嵐"
        elif xian == "代州四關一廂" or xian == "代州王里一都" or xian == "代縣":
            xian = "代州"
        if xian == "諸暨西安鄉六十五都":
            xian = "諸暨"
        if xian == "大台":
            xian = "天台"
        if xian == "海塩":
            xian = "海鹽"
        elif xian == "撫平湖縣":
            xian = "平湖"
        if xian == "安吉州":
            xian = "安吉"
        if xian == "閔縣":
            xian = "閩縣"
        elif xian == "官府長樂縣":
            xian = "長樂"
        if xian == "浦田" or xian == "圃田" or xian == "蒲田":
            xian = "莆田"
        elif xian == "遷遊" or xian == "仙游":
            xian = "仙遊"
        if xian == "普江":
            xian = "晉江"
        if xian == "漳蒲" or xian == "彰浦":
            xian = "漳浦"
        if xian == "金州":
            xian = "全州"
        if xian == "欎林州南廂第一圖":
            xian = "鬱林"
        if xian == "鄧州內鄉縣上白亭保":
            xian = "鄧州"
        elif xian == "汝川壽永鄉西八里保":
            xian = "汝州"
        if xian[:2] == "歸德":
            xian = "歸德"
        elif xian == "許州襄城":
            xian = "許州"
        elif xian == "祥府":
            xian = "祥符"
        elif xian == "雎州":
            xian = "睢州"
        if xian == "陜州":
            xian = "陝州"
        elif xian == "永寍":
            xian = "永寧"
        if xian == "信陽州":
            xian = "信陽"
        if xian == "東菀" or xian == "東筦":
            xian = "東莞"
        if xian == "衛軍":
            xian = "其他"
        elif xian == "慱羅":
            xian = "博羅"
        if xian == "華洲渭南縣":
            xian = "華州"
        elif xian == "盩屋":
            xian = "盩厔"
        elif xian[:2] == "乾州" or xian[:2] == "乾洲":
            xian = "乾州"
        if xian[:2] == "綏德":
            xian = "綏德"
        if xian == "寶鷄":
            xian = "寶雞"
        if xian == "會寍":
            xian = "會寧"
        elif xian == "縣隴西縣":
            xian = "隴西"
        if xian == "江府陰縣" or xian == "江隂":
            xian = "江陰"
        if xian == "崐山":
            xian = "崑山"
        elif xian == "太倉州":
            xian = "太倉"
        elif xian == "長熟":
            xian = "常熟"
        elif xian == "常州":
            xian = "長洲"
        elif xian == "大倉":
            xian = "太倉"
        elif xian == "嘉定榮縣":
            xian = "嘉定"
        if xian == "石碌":
            xian = "石埭"
        if xian == "漂陽":
            xian = "溧陽"
        if xian == "沐陽":
            xian = "沭陽"
        if xian == "無為州":
            xian = "無為"
        if xian == "宿州靈璧":
            xian = "宿州"
        elif xian == "潁州":
            xian = "頴州"
        elif xian == "亳州":
            xian = "毫州"
        if xian == "高郵州":
            xian = "高郵"
        if xian == "休寍":
            xian = "休寧"
        if xian == "大平":
            xian = "太平"
        if xian == "蠡州" or xian == "縣蠡":
            xian = "蠡縣"
        elif xian == "愽野":
            xian = "博野"
        if xian == "渭縣":
            xian = "魏縣"
        if xian == "藳城" or xian == "藁縣":
            xian = "藁城"
        if xian == "昌平州":
            xian = "昌平"
        elif xian == "州寶坻縣":
            xian = "寶坻"
        if xian == "廬龍":
            xian = "盧龍"
        elif xian == "欒州":
            xian = "灤州"
        if xian[:2] == "東平":
            xian = "東平"
        elif xian[:2] == "濟寧":
            xian = "濟寧"
        elif xian[:2] == "泰安":
            xian = "泰安"
        if xian == "武定州":
            xian = "武定"
        elif xian == "濟東":
            xian = "齊東"
        elif xian == "泰安州":
            xian = "泰安"
        if xian == "菖州":
            xian = "莒州"
        elif xian == "臨胊":
            xian = "臨朐"
        if xian == "寧海州":
            xian = "寧海"
        elif xian == "菜陽":
            xian = "萊陽"
        if xian == "平度州":
            xian = "平度"
        if xian[:2] == "臨清":
            xian = "臨清"
        elif xian == "唐邑" or xian == "堂巴":
            xian = "堂邑"
        elif xian == "高唐州":
            xian = "高唐"
        elif xian == "荏平":
            xian = "茌平"
        elif xian == "愽平":
            xian = "博平"
        if xian == "江律":
            xian = "江津"
        if xian == "温江":
            xian = "溫江"
        elif xian == "重慶州" or xian == "崇慶州四安鄉":
            xian = "崇慶"
        elif xian == "漢川":
            xian = "漢州"
        elif xian == "後衛新都驛":
            xian = "新都"
        if xian == "廣安州":
            xian = "廣安"
        elif xian == "南𠑽":
            xian = "南充"
        if xian == "劔州" or xian == "劒州":
            xian = "劍州"
        elif xian == "巴州":
            xian = "巴縣"
        if xian == "桂楊":
            xian = "桂陽"
        if xian[:2] == "沔陽":
            xian = "沔陽"
        elif xian == "潜江":
            xian = "潛江"
        if xian == "華密":
            xian = "華容"
        if xian == "随州":
            xian = "隨州"

        jiguan = xian+temp
        if jiguan.find("縣")!=-1:
            jiguan = jiguan[:jiguan.find("縣")+1]


        if fu not in num_fu:
            num_fu[fu] = 1
            fu_data.append(
                (
                    {
                        "name": fu,
                        "children": [jiguan],
                        # "value": 1
                    }
                )
            )
        else:
            num_fu[fu] += 1
            for fu_item in fu_data:
                if fu_item["name"] == fu:
                    fu_item["children"].append(jiguan)
                    # fu_item["value"] += 1
                    break
    return fu_data
    
with open("si_data.json",'r', encoding='utf-8') as f:
    data = json.load(f)
for item in data:
    item['children'] = process_fu_data(item)
with open("fu_data.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False))

