import json

from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from BRO_cards import _SET_NUMS, BRO, BRO_NAME_TO_NUM

_BASE_URL = 'https://www.mtgstocks.com/prints/'
_SET_URL_BASE = 'https://www.mtgstocks.com/sets/'

def add_to_dict(card_Name,key,value):
    if card_Name not in _DICT.keys():
        _DICT[card_Name] = {}
        _DICT[card_Name][key] = value
    elif key not in _DICT[card_Name].keys():
        _DICT[card_Name][key] = value
    return

def write_dict_to_disc():
    print(_DICT)
    with open('mtgmap.json', 'w') as fp:
        json.dump(_DICT, fp)

def load_dict():
    global _DICT
    try:
        with open('mtgmap.json','r') as json_file:
            _DICT = json.load(json_file)
    except FileNotFoundError:
        _DICT={}
    

def scrape_mtg(driver_obj):
    global _DICT

    SET_URLS={}
    for key,value in _SET_NUMS.items():
        SET_URLS[key] =  _SET_URL_BASE + value
    for i_url in SET_URLS.values():
        driver_obj.get(i_url)
        soup = BeautifulSoup(driver_obj.page_source, "html.parser")
        while soup.find('li',{'class':'pagination-next page-item'}) != []:
            soup = BeautifulSoup(driver_obj.page_source, "html.parser")
            cards = soup.find_all('tr')[2:]
            for i, icard in enumerate(cards):
                add_to_dict(icard.a.text,'site_num', icard.a['href'][len('/prints/'):icard.a['href'].index('-')])
                try:
                    raw_val = driver_obj.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[1]/ng-component/div[2]/div/tabset/div/tab[1]/mtg-sets-overview/data-table/div[2]/div/div/table/tbody/tr['+str(i+1)+']/td[4]').text
                except exceptions.NoSuchElementException:
                    #only one page
                    raw_val = driver_obj.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[1]/ng-component/div[2]/div/mtg-sets-overview/data-table/div[2]/div/div/table/tbody/tr['+str(i+1)+']/td[4]').text

                try:
                    val = float(raw_val[1:])
                except ValueError:
                    val =0
                add_to_dict(icard.a.text,'value',val)
            try:
                driver_obj.find_element(By.XPATH,'//li[@class="pagination-next page-item"]').click()
            except exceptions.NoSuchElementException:
                write_dict_to_disc()
                break


if __name__=='__main__':
    load_dict()
    # driver = webdriver.Firefox()
    # scrape_mtg(driver)
    for cat, card_nums in BRO.items():
        if cat not in BRO_NAME_TO_NUM.keys():
            continue
        for i in card_nums:
            if BRO_NAME_TO_NUM[cat][i] in _DICT.keys():
                # print(i, BRO_NAME_TO_NUM[cat][i], _DICT[BRO_NAME_TO_NUM[cat][i]]['value'])
                pass
            else:
                print(i,BRO_NAME_TO_NUM[cat][i])
    '''
    for i_print_num in []:
        if i_print_num in _DICT.values():
            continue
        try:
            driver.get(_BASE_URL + str(i_print_num))
            # page = requests.get(_BASE_URL + str(i_print_num), allow_redirects=True)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            print(soup.find('span', {'class','float-start'}).text)
            _DICT[soup.find('span', {'class','float-start'}).text] = i_print_num
        except AttributeError:
            pass
    write_dict_to_disc()
    '''
