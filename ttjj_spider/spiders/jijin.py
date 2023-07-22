# -*- coding: utf-8 -*-
import scrapy
import os
import json,time,random
from lxml import etree
from ttjj_spider.items import MyItem
import requests

class JijinSpider(scrapy.Spider):
    name = 'jijin'
    allowed_domains = ['fund.eastmoney.com', 'fundf10.eastmoney.com']

    data_dir = os.path.join('.', 'data')
    fund_codes_file = os.path.join(data_dir, 'fund_codes.json')
    with open(fund_codes_file, 'r', encoding='utf-8') as fin:
        fund_codes = json.load(fin)
    start_urls = ['http://fund.eastmoney.com/{}.html'.format(code) for code in fund_codes]

    handle_httpstatus_list = [404, 500]

    def parse(self, response):
        my_item = MyItem()


        jjjl_url=''
        if response.status == 200:
            html = etree.HTML(response.text)

            my_item['name'] = html.xpath('//div[@class="fundDetail-tit"]/div[1]/text()')
            my_item['fundCode']=html.xpath('//*[@id="body"]/div[11]/div/div/div[1]/div[1]/div//span[@class="ui-num"]/text()')[0]
            my_item['managerTrigger'] = html.xpath('//*[@id="fundManagerTab"]//td[@class="td03"]/text()')[0]
            if len(my_item['name']) != 0 \
                    and html.xpath('//div[@class="fundInfoItem"]/div[1]/@class')[0] != 'tuishiTip':
                    # and ''.join(html.xpath('//dl[@class="dataItem01"]//span[@class="sp01"]/text()')) == '净值估算' 
                my_item['name'] = my_item['name'][0]
                my_item['netAssetValueEstimated'] = ''.join(html.xpath('//dl[@class="dataItem01"]/dd[1]/dl[1]/span/text()'))  # 估算净值
                my_item['netAssetValue'] = ''.join(html.xpath('//dl[@class="dataItem02"]/dd[1]/span[1]/text()'))  # 单位净值
                my_item['netAssetValueAccumulated'] = ''.join(html.xpath('//dl[@class="dataItem03"]/dd[1]/span/text()'))  # 累计净值
                my_item['riskRating'] = ''.join(html.xpath('//div[@class="infoOfFund"]/table/tr[2]/td[3]/div/@class'))  # 基金评级

                for row in html.xpath('//*[@id="increaseAmount_stage"]/table/tr[position()>1]'):
                    title = ''.join(row.xpath('./td[1]/div/text()'))
                    if title.startswith('阶段涨幅'):
                        key = 'netAssetValueRestoredGrowthRate'
                    elif title.startswith('同类平均'):
                        key = 'categoryAverageOfNetAssetValueRestoredGrowth'
                    elif title.startswith('沪深300'):
                        key = 'hs300GrowthRate'
                    elif title.startswith('同类排名'):
                        key = 'rankInCategoryOfNetAssetValueRestoredGrowth'
                    elif title.startswith('四分位排名'):
                        key = 'quartileRankInCategoryOfNetValueRestoredGrowth'
                    else:
                        key = ''

                    if key == 'quartileRankInCategoryOfNetValueRestoredGrowth':
                        my_item['{}RecentWeek'.format(key)] = ''.join(row.xpath('./td[2]/h3/text()'))
                        my_item['{}RecentMonth'.format(key)] = ''.join(row.xpath('./td[3]/h3/text()'))
                        my_item['{}RecentThreeMonth'.format(key)] = ''.join(row.xpath('./td[4]/h3/text()'))
                        my_item['{}RecentSixMonth'.format(key)] = ''.join(row.xpath('./td[5]/h3/text()'))
                        my_item['{}RecentOneYear'.format(key)] = ''.join(row.xpath('./td[7]/h3/text()'))
                        my_item['{}RecentTwoYear'.format(key)] = ''.join(row.xpath('./td[8]/h3/text()'))
                        my_item['{}RecentThreeYear'.format(key)] = ''.join(row.xpath('./td[9]/h3/text()'))
                        my_item['{}SinceFirstDayOfYear'.format(key)] = ''.join(row.xpath('./td[6]/h3/text()'))
                    elif key != '':
                        my_item['{}RecentWeek'.format(key)] = ''.join(row.xpath('./td[2]/div/text()'))
                        my_item['{}RecentMonth'.format(key)] = ''.join(row.xpath('./td[3]/div/text()'))
                        my_item['{}RecentThreeMonth'.format(key)] = ''.join(row.xpath('./td[4]/div/text()'))
                        my_item['{}RecentSixMonth'.format(key)] = ''.join(row.xpath('./td[5]/div/text()'))
                        my_item['{}RecentOneYear'.format(key)] = ''.join(row.xpath('./td[7]/div/text()'))
                        my_item['{}RecentTwoYear'.format(key)] = ''.join(row.xpath('./td[8]/div/text()'))
                        my_item['{}RecentThreeYear'.format(key)] = ''.join(row.xpath('./td[9]/div/text()'))
                        my_item['{}SinceFirstDayOfYear'.format(key)] = ''.join(row.xpath('./td[6]/div/text()'))

            jjjl_url = html.xpath('//*[@id="fundManagerTab"]//td[@class="td02"]//a/@href')[:1]

        if jjjl_url:
            hea = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
            html = etree.HTML(requests.get(jjjl_url[0], headers=hea).text)
            my_item['fund_manager_total_asset'] = \
            html.xpath('/html/body/div[6]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/span[2]/span[1]/text()')[0]
            yield my_item
        else:
            my_item['fund_manager_total_asset'] = 99999
            yield my_item

