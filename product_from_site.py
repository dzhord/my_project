import requests
from bs4 import BeautifulSoup

def get_html(url):
    #https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty?p=2
    headers = {'User-agent': 'Mozilla/5.0'}
    param = { 'p': '1'}
    SITE_URL = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty"
    try:
        result = requests.get(SITE_URL, headers=headers, params=param)
        return result.text
    except(requests.exceptions.ConnectionError):
        print("No connection")
        return False

def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')

    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1]
    return int(total_pages)
    
def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='description item_table-description')
    # Невыципил данные об товарах
    s = len(ads)
    print(ads)
    print(s)

def get_html_product():
    url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty?p=1"
    base_url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty?"
    page_part = 'p='
    
    total_pages = get_total_pages(get_html(url))

    for i in range(1,3):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)

    return total_pages

if  __name__ == "__main__":
    get_html_product()

'''
    if html:
        with open("avito.html", "w", encoding="utf8") as ff:
            ff.write(html)
'''

