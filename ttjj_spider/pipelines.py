# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
# from pymongo import MongoClient


# def connect_db(config_file):
#     with open(config_file, 'r', encoding='utf-8') as fin:
#         config = json.load(fin)
#
#     host = config.get('host', '127.0.0.1')
#     port = config.get('port', 27017)
#     db_name = config.get('db_name', 'temp')
#     db_user = config.get('db_user', '')
#     db_passwd = config.get('db_passwd', '')
#
#     client = MongoClient(host=host, port=port)
#     if db_user != '':
#         client.admin.authenticate(db_user, db_passwd, mechanism=config.get('mongo_auth_mech', 'SCRAM-SHA-1'))
#     db = client.get_database(db_name)
#
#     return db


class TtjjSpiderPipeline(object):
    def __init__(self):
        self.data_dir = os.path.join('.', 'data')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.data_file = os.path.join(self.data_dir, 'temp.json')
        self.fout = open(self.data_file, 'w', encoding='utf-8')

        # self.db_config_file = os.path.join(self.data_dir, 'db_config.json')
        # self.db = connect_db(self.db_config_file)

    def process_item(self, item, spider):
        data = dict(item)
        print(json.dumps(data, ensure_ascii=False), file=self.fout)

        # if self.db.jijin.find_one(data['fundCode']) is None:
        #     self.db.jijin.insert_one(data)

        return item

    def close_spider(self, spider):
        self.fout.close()
