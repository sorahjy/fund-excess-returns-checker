import json

# 对比的指数ETF代码
compare_index = ["510310", "510580", "000914"]  #沪深300，中证500，中加纯债



# 权益类基金代码
fund = [
        #-----------   指数周期策略   -----------
        "009329",  #消费龙头         0.9%
        "010770",  #农业指数         1.5%
        "012805",  #恒生科技         4.7%
        "012323",  #中证医疗         4.1%
        "008777",  #沪深300          7.4%
        #-----------      高风险      -----------
        "001508",  #富国新动力A      6.8%
        "519702",  #交银趋势优先A    6.4%
        "005775",  #中加转型A        5.2%
        "002036",  #安信优势C        5.1%
        "001043",  #工银美丽城镇A    3.4%
        "001366",  #金鹰产业整合     3.8%
        "010728",  #中泰兴诚一年     2.8%
        #-----------      中风险      -----------
        "007509",  #华商润丰C        6.1%
        "001345",  #富国新收益A      1.1%
        "009206",  #兴银丰运C
        "519613",  #银河君尚         2.8%
        #-----------  全球及大宗商品  -----------
        "040046",  #美国纳斯达克100   8.1%
        "050025",  #美国标普500      8.4%
        "015016",  #德国DAX30        0.3%
        "539003",  #英国富时         0.3%
        "000216",  #黄金ETF          0.5%
        "014982",  #华安全球石油C          
        #-----------     二号组合     -----------    
        "002872",  #华夏智胜C        
]
# 仅监控基金经理是否更改，适合低风险偏债券基金
fund_extra = [
    "014426",   #惠升同业存单     
    "003547",   #鹏华丰禄        3.5%
    "002704",   #德邦锐兴A       3.4%
    "007744",   #长盛安逸A       4.1%
    "003859",   #招商昭旭A       
    "000914",   #中加纯债
    "006242",   #宝盈盈润
    "970132",   #东证融汇A
    "400030",   #东方添益
    "009617",   #东兴兴利C
    #----------- 上纯债，下固收+ ----------- 
    "010036",   #广发恒通A       0.0%   
    "004011",   #华泰鼎利C
    "519769",   #交银优选C       0.9%
    "002087",   #国富新机遇A     2.5%
    "002144",   #华安新优选C  
    "009078",   #红土创新C
    "164105",   #华富强化债    
    "004206",   #华商元亨        
    "008356",   #中加科丰
    "210010",   #金鹰灵活A    
]
# 香港基金，暂不支持
fund_hk = [
    "968010"   #摩根太平洋    7.9%
]

fund.extend(fund_extra)


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
