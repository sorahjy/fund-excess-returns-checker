import json

compare_index = ["510310", "110003"]

fund = [
        "009258",
        "007803",
        "001643",
        "011437",
        "000006",
        "009076",
        "163406",
        "001043",
        "003962",
        "470098",
        "001605",
        "002846",
        "005760",
        "001938",
        "007192",
        "008276",
        "519736",
        "002340",
        "008245",
        "163409",
        "160813",
        "519702",
        "519704",
        "166019",
        "040011",
]

fund_extra = [
    "001182",
    "003154",
    "002364",
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
    "003859",
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
