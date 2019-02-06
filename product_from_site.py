import requests


def download_product():
    headers = {'User-agent': 'Mozilla/5.0'}
    param = { 'p': '1'}
    SITE_URL = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty"
    try:
        result = requests.get(SITE_URL, headers=headers, params=param)
        data = result.text
        print(result)
        return data
    except(requests.exceptions.ConnectionError):
        print("No connection")
        return False

if  __name__ == "__main__":
    html = download_product()
    if html:
        with open("avito.html", "w", encoding="utf8") as ff:
            ff.write(html)
