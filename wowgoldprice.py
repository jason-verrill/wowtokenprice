import requests
import os


def get_wow_token_price():
    res = requests.get('https://www.wowhead.com/')

    gold_price = ''
    search_phrase = 'moneygold'
    offset = 3
    index_start = res.text.find(search_phrase) + len(search_phrase) + offset
    max_characters = 10
    
    substring = res.text[index_start : index_start + max_characters]

    for i in substring:
        if (i == '<'):
            break

        gold_price += i

    print('Gold token price:', gold_price)


def main():
    get_wow_token_price()
    os.system('PAUSE')
        
    
if (__name__ == '__main__'):
    main()
