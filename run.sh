rm -rf ./.scrapy/*
python funds.py
scrapy crawl jijin
python generate_output.py