from requests import get, utils
import re



# users_currency_code = input('Введите код валюты, по которой интересует цена по курсу ЦБ: ')

def  currency_rates(price_by_code='USD'):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_code = re.findall(r'(?s)(?<=<CharCode>).*?(?=</CharCode>)', content)
    price_of_one_currency = re.findall(r'(?s)(?<=<Value>).*?(?=</Value>)', content)
    date_currency = re.findall(r'(?s)(?<=Date=").*?(?=" name)', content)
    date_currency = "".join(date_currency)
    currency_dictionary = dict(zip(currency_code, price_of_one_currency))
    for key_code in currency_dictionary:
        if price_by_code == key_code:
            total_currency_amount = currency_dictionary[key_code]

            return print(f'На {date_currency} курс валюты {price_by_code} составляет: {total_currency_amount}')
        # else:
        #     return

# currency_rates(users_currency_code)


