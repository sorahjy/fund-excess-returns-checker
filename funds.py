import json

# 对比的中高风险基金
compare_index = ["510310", "510580" ]  #沪深300，中证500，

# 对比的中低风险基金
compare_index_bond = ["161119", "519769"]  #债券综指,交银固收+



# 中高风险基金代码
fund = [
        #-----------      指数型      -----------
        "012043",  #酒C              0.4%
        "005693",  #广发军工C        0.4%
        "012970",  #芯片半导体       2.4%
        "012805",  #恒生科技         4.1%
        "012323",  #中证医疗         3.1%
        "006705",  #MSCI A股        2.1%
        "008777",  #沪深300          1.4%
        "007209",  #中证500          1.4%
        #-----------      高风险      -----------
        "001508",  #富国新动力A      5.8%
        "519702",  #交银趋势优先A    5.8%
        "005775",  #中加转型A        5.2%
        "002036",  #安信优势C        5.1%
        "010728",  #中泰兴诚一年     2.8%
        #-----------      中风险      -----------
        "007509",  #华商润丰C        7.1%
        "001345",  #富国新收益A      7.0%
        "009206",  #兴银丰运C        3%      
        #-----------  全球及大宗商品  -----------
        "040046",  #美国纳斯达克100   9.1%
        "050025",  #美国标普500      9.4%
        "000216",  #黄金             1.6%
        "014982",  #全球石油                
]
# 中低风险基金代码
fund_bond = [
    #-----------      固收+     ----------- 
    "010036",   #广发恒通A       3.0%   
    "004011",   #华泰鼎利C       1.0% 
    "009078",   #红土创新C       1.0% 
    "002015",   #南方荣光        1.4%
    "002058",   #中银新机遇C
    "001422",   #景顺安享A    
    #-----------      混债      -----------
    "164105",   #华富强化债
    "217024",   #招商安盈A     
    #-----------      纯债       -----------   
    "161119",   #债券综指A       2.1%
    "003547",   #鹏华丰禄        3.9%
    "011489",   #创金双季A       1.4%
    "007744",   #长盛安逸A       5.1%
    "006242",   #宝盈盈润        1.4%
    #-----------      监控      -----------
    "240003",   #华宝宝康A  
    "003859",   #招商昭旭A     
    "000914",   #中加纯债  
    "004206",   #华商元亨        
    "008356",   #中加科丰
    "210010",   #金鹰灵活A
]

# fund.extend(fund_bond)
fund_lc = [
    "004010", #华泰柏瑞鼎利A
    "003591", #华泰柏瑞享利A
    "002058", #中银新机遇C
    "002502", #中银腾利A
    "002146", #长安鑫益增强A
    "004045", #金鹰添润定开
    "000552", #中加纯债一年A
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund}

def get_funds_bond():
    return {'compare_index': compare_index_bond, 'fund': fund_bond }

if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index +compare_index_bond+ fund + fund_bond)), fin)
