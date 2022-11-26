import requests
from bs4 import BeautifulSoup
_BASE_URL = 'https://www.mtgstocks.com/prints/'


if __name__=='__main__':
    i_print_num=1
    page = requests.get(_BASE_URL + str(i_print_num), allow_redirects=True)
    soup = BeautifulSoup(page.content, "html.parser")
    with open('test.html','wb') as fileH:
        fileH.write(page.content)
    pass
    print(soup.body.\
          find('app-root').\
          div.\
          div.\
          div)
    pass
