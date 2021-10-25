import json

compare_index = ["510310", "110003"]

fund = [
        "450004",
        "004475",
        "000547",
        "001532", #013116
        "550015",
        "002258",
        "519126", #013259
        "009708",
        "009369",
        "009258",
        "010728",
        "009243",
        "000006",
        "003962",
        "001043",
        "006039",
        "002846",
        "519702",
        "470098",
        "001938",
        "008276",
        "002340",
        "008245",
        "163409",
        "160813",
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
    "003358",
    "003859",
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
