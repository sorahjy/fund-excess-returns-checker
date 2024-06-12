import datetime
import requests
from lxml import etree
import pandas as pd
from chinese_calendar import is_holiday
import base64

def run_citic_futures():
    currentDateAndTime = datetime.datetime.now()
    today = datetime.date.today()
    yesterday = (today + datetime.timedelta(days=-1 if currentDateAndTime.hour < 19 else 0))
    while is_holiday(yesterday) or yesterday.isoweekday() > 5:
        yesterday = yesterday + datetime.timedelta(days=-1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    print("开始计算 "+yesterday+" 的小可爱股指期货持仓...")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "br, gzip, deflate",
        "Accept-Language": "zh-cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    url = 'https://vip.stock.finance.sina.com.cn/q/view/vCffex_Positions_cjcc.php'
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    cands = html.xpath('/html/body/div[3]/form/select/option')
    futures = {"IF": [], "IC": [], "IH": [], "T": []}
    for term in [x.text for x in cands]:
        for val in futures.keys():
            if term.startswith(val):
                futures[val].append(term)
            futures[val].sort()
    print(futures)
    result_dict = {}
    for varity, specific in futures.items():
        buy_values = []
        sell_values = []
        for spec in specific:
            url = 'https://vip.stock.finance.sina.com.cn/q/view/vCffex_Positions_cjcc.php?symbol=' + spec + '&date=' + yesterday
            response = requests.get(url=url, headers=headers)
            html = etree.HTML(response.text)
            buy, sell = html.xpath('//table[@class="listT"]')[1:3]
            results = list(pd.read_html(etree.tostring(buy, encoding='utf-8').decode(), encoding='utf-8', header=0)[
                            0].T.to_dict().values())
            for json in results:
                if json['会员简称'] == base64.b64decode('5Lit5L+h5pyf6LSn').decode('utf8'):
                    buy_values.append((json['多单持仓'], json['比上交易增减']))
                    break
            results = list(pd.read_html(etree.tostring(sell, encoding='utf-8').decode(), encoding='utf-8', header=0)[
                            0].T.to_dict().values())
            for json in results:
                if json['会员简称'] == base64.b64decode('5Lit5L+h5pyf6LSn').decode('utf8'):
                    sell_values.append((json['空单持仓'], json['比上交易增减']))
                    break
        result_dict[varity] = {'多单总计': sum([x for x, _ in buy_values]), '空单总计': sum([x for x, _ in sell_values]),
                            '较昨日净多单': sum([x for _, x in buy_values]) - sum([x for _, x in sell_values])}
    IFIC = [0, 0, 0]  # 多 空 差
    for varity, data in result_dict.items():
        if varity in ["IC", "IF"]:
            IFIC[0] += data["多单总计"]
            IFIC[1] += data['空单总计']
            IFIC[2] += data['较昨日净多单']
    try:
        result_dict['IF+IC'] = {'多单总计': IFIC[0], '空单总计': IFIC[1], '较昨日净多单': IFIC[2],
                                "多空比": IFIC[0] / IFIC[1]}
        for future, statistic in result_dict.items():
            print(future, ":", statistic)
    except Exception:
        print('有误，此日期非工作日！！！')

    print('*' * 68)

if __name__ == '__main__':
    run_citic_futures()
