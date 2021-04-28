import json

compare_index = ["510310", "110003","673100"]

fund = [
        "004746",
        "005354",
        "011437",
        "009439",
        "001875",
        "001473",
        "470098",
        "673100",
        "000006",
        "501090",
        "001182",
        "009076",
        "163406",
        "163415",
        "003889",
        "005827",
        "001605",
        "005760",
        "001043",
        "002846",
        "001938",
        "005395",
        "519736",
        "450009",
        "001217",
        "009391",
        "004263",
        "001668",
]

fund_extra = [
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
    "003346",
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
