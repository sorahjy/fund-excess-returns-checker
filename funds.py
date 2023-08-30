import json

# 对比的中高风险基金
compare_index = ["510310", "510580" ]  #沪深300，中证500，

# 对比的中低风险基金
compare_index_bond = ["161119", "519769"]  #债券综指,交银固收+

hold_index = ["008155", "008115", "010769", "008929", "161028", "012805","015877"]
# 中高风险基金代码
fund_index = [
        #-----------   策略指数     -----------11111111
        "015877",  #消费电子C
        "008929",  #泰达宏利消费红利C
        "008155",  #嘉实医药100策略C
        "011133",  #鹏扬沪深300质量成长低波C
        "008115",  #天弘红利低波100C
        #-----------   价值指数     -----------
        "007785",  #广发央企创新C
        "257060",  #上证大宗商品C|015577  
        "159876",  #华宝有色C|017141
        "017057",  #嘉实绿电C
        "167301",  #方正富邦保险
        "012645",  #建信券商C|012646
        "010769",  #天弘农业C|010770
        "005224",  #广发基建C
        "001595",  #天弘银行C
        "004642",  #南方房地产C|010989     
        "159766",  #旅游（场内） 
        "516010",  #国泰动漫游戏C|012729
        "004752",  #广发传媒C|004753
        "516020",  #华宝化工C|012538
        #-----------   成长指数     -----------
        "001630",  #天弘计算机C
        "159996",  #富国家电C|017227
        "160632",  #鹏华酒C|012043
        "161028",  #嘉实新能源C|012544      
        "011103",  #天弘光伏C 
        "588080",  #易方达科创50|011609
        "005693",  #广发军工C              
        "008888",  #芯片半导体C|012970      
        "162412",  #华宝中证医疗C|012323    
        "016892",  #鹏华中药C
        "513360",  #教育（场内）
        "014425",  #博时恒生医疗C          
        "012805",  #广发恒生科技C          
        #-----------   宽基指数     -----------
        "008777",  #沪深300               
        "007029",  #中证500                     
]
fund_stock = [ 
        #-----------  量化基金  -----------
        "000006",  #西部利得量化A
        "016466",  #国泰君安量化A      
        #-----------  主动基金  -----------
        "001508",  #富国新动力A      
        "010447",  #中邮未来成长A      
        "014038",  #交银启诚         
        #-----------  全球指数  -----------
        "040046",  #美国纳斯达克100   
        "050025",  #美国标普500      
        "014982",  #标普石油     
        #-----------  大宗商品  -----------
        "000216",  #黄金             
        "006476",  #原油             
           
]
fund = fund_index + fund_stock

# 中低风险基金代码
fund_bond = [
    #-----------      固收+     ----------- 
    "010036",   #广发恒通A       
    "009078",   #红土创新C       
    "002058",   #中银新机遇C
    "001422",   #景顺安享A    
    "010658",   #海富通欣睿C   
    #-----------      混债      -----------
    "217024",   #招商安盈A     
    #-----------      纯债       -----------   
    "161119",   #债券综指A       
    #-----------      监控      -----------
    "004206",   #华商元亨        
    "002015",   #南方荣光        
    "012324",   #兴证30天超短A       
    "210010",   #金鹰灵活A
]

# fund.extend(fund_bond)

def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'hold_index': hold_index}

def get_funds_bond():
    return {'compare_index': compare_index_bond, 'fund': fund_bond }

if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index +compare_index_bond+ fund + fund_bond)), fin)
