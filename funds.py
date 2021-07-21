import json

compare_index = ["510310", "110003"]

fund = [
        "007192",
        "166019",
        "001217",
        "008276",
        "007803",
        "163409",
        "001644",
        "169104",
        "011437",
        "004605",
        "011437",
        "000006",
        "163406",
        "009076",
        "001043",
        "001182",
        "163415",
        "003889",
        "001605",
        "005760",
        "519736",
        "002846",
        "001938",
        "470098",
        "002340",
        "004263",
        "001473",
]

fund_extra = [
    "003154",
    "002364",
    "485111",
    "470018",
    "519768",
    "002742",
    "000171",
    "003429",
    "007915",
    "003547",
    "206018",
    "233005",
    "003358",
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
