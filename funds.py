import json

# 对比的指数基金代码
compare_index = ["510310", "510580"]  #沪深300，中证500

# 权益类基金代码
fund = [
        "010728",  #中泰一年
        "009375",  #MSCI_CHN_INDEX
        "000006",  #西部量化A
        "002340",  #富国价值优势
        "003962",  #易方达瑞程C
        "519702",  #交银趋势优先A
        "470098",  #汇添富逆向
        "009708",  #工银新兴制造C
        "001043",  #工银美丽城镇A
        "008276",  #财通价值发现A
        "002846",  #弘德泓华
        "008245",  #圆信致优A
        "160813",  #长盛成长优选
        "040011",  #华安核心优选
        "163409",  #兴全绿色
        "550015",  #中信至远A
        #----------- 下面是美股指数 -----------
        "040046",  #华安纳斯达克100
        "050025",  #博时标普500
]
# 仅监控基金经理是否更改，适合偏债券基金
fund_extra = [
    "003547",   #鹏华丰禄
    "003859",   #招商昭旭A
    "006966",   #财通安瑞C
    "007744",   #长盛安逸A
    "000914",   #中加纯债
    "003429",   #兴业高级债指
    #----------- 上纯债，下固收+ -----------
    "001182",   #易方达安心
    "519768",   #交银优选A  
    "000171",   #易方达裕丰
    "002742",   #泓德裕祥A
    "008356",   #中加科丰
    "002087",   #国富新机遇A
    "002144",   #华安新优选C
    "003154",   #华宝新活力
    "003849",   #中银广利C
    "013260",   #太平睿享A
    "002935"    #泰康恒泰C
]
# 香港基金，暂不支持
fund_hk = [
    "968075",  #百达策略收益
    "968010"   #摩根太平洋
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
