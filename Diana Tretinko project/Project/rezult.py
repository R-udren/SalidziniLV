import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import matplotlib.pyplot as plt

def scrape_rezult(name):
    url = f'https://www.salidzini.lv/cena?q={name}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        projects = soup.find_all('div', class_='item_box_main')

        wb = Workbook()
        ws = wb.active
        ws.append(['Name', 'Shop', 'Price'])

        product_data = []

        for project in projects:
            Name = project.find('h2', class_='item_name').text.strip()
            Shop = project.find('div', class_='item_shop_name').text.strip()
            Price = project.find('div', class_='item_price').text.strip()
            product_data.append([Name, Shop, Price])

        product_data.sort(key=lambda x: float(x[2].replace('€', '').replace(',', '')))

        for row in product_data:
            ws.append(row)

        wb.save('Rezult.xlsx')
        print('Saved')

        prices = [float(row[2].replace('€', '').replace(',', '')) /100 for row in product_data]
        shops = [row[1] for row in product_data]

        plt.barh(shops, prices)
        plt.xlabel('Price')
        plt.ylabel('Shop')
        plt.title('Prices by shops')
        plt.show()

    else:
        print('Mistake')

if __name__ == '__main__':
    style = input('Name of the device: ')
    scrape_rezult(style)