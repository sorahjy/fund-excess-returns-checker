import json

compare_index = ["510310", "510580"]

fund = [
        "519773",
        "040020",
        "005267",
        "005760",
        "001508",
        "001694",
        "000566",
        "008186",
        "168002",
        "673100",
        "000006",
        "006327",
        "501090",
        "001714",
        "001182",
        "000251",
        "163415",
        "163406",
        "003889",
        "001410",
        "001938",
        "519772",
        "007412",
        "005827",
        "002846",
        "001500",
        "519069",
        "519736",
        "005001",
        "001605",
        "160133",
        "000991",
        "000628",
        "450009",
        "470098", 
        "160813"
]

fund_extra = [
    "470018",
    "519768",
    "675111",
    "002742",
    "000171",
    "003429",
    "007915",
    "003547",
    "206018",
    "003327",
    "007010",
    "006852",
    "006387"
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
