import json

compare_index = ["510310", "510580"]

fund = [
        "002148",
        "160133",
        "005001",
        "004263",
        "005738",
        "001473",
        "005267",
        "470098", 
        "001694",
        "000566",
        "008186",
        "673100",
        "000006",
        "006327",
        "501090",
        "001182",
        "163415",
        "163406",
        "003889",
        "005827",
        "001714",
        "002846",
        "000251",
        "001410",
        "001938",
        "519772",
        "007412",
        "001500",
        "001605",
        "519736",
        "009076",
        "001043",
        "519069",
        "000628",
        "005760",
        "450009",
        "160813",
        "008314",
        "004075",
        "006308",
        "001668",
        "004877"
]

fund_extra = [
    "007280",
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
    "003358",
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
