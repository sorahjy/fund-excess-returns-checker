import json, openpyxl
from funds import get_funds,get_funds_bond
from openpyxl.styles.colors import Color
from openpyxl.styles import PatternFill
import datetime
import requests
from lxml import etree
import pandas as pd
from chinese_calendar import is_holiday


def convert(str):
    return float(str[:-1])


def process_item(json_file):
    code = json_file['fundCode']
    name = json_file['name']
    total_asset = json_file['fund_manager_total_asset']
    week = round(convert(json_file['netAssetValueRestoredGrowthRateRecentWeek']), 2)
    try:
        month = convert(json_file['netAssetValueRestoredGrowthRateRecentMonth']) + 100
        week2month = round(month / (week + 100) * 100 - 100, 2)
    except:
        week2month = '--'
    try:
        three_month = convert(json_file['netAssetValueRestoredGrowthRateRecentThreeMonth']) + 100
        month2three_month = round(three_month / month * 100 - 100, 2)
    except:
        month2three_month = '--'
    try:
        six_month = convert(json_file['netAssetValueRestoredGrowthRateRecentSixMonth']) + 100
        three_month2six_month = round(six_month / three_month * 100 - 100, 2)
    except:
        three_month2six_month = '--'
    try:
        year = convert(json_file['netAssetValueRestoredGrowthRateRecentOneYear']) + 100
        six_month2year = round(year / six_month * 100 - 100, 2)
    except:
        six_month2year = '--'
    try:
        two_year = convert(json_file['netAssetValueRestoredGrowthRateRecentTwoYear']) + 100
        year_2two_year = round(two_year / year * 100 - 100, 2)
    except:
        year_2two_year = '--'
    try:
        three_year = convert(json_file['netAssetValueRestoredGrowthRateRecentThreeYear']) + 100
        two_year_2three_year = round(three_year / two_year * 100 - 100, 2)
    except:
        two_year_2three_year = '--'
    return (
        code, name, week, week2month, month2three_month, three_month2six_month, six_month2year, year_2two_year,
        two_year_2three_year, total_asset, json_file['managerTrigger'])
    # 代码  名字  周  1月 3月 6月 1年 trigger


if __name__ == '__main__':
    green = Color(indexed=3, tint=0.5)
    fill_green = PatternFill('solid', fgColor=green)
    red = Color(indexed=2, tint=0.5)
    fill_red = PatternFill('solid', fgColor=red)
    tmp_data = {}
    change_manager = []
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "fund"
    with open('data/temp.json', encoding='utf8') as file:
        for line in file:
            data = json.loads(line)
            tuple = process_item(data)
            tmp_data[tuple[0]] = tuple

    # 股票基金
    highlight_red = [1.5, 3, 5, 6.5, 10, 15, 15]
    highlight_green = [-1.5, -3, -5, -6.5, -10, -15, -15]
    all_funds = get_funds()
    compare_index = all_funds['compare_index']
    title1 = ['', '', '']
    for i, index in enumerate(compare_index):
        title1.append(tmp_data[index][1])
        title1.extend(['', '', '', '', '', ''])
    title2 = ['代码', '名字', '基金经理管理规模']
    for index in compare_index:
        title2.extend(['近一周', '1周~1月', '1月~3月', '3月~6月', '6月~1年', '1年-2年', '2年-3年'])
    for i in range(len(title1)):
        worksheet.cell(1, i + 1, title1[i])
    for i in range(len(title2)):
        worksheet.cell(2, i + 1, title2[i])
    for ind, item in enumerate(all_funds['fund']):
        worksheet.cell(3 + ind, 1, item)
        worksheet.cell(3 + ind, 2, tmp_data[item][1])  # name
        asset = worksheet.cell(3 + ind, 3, tmp_data[item][-2])  # total asset
        if float(tmp_data[item][-2]) <= 100:
            asset.fill = fill_red
        elif float(tmp_data[item][-2]) > 300:
            asset.fill = fill_green
        cnt = 4
        for index in compare_index:
            for i in range(2, 9):
                try:
                    value = tmp_data[item][i] - tmp_data[index][i]
                    c = worksheet.cell(3 + ind, cnt, value)
                    if i - 2 < len(highlight_green):
                        if value < highlight_green[i - 2]:
                            c.fill = fill_green
                    if i - 2 < len(highlight_red):
                        if value > highlight_red[i - 2]:
                            c.fill = fill_red
                except:
                    worksheet.cell(3 + ind, cnt, '--')
                cnt += 1
        # 检查经理是否变更
        if '又' not in tmp_data[item][-1]:
            if int(tmp_data[item][-1][:-1]) < 20:
                change_manager.append((tmp_data[item][0], tmp_data[item][1]))
    # for item in all_funds['fund_extra']:
    #     if '又' not in tmp_data[item][-1]:
    #         if int(tmp_data[item][-1][:-1]) < 20:
    #             change_manager.append((tmp_data[item][0], tmp_data[item][1]))

    # 债券基金
    highlight_red = [0.04, 0.1, 0.3, 0.4, 0.75, 1.5, 1.5]
    highlight_green = [-0.03, 0, 0.1, 0.15, 0.25, 0.5, 0.5]
    pre_fix = 6+len(all_funds['fund'])
    all_funds = get_funds_bond()
    compare_index = all_funds['compare_index']
    title1 = ['', '', '']
    for i, index in enumerate(compare_index):
        title1.append(tmp_data[index][1])
        title1.extend(['', '', '', '', '', ''])
    title2 = ['代码', '名字', '基金经理管理规模']
    for index in compare_index:
        title2.extend(['近一周', '1周~1月', '1月~3月', '3月~6月', '6月~1年', '1年-2年', '2年-3年'])
    for i in range(len(title1)):
        worksheet.cell(pre_fix-2, i + 1, title1[i])
    for i in range(len(title2)):
        worksheet.cell(pre_fix-1, i + 1, title2[i])
    for ind, item in enumerate(all_funds['fund']):
        worksheet.cell(pre_fix + ind, 1, item)
        worksheet.cell(pre_fix+ ind, 2, tmp_data[item][1])  # name
        asset = worksheet.cell(pre_fix + ind, 3, tmp_data[item][-2])  # total asset
        if float(tmp_data[item][-2]) <= 100:
            asset.fill = fill_red
        elif float(tmp_data[item][-2]) > 300:
            asset.fill = fill_green
        cnt = 4
        for index in compare_index:
            for i in range(2, 9):
                try:
                    value = tmp_data[item][i] - tmp_data[index][i]
                    c = worksheet.cell(pre_fix + ind, cnt, value)
                    if i - 2 < len(highlight_green):
                        if value < highlight_green[i - 2]:
                            c.fill = fill_green
                    if i - 2 < len(highlight_red):
                        if value > highlight_red[i - 2]:
                            c.fill = fill_red
                except:
                    worksheet.cell(pre_fix + ind, cnt, '--')
                cnt += 1
        # 检查经理是否变更
        if '又' not in tmp_data[item][-1]:
            if int(tmp_data[item][-1][:-1]) < 20:
                change_manager.append((tmp_data[item][0], tmp_data[item][1]))

    worksheet.column_dimensions['B'].width = 32
    worksheet.column_dimensions['C'].width = 20
    workbook.save(filename='fund.xlsx')
    print('*' * 30, 'result', '*' * 30)
    print('处理完毕，文件fund.xlsx已经输出。')
    if not change_manager:
        print('经检查，近20天内列表中基金的经理没有更换。')
    else:
        print('经检查，近20天以下基金的经理发生了人事变动：')
        for tuple in change_manager:
            print(tuple)
    print('*' * 29, '中信期指' ,'*' * 29)

    ###### new feature: 爬取中信期指
    currentDateAndTime = datetime.datetime.now()
    today = datetime.date.today()
    yesterday = (today + datetime.timedelta(days=-1 if currentDateAndTime.hour < 19 else 0))
    while is_holiday(yesterday) or yesterday.isoweekday() > 5:
        yesterday = yesterday + datetime.timedelta(days=-1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    print("开始计算 "+yesterday+" 的中信股指期货持仓...")
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
    futures = {"IF": [], "IC": [], "IH": [], }
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
                if json['会员简称'] == '中信期货':
                    buy_values.append((json['多单持仓'], json['比上交易增减']))
                    break
            results = list(pd.read_html(etree.tostring(sell, encoding='utf-8').decode(), encoding='utf-8', header=0)[
                            0].T.to_dict().values())
            for json in results:
                if json['会员简称'] == '中信期货':
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

