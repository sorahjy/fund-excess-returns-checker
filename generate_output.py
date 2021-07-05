import json, openpyxl
from funds import get_funds
from openpyxl.styles.colors import Color
from openpyxl.styles import PatternFill

# highlight_red = [2, 4, 8, 10, 15, 20, 20]
highlight_red = [2, 4.5, 9, 13, 20, 30, 30]
highlight_green = [-1, -0.5, 0, 1, 3, 6, 6]


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
        elif float(tmp_data[item][-2]) > 400:
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
    for item in all_funds['fund_extra']:
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
    print('*' * 68)
