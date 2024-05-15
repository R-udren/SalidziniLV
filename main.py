import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook
import matplotlib.pyplot as plt

def scrape_result(name):
    url = f'https://www.salidzini.lv/cena?q={name}'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raise exception if status code is 4xx or 5xx

    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='item_box_main')

    product_data = []

    for product in products:
        name = product.find('h2', class_='item_name').text.strip()
        shop = product.find('div', class_='item_shop_name').text.strip()
        raw_price = product.find('div', class_='item_price').text.strip()
        price = float(raw_price.replace('€', '').replace(',', '.'))  # TODO: replace with regex
        product_data.append((name, shop, price))

    return product_data.sort(key=lambda x: x[2])

def save_to_excel(product_data):
    wb = Workbook()
    ws = wb.active
    ws.append(['Name', 'Shop', 'Price'])

    for row in product_data:
        ws.append(row)
    try:
        wb.save('Result.xlsx')
        print('Saved')
    except PermissionError:
        print('Please close the file and try again')
    except Exception as e:
        print('Error:', e)



def plot_prices(product_data):
    plt.barh([x[1] for x in product_data], [x[2] for x in product_data])
    plt.xlabel('Price')
    plt.ylabel('Shop')
    plt.title('Prices by shops')
    plt.show()


def main():
    name = input('Enter product name: ').replace(' ', '+')

    try:
        product_data = scrape_result(name)
    except Exception as e:
        print('Error:', e)
        return

    try:
        save_to_excel(product_data)
    except Exception as e:
        print('Error:', e)
        return

    plot_prices(product_data)


if __name__ == '__main__':
    main()
